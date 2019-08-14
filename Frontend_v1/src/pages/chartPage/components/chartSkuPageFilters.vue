<template xmlns:el-col="http://www.w3.org/1999/html">
  <div class="main" style="width: 230px;">


    <product-dialog
      :propProductSelectShow="dialogSkuSelectShow"
      v-on:dialogSubmitCallback="dialogSubmitCallBack"
      @closeMe="onShowProductDialogChange"
      :propGetSkuUrl="getSkuUrl"
      :propMaxSelect="maxSelect"
    >
    </product-dialog>

    <el-row style="margin:5px auto" v-if="chartType == 'sku'">
      <h3>{{$t('w.'+route_cur_name)}}</h3>
      <div style="text-align: left; line-height: 40px; padding: 0 0 0 0">
        SKU筛选({{totalSelectSkuItems.length}})
      </div>
      <el-table
        class="compact"
        :data="$store.getters.getFilterSkuSelectData"
        style="width: 235px;margin: auto;"
        max-height="350">
        <el-table-column
          prop="sku"
          label="SKU"
        ></el-table-column>

        <el-table-column
          fixed="left"
          width="42" align="center">
          <template slot-scope="scope">
            <el-button
              @click="deleteSkuSelectRow(scope)"
              type="text" style="color:red"
              size="mini" icon="el-icon-circle-close-outline">
            </el-button>
          </template>
          <template slot="header" slot-scope="scope">
            <el-button
              icon="el-icon-plus"
              size="mini"
              class="submini-2px"
              style="background: rgb(64, 158, 255); color: #fff; border: none;"
              @click="dialogSkuSelectShow = true"
            ></el-button>
          </template>

        </el-table-column>

      </el-table>
    </el-row>

    <el-row style="margin:5px auto" v-show="isKeyword">
      <div style="text-align: left; line-height: 40px; padding: 0 0 0 0;">
        Keyword筛选({{totalSelectKeywordItems.length || 0}})
      </div>
      <el-table
        class="compact"
        :data="$store.getters.getFilterKeywordSelectData"
        style="width: 300px;margin: auto;"
        max-height="450">

        <el-table-column
          fixed="left"
          width="42" align="center">
          <template slot-scope="scope">
            <el-button
              @click="deleteKeywordSelectRow(scope)"
              type="text" style="color:red"
              size="mini" icon="el-icon-circle-close-outline">
            </el-button>
          </template>
          <template slot="header" slot-scope="scope">
            <el-button
              icon="el-icon-plus"
              size="mini"
              class="submini-2px"
              style="background: rgb(64, 158, 255); color: #fff; border: none;"
              @click="dialogKeywordSelectShow = true"
            ></el-button>
          </template>

        </el-table-column>
        <el-table-column
          prop="title"
          label="Keyword"
        ></el-table-column>
      </el-table>
    </el-row>

    <keyword-dialog
      :propKeywordSelectShow="dialogKeywordSelectShow"
      v-on:dialogSubmitCallback="dialogSubmitCallBack"
      @closeMe="onShowKeywordDialogChange"
      :propGetKeywordUrl="getKeywordUrl"
      :propMaxSelect="maxSelect"
    ></keyword-dialog>


    <el-row style="margin:5px auto" v-show="isCategory">
      <div style="text-align: left; line-height: 40px; padding: 0 0 0 0;">
        Category筛选({{totalSelectCategoryItems.length ||0}})
      </div>
      <el-table
        class="compact"
        :data="$store.getters.getFilterCategorySelectData"
        style="width: 300px;margin: auto;"
        max-height="450">

        <el-table-column
          fixed="left"
          width="42" align="center">
          <template slot-scope="scope">
            <el-button
              @click="deleteCategorySelectRow(scope)"
              type="text" style="color:red"
              size="mini" icon="el-icon-circle-close-outline">
            </el-button>
          </template>
          <template slot="header" slot-scope="scope">
            <el-button
              icon="el-icon-plus"
              size="mini"
              class="submini-2px"
              style="background: rgb(64, 158, 255); color: #fff; border: none;"
              @click="dialogCategorySelectShow = true"
            ></el-button>
          </template>

        </el-table-column>
        <el-table-column
          prop="title"
          label="Category"
        ></el-table-column>
      </el-table>
    </el-row>

    <category-dialog
      :propCategorySelectShow="dialogCategorySelectShow"
      v-on:dialogSubmitCallback="dialogSubmitCallBack"
      @closeMe="onShowCategoryDialogChange"
      :propGetCategoryUrl="getCategoryUrl"
    ></category-dialog>

    <el-form :label-position='labelPosition' ref="form" label-width="80">
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
                 :disabled="skuListData.length < 1" @click="getRemoteDataChartHandle">生成
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
    components: {
      categoryDialog: () => import('./categoryDialog.vue'),
      productDialog: () => import('./productDialog.vue'),
      keywordDialog: () => import('./keywordDialog.vue')
    },

    props: {
      getKeywordUrl: '',
      getSkuUrl: '',
      getCategoryUrl: '',
      getDailyReportUrl: '',
      getMonthlyReportUrl: '',
      getWeeklyReportUrl: '',
      chartModes: {
        type: Array
      },
      maxSelectDefault: {
        default: 20
      },
      isCategory: {
        default: false
      },
      isKeyword: {
        default: false
      }
    },
    data() {
      return {
        labelPosition: 'left',
        maxSelect: this.maxSelectDefault,
        //  即使搜索
        skuSearch: '',
        //  请求搜索


        dialogKeywordSelectShow: false,

        dialogSkuSelectShow: false,
        totalSelectSkuItems: '',

        dialogCategorySelectShow: false,
        CategoryListTableInit: true,
        chartSelected: ["chart_daily", "chart_monthly", "chart_weekly"],

        //  sku 用的
        skuListTable: [],

        //  选择临时表
        skuListSelectedTemp: [],

        //Category
        categoryListSelectedTemp: [],

        //keyword
        keywordListSelectedTemp: [],

        categoryListTableCurrentPage: 1,
        categoryListTableTotalPage: 1,
        categoryListTablePageSize: Configs.system.query.pageSize + 0,
        categoryListTableLoading: false,

        filterMethod(query, item) {
          return item.pinyin.indexOf(query) > -1;
        },
        dateSelected: [
          Moment().subtract(1, 'years').format('YYYY-MM-DD'), Moment().format('YYYY-MM-DD')
        ]
      }
    },
    methods: {

      // dialogCategorySelectSubmitHandle: function () {
      //   console.log('dialogCategorySelectSubmitHandle');
        // let vm = this;
        // if (vm.totalSelectSkuItems.length > 20) {
        //   vm.$message.warning('选择的SKU超过20个');
        //   return false;
        // }
        // vm.skuSearchWord = '';
        // vm.skuListTableCurrentPage = 1;
        // // vm.skuListData = [...vm.totalSelectSkuItems];
        // vm.$store.dispatch('updateSkuSelectedListData', [...vm.totalSelectSkuItems]);
        // vm.skuListSelectedTemp = [];
        // vm.dialogSkuSelectShow = false;
      // },


      getRemoteDataChartHandle: function () {
        let form = {
          skuSelected: this.skuListSelected,
          keywordSelected:this.keywordListSelected,
          categorySelected:this.categoryListSelected,
          dateSelected: this.dateSelected,
          chartSelected: this.chartSelected,
        };
        // console.log(form);
        this.$emit('listenFilterSubmit', form)
      },

      deleteSkuSelectRow: function (row) {
        console.log(row);
        let temp = [...this.skuListSelected];
        temp.splice(row.$index, 1);
        this.$store.dispatch('updateSkuSelectedListData', temp)
        // this.skuListData.splice(row.$index, 1);
        this.totalSelectSkuItems = temp;
      },

      deleteKeywordSelectRow: function (row) {
        console.log(row);
        let temp = [...this.keywordListSelected];
        temp.splice(row.$index, 1);
        this.$store.dispatch('updateKeywordSelectedListData', temp);
        this.totalSelectKeywordItems = temp;
      },
      deleteCategorySelectRow: function (row) {
        console.log(row);
        let temp = [...this.categoryListSelected];
        temp.splice(row.$index, 1);
        this.$store.dispatch('updateCategorySelectedListData', temp);
        this.totalSelectCategoryItems = temp;
      },
      //  Category选择弹框初始化
      // dialogCategoryShowHandle: function () {
      //   console.log('dialogCategoryShowHandle');
      //   let vm = this;
      //   if (!!vm.CategoryListTableInit) {
      //     vm.dialogCategoryGetHandle(vm.categoryListTablePageFilter, vm.inputSearchWordFilter)
      //   }
      // },
      //  Line获取处理
      // dialogCategoryGetHandle: async function (form = {}, filter = []) {
      //   let vm = this;
      //   vm.dialogLineSelectShow = true;
      //   vm.lineListTableLoading = true;
      //   console.log(form);
      //   await ChartApi.fetchProductLineData(vm.getLineUrl, form, filter).then(response => {
      //     // vm.skuListTable = [...response.data];
      //     vm.$store.dispatch('updateLineListData', response.data);
      //     if (response.tp < 1) {
      //       // vm.skuListTable = [];
      //       vm.$store.dispatch('updateLineListData', []);
      //     }
      //     vm.lineListTableTotalPage = response.tp;
      //     vm.lineListTableLoading = false;
      //   }).catch(err => {
      //     vm.$message.error(err.message || vm.$i18n.t('操作失败'));
      //     vm.lineListTableLoading = false;
      //   });
      // },
      dialogSubmitCallBack() {
        let vm = this;
        // vm.totalSelectSkuItems = 2;
        console.log('dialogSubmitCallBack')
      },

      onShowProductDialogChange(val) {
        this.dialogSkuSelectShow = val;
      },
      onShowCategoryDialogChange(val) {
        this.dialogCategorySelectShow = val;
      },
      onShowKeywordDialogChange(val) {
        console.log(val);
        this.dialogKeywordSelectShow = val;
      }
    },
    computed: {
      skuListSelected: vm => vm.$store.getters.getFilterSkuSelectData,
      skuListData: vm => vm.$store.getters.getFilterSkuData,
      categoryListSelected: vm => vm.$store.getters.getFilterCategorySelectData,
      keywordListSelected: vm => vm.$store.getters.getFilterKeywordSelectData,

      //  chart表类型
      chartType: function () {
        let vm = this;
        vm.$store.dispatch('updatePageSeries', vm.$route.meta.series);
        return vm.$route.meta.series;
      },

      /**
       * 合计已选择内容,包括临时选择与已选择
       * @returns {*[]}
       */
      totalSelectCategoryItems: function () {
        let vm = this, _categoryList;

        _categoryList = vm.categoryListSelectedTemp.filter(item => {
          let _repeated;
          for (let index in vm.categoryListSelected) {
            _repeated = vm.categoryListSelected[index]['id'] == item['id'];
            if (_repeated == true) {
              break;
            } else {
              _repeated = false
            }
          }
          return !_repeated
        });

        console.log('去重选择列表', _categoryList);

        return _categoryList.concat(vm.categoryListSelected);
      },


      totalSelectKeywordItems: function () {
        let vm = this, _keywordList;

        _keywordList = vm.keywordListSelectedTemp.filter(item => {
          let _repeated;
          for (let index in vm.keywordListSelected) {
            _repeated = vm.keywordListSelected[index]['id'] == item['id'];
            if (_repeated == true) {
              break;
            } else {
              _repeated = false
            }
          }
          return !_repeated
        });

        console.log('去重选择列表', _keywordList);

        return _keywordList.concat(vm.keywordListSelected);
      },


      //  category 表分页 filter
      categoryListTablePageFilter: function () {
        console.log('test');
        let vm = this;
        return {
          page: vm.categoryListTableCurrentPage,
          size: vm.categoryListTablePageSize || Configs.system.query.pageSize
        };
      },

      route_cur_name: function () {
        return this.$route.name
      },

    },
    mounted() {
      console.log(this.chartType);
    }
  }
</script>

<style lang="stylus">
  .el-checkbox__label
    display inline-block !important

  .el-checkbox__input.is-checked + .el-checkbox__label
    color: #f3f3f3

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
    float: left !important;

  .el-checkbox-group
    margin: 0;
    padding: 0;
    float: left;
    width: 100%

</style>
