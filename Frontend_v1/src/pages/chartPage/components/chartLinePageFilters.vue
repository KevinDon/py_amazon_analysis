<template rel="linePageFilter" xmlns:el-col="http://www.w3.org/1999/html">
  <div class="main" style="width: 230px;">
    <el-dialog title="LINE 选择"
               :visible.sync="dialogLineSelectShow"
               :modal="true"
               top="5vh"
               :append-to-body="true"
               :close-on-click-modal="false"
               @opened="dialogLineShowHandle">
      <el-row :gutter="24" style="z-index:2048">
        <!--搜索栏-->
        <el-col :span="14">
          <el-input placeholder="输入LINE的名字进行搜索" v-model="lineSearchWord"
                    class="input-with-select"
                    size="mini">
            <el-button slot="append" type="primary" class="el-icon-third  el-icon-search"
                       @click="btnSearchHandle"></el-button>
          </el-input>
        </el-col>
      </el-row>
      <el-row :gutter="24" style="height: 70vh;z-index:2048">
        <el-col :span="14">
          <!--左侧筛选表格-->
          <el-table
            class="compact"
            ref="multipleTable"
            v-loading="lineListTableLoading"
            :data="lineListData"
            style="width: 100%;margin-top:.5em;min-height: 400px;max-height: 500px;"
            max-height="500"
            :select-on-indeterminate="false"
            :header-row-style="{height:'32px'}"
            @select="dialogTableRowSelectedHandle"
            @row-click="dialogTableCheckSelect"
          >
            <!--字段-->
            <el-table-column
              class="table-column"
              type="selection"
              @filter-method="dialogSkuFilterFunc"
              width="55">
            </el-table-column>
            <el-table-column
              class="table-column"
              prop="title"
              label="Title">
            </el-table-column>
          </el-table>
          <!--分页-->
          <el-row>
            <el-col align="center">
              <el-pagination
                small
                background
                layout="prev, pager, next"
                :page-count="lineListTableTotalPage"
                :current-page.sync="lineListTableCurrentPage"
                @current-change="skuListTablePageChangeHandle">
              </el-pagination>
            </el-col>
          </el-row>
        </el-col>
        <el-col :span="10">
          <!--右侧表格-->
          <el-table
            class="compact"
            v-loading="lineListTableLoading"
            :data="lineListSelectedTemp"
            style="width: 100%; margin-top:.5em;min-height: 400px;max-height: 500px;"
            max-height="600">
            <el-table-column
              prop="title"
              label="Selected LINE">
            </el-table-column>
          </el-table>
        </el-col>
      </el-row>
      <div slot="footer" class="dialog-footer" align="center">
        <el-button @click="dialogCancelHandle" size="mini">取 消</el-button>
        <el-button type="primary" @click="dialogSubmitHandle" size="mini">确 定</el-button>
      </div>
    </el-dialog>

    <el-row style="margin:1em auto">
      <h3>{{$t('w.'+route_cur_name)}}</h3>
      <div  style="text-align: left; line-height: 40px; padding: 0 0 10px;">
        LINE筛选({{totalSelectItems.length}})
      </div>
      <el-table
        class="compact"
        :data="$store.getters.getFilterLineSelectData"
        style="width: 300px;margin: auto;"
        max-height="450">
        <el-table-column
          prop="title"
          label="Product Line"
        ></el-table-column>
        <el-table-column
          fixed="left"
          width="42" align="center">
          <template slot-scope="scope">
            <el-button
              @click="deleteLineSelectRow(scope)"
              type="text" style="color:red"
              size="mini" icon="el-icon-circle-close-outline">
            </el-button>
          </template>
          <template slot="header" slot-scope="scope">
            <!--弹出框按钮-->
            <el-button
              icon="el-icon-plus"
              size="mini"
              class="submini-2px"
              style="background: rgb(64, 158, 255); color: #fff; border: none;"
              @click="dialogLineSelectShow = true"
              ></el-button>
          </template>
        </el-table-column>


      </el-table>
    </el-row>

    <el-form :label-position='labelPosition' ref="form" label-width="80" >
      <el-form-item label="开始日期">
        <el-date-picker
          v-model="dateSelected[0]"
          type="date"
          placeholder="开始日期"
          format="yyyy-MM-dd"
          value-format="yyyy-MM-dd"
          style="width:230px">
        </el-date-picker>
      </el-form-item>
      <el-form-item label="结束日期">
        <el-date-picker
          v-model="dateSelected[1]"
          type="date"
          placeholder="结束日期"
          format="yyyy-MM-dd"
          value-format="yyyy-MM-dd"
          style="width:230px">
        </el-date-picker>
      </el-form-item>
      <el-form-item label="表格选择">
        <el-checkbox-group v-model="chartSelected" size="mini">
          <el-checkbox v-for="chartMode in chartModes"
                       :label="chartMode.name"
                       :key="chartMode.name"
                       style=" color: #f3f3f3; float: left; line-height: 32px; width: 100%; text-align: left;"
          >
            {{chartMode.label}}
          </el-checkbox>
        </el-checkbox-group>
      </el-form-item>
    </el-form>

    <el-row style="margin-top: 30px;">
      <el-button size="mini" style="background: #409EFF; color: #fff; border: none;"
                 :disabled="lineListSelected.length < 1" @click="getRemoteDataChartHandle">刷新
      </el-button>
    </el-row>
  </div>
