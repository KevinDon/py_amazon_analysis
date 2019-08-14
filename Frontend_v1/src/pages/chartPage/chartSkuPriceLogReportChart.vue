<template>
  <el-container>
    <div class="side-box mark el-icon-d-arrow-right" :class="(!!asideShow || fixShow)?'hide':'show'" @mouseover="asideToggleHandler(!asideShow)"></div>
    <el-aside class="aside"  :class="!!asideShow?'aside-show':'aside-hide'"  style="background: rgb(48, 65, 86); float: left; position: fixed; height: 100%;bottom: 0;left: 0; right: 0;z-index: 99;"
              @mouseleave.native="asideToggleHandler(false)"
    >
      <div class="aside-toggle-btn">
        <el-button class="el-icon-third el-icon-ping" style="border: none; padding: 5px; margin: 0 5px 0 0 " :class="!!fixShow ? 'fix' : 'nofix'" v-on:click="fixShow = !fixShow"></el-button>
      </div>
      <side-filter
        :chartModes="chartModes"
        getSkuUrl="/v1/statamazonsku/"
        @listenFilterSubmit="filterSubmit" v-loading.fullscreen.lock="fullscreenLoading"></side-filter>
    </el-aside>
    <el-container>
      <el-header style="">
        <!--        <h1 class="report-title">-->
        <!--          <span>Report List</span>-->
        <!--        </h1>-->
      </el-header>
      <el-main id="main-box" :style="!!fixShow ? 'margin :0 0 0 270px;' : ''">
        <div class="chart-box" v-show.sync="showDailyChart">
          <div class="chart" id="chartDaily"></div>
        </div>
        <div class="chart-box" v-show.sync="showMonthlyChart">
          <div class="chart" id="chartMonthly"></div>
        </div>
        <div class="chart-box" v-show.sync="showWeeklyChart">
          <div class="chart" id="chartWeekly"></div>
        </div>
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
    name: "chartSkuPriceLogReportChart",
    components: {
      sideFilter: () => import('./components/chartSkuPageFilters.vue')
    },
    data() {
      return {
        chartModes: [{label: '日统计表', name: 'chart_daily'},
          {label: '月统计表', name: 'chart_monthly'},
          {label: '周统计表', name: 'chart_weekly'}],
        screenWidth: document.body.clientWidth,
        fullscreenLoading: false,
        fixShow:true,
        asideShow: true,
        queryForm: [],
        dailyChart: null,
        monthlyChart: null,
        weeklyChart: null,
        chartData: [],
        chartSelected: ['chart_daily'],
      }
    },
    mounted: function () {
      let vm = this;
      vm.dailyChart = echarts.init(document.getElementById('chartDaily'), 'canvas', 'auto', 'auto');
      vm.monthlyChart = echarts.init(document.getElementById('chartMonthly'), 'canvas', 'auto', 'auto');
      vm.weeklyChart = echarts.init(document.getElementById('chartWeekly'), 'canvas', 'auto', 'auto');
      window.onresize = () => {
        return (() => {
          window.screenWidth = document.body.clientWidth;
          vm.screenWidth = window.screenWidth;
        })()
      }
    },
    methods: {

      asideToggleHandler: function (val) {
        let vm = this;
        console.log('切换侧栏');
        vm.asideShow = vm.fixShow ? true: val;
        setTimeout(() => {
            ChartDataHandler.chartResizeHandle(vm.dailyChart);
            ChartDataHandler.chartResizeHandle(vm.monthlyChart);
            ChartDataHandler.chartResizeHandle(vm.weeklyChart);
          }, 500
        )
      },
      filterSubmitHandle: async function (form) {
        let vm = this;
        let _params = [];

        //  处理sku查询语句
        if (form.skuSelected.length > 0) {
          let _filter = [];
          form.skuSelected.forEach(item => {
            if (item != undefined) {
              _filter.push({'sku-eq': item.sku})
            }
          });
          _params.push(_filter)
        }
        console.log(_params);
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
            await ChartsApi.statamazonskutotalitemsday('/v1/statamazonskupricelogday/',{}, queryParams).then(response => {
              vm.daliyChartOptions = ChartDataHandler.skuDailyChangHandle(vm.dailyChart, response.data, vm);
            });
          }

          if (vm.showMonthlyChart) {
            let queryParams = [..._params];
            queryParams.push([{'first_day-gte-and': _beginDate}]);
            queryParams.push([{'last_day-lte-and': _endDate}]);
            await ChartsApi.statamazonskutotalitemsmonth('/v1/statamazonskupricelogmonth/',{}, queryParams).then(response => {
              vm.monthlyChartOptions = ChartDataHandler.skuMonthlyChangeHandle(vm.monthlyChart, response.data, vm);
            });

          }
          if (vm.showWeeklyChart) {
            let queryParams = [..._params];
            queryParams.push([{'first_day-gte-and': _beginDate}]);
            queryParams.push([{'last_day-lte-and': _endDate}]);
            await ChartsApi.statamazonskutotalitemsweek('/v1/statamazonskupricelogweek/',{}, queryParams).then(response => {
              vm.weeklyChartOptions = ChartDataHandler.skuWeeklyChangeHandle(vm.weeklyChart, response.data, vm);
            });
          }
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
      showMonthlyChart: function () {
        return this.chartSelected.indexOf('chart_monthly') >= 0
      },
      showWeeklyChart: function () {
        return this.chartSelected.indexOf('chart_weekly') >= 0
      }
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
            ChartDataHandler.chartResizeHandle(vm.monthlyChart);
            ChartDataHandler.chartResizeHandle(vm.weeklyChart);
            vm.timer = false
          }, 500)
        }
      },
    }
  }
</script>

<style lang="stylus" scoped>
  #main-box
    /*margin :0 0 0 270px;*/
    .chart
      &-box
        margin: 3em 0;
      width: 100%
      height: 500px

    .el-checkbox-group
      text-align: left;

    .transition-box
      margin-bottom: 10px;
      width: 200px;
      height: 100px;
      border-radius: 4px;
      background-color: #409EFF;
      text-align: center;
      color: #fff;
      padding: 40px 20px;
      box-sizing: border-box;
      margin-right: 20px;
    h1.report-title
      color: #909399;
      margin :0;
      text-align: left;
      background: #f3f3f3;
      line-height: 40px;
      padding-left: 5px;
    .mark
      width: 15px;
      background: #cecece;
      z-index: 999;
      height: 100%;
      text-align: center;
      cursor pointer;
      position :fixed;
      padding-top: 18%;
    .aside
      & >.side-box
        width 230px;
        margin:  0 0 0 20px;
        position fixed;
    .open-aside
      width: 256px!important
    .hide-aside
      width: 15px!important;

    .fix
      color: #fff;
      background : none;
      -webkit-transform: rotate(315);
      transform: rotate(315deg);
      -webkit-transition: -webkit-transform 1s linear;
      transition: all 0.2s ease-in-out;

    .nofix
      color: #cecece;
      background : none;
      -webkit-transform: rotate(-5);
      transform: rotate(-5deg);
      -webkit-transition: -webkit-transform 1s linear;
      transition: all 0.2s ease-in-out;
</style>
