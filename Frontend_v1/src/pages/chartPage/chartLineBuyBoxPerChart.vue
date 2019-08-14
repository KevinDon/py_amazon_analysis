<template>
  <el-container>
    <el-aside class="aside" :class="!!asideShow?'aside-show':'aside-hide'">
      <div class="aside-toggle-btn">
        <el-button icon="el-icon-d-arrow-left" circle size="mini"
                   v-if="!!asideShow"
                   v-on:click="asideToggleHandler(!asideShow)">

        </el-button>
        <el-button icon="el-icon-d-arrow-right" circle size="mini"
                   v-else
                   @click="asideToggleHandler(!asideShow)">

        </el-button>
      </div>

      <side-filter
        :chartModes="chartModes"
        getLineUrl="/v1/statamazonline/"
        @listenFilterSubmit="filterSubmit"
        v-loading.fullscreen.lock="fullscreenLoading"
      ></side-filter>
    </el-aside>
    <el-container>
      <el-main id="main-box" :style="!!fixShow ? 'margin :0 0 0 270px;' : ''">
        <h1>Report List</h1>
        <div class="chart-box" v-show.sync="showDailyChart">
          <div class="chart" id="chartDaily"></div>
        </div>
        <!--        <div class="chart-box" v-show.sync="showMonthlyChart">-->
        <!--          <div class="chart" id="chartMonthly"></div>-->
        <!--        </div>-->
        <!--        <div class="chart-box" v-show.sync="showWeeklyChart">-->
        <!--          <div class="chart" id="chartWeekly"></div>-->
        <!--        </div>-->
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
  // 引入 ECharts 全模块 todo 日后精简
  import ChartsApi from "@/pages/chartPage/lib/chartApiHandler.js";
  import ChartDataHandler from './chartDataHandler';


  // // 引入 ECharts 主模块
  // var echarts = require('echarts/lib/echarts');
  // // 引入线图
  // require('echarts/lib/chart/line');
  // // 引入提示框和标题组件
  // require('echarts/lib/component/legend');
  // require('echarts/lib/component/grid');
  // require('echarts/lib/component/tooltip');
  // require('echarts/lib/component/title');
  // require('echarts/lib/component/dataZoom');

  const echarts = require('echarts/echarts.all');

  export default {
    name: "chartLineBuyBoxPerChart",
    components: {
      sideFilter: () => import('./components/chartLinePageFilters.vue')
    },
    data() {
      return {
        chartModes: [
          {label: '日统计表', name: 'chart_daily'},
          // {label: '月统计表', name: 'chart_monthly'},
          // {label: '周统计表', name: 'chart_weekly'}
          ],
        screenWidth: document.body.clientWidth,
        fullscreenLoading: false,
        asideShow: true,
        queryForm: [],
        dailyChart: null,
        monthlyChart: null,
        weeklyChart: null,
        chartData: [],
        chartSelected: ['chart_daily', 'chart_monthly', 'chart_weekly'],
      }
    },
    mounted: function () {
      let vm = this;
      vm.dailyChart = echarts.init(document.getElementById('chartDaily'), 'canvas', 'auto', 'auto');
      // vm.monthlyChart = echarts.init(document.getElementById('chartMonthly'), 'canvas', 'auto', 'auto');
      // vm.weeklyChart = echarts.init(document.getElementById('chartWeekly'), 'canvas', 'auto', 'auto');
      window.onresize = () => {
        return (() => {
          window.screenWidth = document.body.clientWidth
          vm.screenWidth = window.screenWidth;
        })()
      }
    },
    methods: {

      asideToggleHandler: function (val) {
        let vm = this;
        console.log('切换侧栏');
        vm.asideShow = val;
        setTimeout(() => {
            ChartDataHandler.chartResizeHandle(vm.dailyChart);
            // ChartDataHandler.chartResizeHandle(vm.monthlyChart);
            // ChartDataHandler.chartResizeHandle(vm.weeklyChart);
          }, 500
        )
      },
      filterSubmitHandle: async function (form) {
        let vm = this;
        let _params = [];

        //  处理查询语句
        if (form.itemSelected.length > 0) {
          let _filter = [];
          form.itemSelected.forEach(item => {
            if (item != undefined) {
              _filter.push({'line_id-eq': item.id})
            }
          });
          _params.push(_filter)
        }

        let _beginDate, _endDate;
        //  处理date查询
        // if (form.dateSelected.length > 0) {
        _beginDate = form.dateSelected[0];
        _endDate = form.dateSelected[1];
        // }
        //  处理chart查询
        if (form.chartSelected.length > 0) {
          vm.chartSelected = form.chartSelected;
          if (vm.showDailyChart) {
            let queryParams = [..._params];
            queryParams.push([{'dy-gte-and': _beginDate}]);
            queryParams.push([{'dy-lte-and': _endDate}]);
            await ChartsApi.fetchstatamazonlinedaily('/v1/statamazonlinebuyboxday/', {
              order: ['dy','line_id'],
              size: 500000
            }, queryParams).then(response => {
              console.log(response);
              vm.daliyChartOptions = ChartDataHandler.lineDailyChangHandle(vm.dailyChart, response.data, vm);
            }).catch(err => {
              console.log(err);
            });
          }

          // if (vm.showMonthlyChart) {
          //   let queryParams = [..._params];
          //   queryParams.push([{'first_day-gte-and': _beginDate}]);
          //   queryParams.push([{'last_day-lte-and': _endDate}]);
          //   await ChartsApi.statamazonskutotalitemsmonth({}, queryParams).then(data => {
          //     vm.monthlyChartOptions = ChartDataHandler.skuMonthlyChangeHandle(vm.monthlyChart, data, vm);
          //   });
          //
          // }
          // if (vm.showWeeklyChart) {
          //   let queryParams = [..._params];
          //   queryParams.push([{'first_day-gte-and': _beginDate}]);
          //   queryParams.push([{'last_day-lte-and': _endDate}]);
          //   await ChartsApi.statamazonskutotalitemsweek({}, queryParams).then(data => {
          //     vm.weeklyChartOptions = ChartDataHandler.skuWeeklyChangeHandle(vm.weeklyChart, data, vm);
          //   });
          // }
        }
      },
      //  筛选器刷新
      filterSubmit: async function (form) {
        let vm = this;

        vm.fullscreenLoading = true;
        await vm.filterSubmitHandle(form).then(res => {
          vm.fullscreenLoading = false;
          vm.$message.success(vm.$i18n.t('message.success'))
        }).catch(e => {
          vm.fullscreenLoading = false;
          vm.$message.error(e)
        })

      },
      chartResizeHandle() {

      }
    },
    computed: {
      showDailyChart: function () {
        return this.chartSelected.indexOf('chart_daily') >= 0
      },
      // showMonthlyChart: function () {
      //   return this.chartSelected.indexOf('chart_monthly') >= 0
      // },
      // showWeeklyChart: function () {
      //   return this.chartSelected.indexOf('chart_weekly') >= 0
      // }
    },
    watch: {
      screenWidth(val) {
        if (!this.timer) {
          this.screenWidth = val;
          this.timer = true;
          let vm = this;
          setTimeout(function () {
            // that.screenWidth = that.$store.state.canvasWidth
            console.log(vm.screenWidth);
            // vm.init();
            ChartDataHandler.chartResizeHandle(vm.dailyChart);
            // ChartDataHandler.chartResizeHandle(vm.monthlyChart);
            // ChartDataHandler.chartResizeHandle(vm.weeklyChart);
            vm.timer = false
          }, 500)
        }
      },
    }
  }
</script>

<style lang="stylus" scoped>
  .chart
    &-box
      margin: 3em 0;
    width: 100%
    height: 500px

  .el-checkbox-group
    text-align: left;
</style>