</template>

<script>
  import Configs from '@/lib/sysConfig';
  import Moment from 'moment';
  import ChartApi from '@/pages/chartPage/lib/chartApiHandler.js';

  export default {
    name: "chartPageFilters",
    props: {
      getLineUrl: '',
      getDailyReportUrl: '',
      getMonthlyReportUrl: '',
      getWeeklyReportUrl: '',
      chartModes: {
        type: Array
      },
    },
    data() {
      return {
        labelPosition:'left',
        maxSelect: 20,
        //  即使搜索
        lineSearch: '',
        //  请求搜索
        lineSearchWord: '',
        dialogLineSelectShow: false,
        lineListTableInit: true,
        chartSelected: ["chart_daily", "chart_monthly", "chart_weekly"],

        //  选择临时表
        lineListSelectedTemp: [],

        lineListTableCurrentPage: 1,
        lineListTableTotalPage: 1,
        lineListTablePageSize: Configs.system.query.pageSize + 0,
        lineListTableLoading: false,

        filterMethod(query, item) {
          return item.pinyin.indexOf(query) > -1;
        },

        dateSelected: [
          Moment().subtract(1, 'years').format('YYYY-MM-DD'), Moment().format('YYYY-MM-DD')
        ]
      }
    },
    methods: {
      //  Line选择弹框初始化
      dialogLineShowHandle: function () {
        let vm = this;
        if (!!vm.lineListTableInit) {
          vm.dialogLineGetHandle(vm.lineListTablePageFilter, vm.inputSearchWordFilter)
        }
        // vm.lineListTableInit = false;
      },
      //  Line获取处理
      dialogLineGetHandle: async function (form = {}, filter = []) {
        let vm = this;
        vm.dialogLineSelectShow = true;
        vm.lineListTableLoading = true;
        console.log(form);
        await ChartApi.fetchProductLineData(vm.getLineUrl, form, filter).then(response => {
          // vm.skuListTable = [...response.data];
          vm.$store.dispatch('updateLineListData', response.data);
          if (response.tp < 1) {
            // vm.skuListTable = [];
            vm.$store.dispatch('updateLineListData', []);
          }
          vm.lineListTableTotalPage = response.tp;
          vm.lineListTableLoading = false;
        }).catch(err => {
          vm.$message.error(err.message || vm.$i18n.t('操作失败'));
          vm.lineListTableLoading = false;
        });
      },
      //  单击表格行事件
      dialogTableCheckSelect: function (row, col, event) {
        let vm = this;
        vm.dialogTableRowSelectedHandle(vm.$refs.multipleTable.selection, row)
      },
      /**
       * @deprecated 暂停使用
       * */
      dialogSkuListTableSelectionChange(val) {
        let vm = this;
        console.log('补勾选sku');
        //  根据已选择的sku勾选左侧sku
        vm.totalSelectItems.forEach(item => {
          for (let index in vm.lineListData) {
            let row = vm.lineListData[index];
            console.log(row);
            if (item.id == row.id) {
              vm.$refs.multipleTable.toggleRowSelection(item, true)
              vm.$refs.multipleTable.toggleRowSelection(row, true)
            }
          }
        })
      },
      //  勾选左侧  table
      dialogTableRowSelectedHandle(selection, row) {
        let vm = this;
        let rowExist = vm.lineListSelectedTemp.filter(val => row.id == val.id);
        console.log('重复勾选检查', rowExist);

        //  临时选择数据中没有重复就push
        if (rowExist.length < 1) {
          console.log('没有重复就加入', rowExist.length < 1, rowExist);
          if (vm.lineListSelectedTemp.length < vm.maxSelect) {
            let temp = vm.lineListSelectedTemp;
            temp.push(row);
            // vm.$store.dispatch('updateLineSelectedListTempData', temp);
            vm.$refs.multipleTable.toggleRowSelection(row, true);
          } else {
            //  临时选择的个数超过了最大选择
            vm.$message.warning(`可选择的SKU不可超过${vm.maxSelect}个`);
            vm.$refs.multipleTable.toggleRowSelection(row, false);
            return false;
          }
        } else {
          //  已有选择则去掉勾选
          vm.lineListSelectedTemp.splice(vm.lineListSelectedTemp.indexOf(row), 1);
          vm.$refs.multipleTable.toggleRowSelection(row, false);

          console.log('重复了就去掉', rowExist.length > 0, rowExist);
        }
      },
      // 弹出框 cancel
      dialogCancelHandle: function () {
        let vm = this;
        // vm.lineListSelected = [];
        vm.$store.dispatch('updateLineSelectedListData', []);
        vm.dialogLineSelectShow = false;
      },
      //  弹出框 submit
      dialogSubmitHandle: function () {
        let vm = this;
        if (vm.totalSelectItems.length > 20) {
          vm.$message.warning('选择的SKU超过20个');
          return false;
        }
        //  重置控件
        vm.lineSearchWord = '';
        vm.lineListTableCurrentPage = 1;
        vm.$store.dispatch('updateLineSelectedListData', [...vm.totalSelectItems]);
        vm.lineListSelectedTemp = [];
        vm.dialogLineSelectShow = false;

      },
      //
      getRemoteDataChartHandle: function () {
        let form = {
          itemSelected: this.lineListSelected,
          dateSelected: this.dateSelected,
          chartSelected: this.chartSelected,
        };
        // console.log(form);
        this.$emit('listenFilterSubmit', form)
      },
      dialogSkuFilterFunc: function (value, row, col) {
        console.log(value, '123');
      },
      deleteLineSelectRow: function (row) {
        console.log(row);
        let temp = [...this.lineListSelected];
        temp.splice(row.$index, 1);
        this.$store.dispatch('updateLineSelectedListData', temp)
        // this.lineListSelected.splice(row.$index, 1);
      },
      skuListTablePageChangeHandle: function (cp) {
        console.log(cp);
        let vm = this;
        vm.lineListTableCurrentPage = cp;
        vm.dialogLineGetHandle(vm.lineListTablePageFilter, vm.inputSearchWordFilter)
      },
      /**
       * 关键字搜索
       * @param val
       * @returns {Promise<void>}
       */
      btnSearchHandle: async function (val) {
        let vm = this;
        vm.lineListTableCurrentPage = 1;
        vm.dialogLineGetHandle(vm.lineListTablePageFilter, vm.inputSearchWordFilter)
      }
    },
    computed: {
      //  line selected list
      lineListSelected: vm => vm.$store.getters.getFilterLineSelectData,
      //  line list
      lineListData: vm => vm.$store.getters.getFilterLineData,
      //  chart表类型
      chartType: vm => vm.$store.getters.getPageSeries,
      //  远程关键字搜索filter
      inputSearchWordFilter: function () {
        let vm = this;
        let _queryParams = [];
        vm.lineListTableCurrentPage = 1;
        if (!!vm.lineSearchWord) {
          //  拼装传递的搜素内容
          _queryParams.push([{"title-ilk": vm.lineSearchWord}]);
        }
        return _queryParams;
      },
      //  line 表分页 filter
      lineListTablePageFilter: function () {
        let vm = this;
        return {page: vm.lineListTableCurrentPage, size: vm.lineListTablePageSize || Configs.system.query.pageSize};
      },


      skuListTableFiltered: function () {
        let vm = this;
        let res = !!vm.lineSearch ? vm.lineListData.filter(item => item.sku.match(new RegExp(vm.lineSearch, 'i'))) : vm.lineListData;
        return res;
      },
      /**
       * 合计已选择内容,包括临时选择与已选择
       * @returns {*[]}
       */
      totalSelectItems: function () {
        let vm = this, _skuList;

        _skuList = vm.lineListSelectedTemp.filter(item => {
          let _repeated;
          for (let index in vm.lineListSelected) {
            _repeated = vm.lineListSelected[index]['id'] == item['id'];
            if (_repeated == true) {
              break;
            }else {
              _repeated = false
            }
          }
          return !_repeated
        });

        console.log('去重选择列表', _skuList);

        return _skuList.concat(vm.lineListSelected);
      },
      route_cur_name: function () {
        return this.$route.name
      },

    },
    mounted() {
      this.$store.dispatch('updatePageSeries', this.$route.meta.series);
    }
  }
</script>

<style lang="stylus">
  .el-checkbox__label
    display inline-block !important

  .compact
    .el-table__row td
      padding 3px

    .el-table__row
      cursor: pointer;

    thead
      th
        padding 3px
        background rgba(5, 28, 31, 0.04)

  th .el-checkbox__input
    display none

  button.submini-2px
    padding 2px 2px;

  .el-form-item__label
    color: #f3f3f3;
    float :left!important;

  .el-checkbox-group
    margin: 0;
    padding: 0;
    float: left;
    width: 100%

</style>
