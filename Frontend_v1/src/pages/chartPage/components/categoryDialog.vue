
<template>
  <el-dialog title="Category 选择" :visible.sync="categorySelectShow" :modal="true" top="5vh" :append-to-body="true" @opened="dialogCategoryShowHandle"  :before-close="beforeClose">

    <el-row :gutter="24" style="height: 70vh;z-index:2048">
      <!--搜索栏-->
      <el-col :span="14">
        <el-input placeholder="输入Category进行搜索" v-model="categorySearchWord"
                  class="input-with-select"
                  size="mini">
          <el-button slot="append" type="primary" icon="el-icon-third  el-icon-search"
                     @click="categorySearchHandle"></el-button>
        </el-input>
      </el-col>
      <el-col :span="14">

        <el-table
          class="compact"
          ref="multipleTable"
          v-loading="categoryListTableLoading"
          :data="categoryListData"
          style="width: 100%;margin-top:.5em;min-height: 400px;max-height: 500px;"
          max-height="500"
          :select-on-indeterminate="false"
          :header-row-style="{height:'32px'}"
          @select="dialogCategoryListTableRowSelectedHandle"
          @row-click="dialogTableCheckSelect"
        >
          <el-table-column
            class="table-column"
            type="selection"
            @filter-method="dialogCategoryFilterFunc"
            width="55">
          </el-table-column>
          <el-table-column
            class="table-column"
            prop="id"
            label="Id">
          </el-table-column>
          <el-table-column
            class="table-column"
            prop="title"
            label="Category"
            width="150">
          </el-table-column>
          <el-table-column
            class="table-column"
            prop="code"
            label="Node Code"
            width="150">
          </el-table-column>
        </el-table>
        <el-row style="margin: 5px 0 0 0">
          <el-col align="center">
            <el-pagination
              small
              background
              layout="total, prev, pager, next, jumper"

              :page-count="categoryListTableTotalPage"
              :current-page.sync="categoryListTableCurrentPage"
              @current-change="categoryListTablePageChangeHandle">
            </el-pagination>
          </el-col>
        </el-row>

      </el-col>
      <el-col :span="10">
        <el-table
          class="compact"
          v-loading="categoryListTableLoading"
          :data="categoryListSelectedTemp"
          style="width: 100%;margin-top:.5em;min-height: 400px;max-height: 500px;"
          max-height="600">
          <el-table-column
            prop="title"
            label="Selected Category">
          </el-table-column>
          <el-table-column
            prop="code"
            label="Node Code">
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
    <div slot="footer" class="dialog-footer" align="center">
      <el-button @click="dialogCategorySelectCancelHandle" size="mini">取 消</el-button>
      <el-button type="primary" @click="dialogCategorySelectSubmitHandle" size="mini">确 定</el-button>
    </div>
  </el-dialog>
</template>

<script>
  import Configs from '@/lib/sysConfig';
  import ChartApi from '@/pages/chartPage/lib/chartApiHandler.js';

  export default {
        name: "categoryDialog",
        props: {
          propGetCategoryUrl: '',
          getDailyReportUrl: '',
          getMonthlyReportUrl: '',
          getWeeklyReportUrl: '',
          propCategorySelectShow: {
            default: false
          },
        },
      data() {
        return {
          propMaxSelect:20,
          categorySelectShow : false,
          //  选择临时表
          categoryListSelectedTemp: [],
          categorySearchWord:'',
          categoryListTableCurrentPage: 1,
          categoryListTableTotalPage: 1,
          categoryListTotalRecord: 0,
          categoryListTablePageSize: Configs.system.query.pageSize + 0,
          categoryListTableLoading: false,
          categoryListTableInit: true,
        }
      },
      methods:{
        // category选择弹框初始化
        dialogCategoryShowHandle: function () {
          let vm = this;
          if (!!vm.categoryListTableInit) {
            vm.dialogCategoryGetHandle(vm.categoryListTablePageFilter, vm.inputSearchWordFilter)
          }
          // vm.categoryListTableInit = false;
        },
        //  category获取处理
        dialogCategoryGetHandle: async function (form = {}, filter = []) {
          console.log('dialogCategoryGetHandle');
          let vm = this;
          vm.dialogSkuSelectShow = true;
          vm.categoryListTableLoading = true;
          await ChartApi.statamazoncategory(vm.propGetCategoryUrl, form, filter).then(response => {
            vm.$store.dispatch('updateCategoryListData', response.data);
            // vm.skuListTable = [...response.data];
            if (response.tp < 1) {
              // vm.skuListTable = [];
              vm.$store.dispatch('updateCategoryListData', [])
            }
            vm.categoryListTotalRecord = !!response.tr ? response.tr : 0;
            vm.categoryListTableTotalPage = response.tp;
            vm.categoryListTableLoading = false;
          }).catch(err => {
            vm.$message.error(err.message || vm.$i18n.t('操作失败'));
            vm.categoryListTableLoading = false;
          });
        },
        //  单击选中SKu row
        dialogTableCheckSelect: function (row, col, event) {
          console.log(row);
          let vm = this;
          vm.dialogCategoryListTableRowSelectedHandle(vm.$refs.multipleTable.selection, row)
        },

        //  勾选左侧sku table
        dialogCategoryListTableRowSelectedHandle(selection, row) {
          let vm = this;
          let rowExist = vm.categoryListSelectedTemp.filter(val => row.id == val.id);

          if (rowExist.length < 1) {
            console.log('没有重复就加入', rowExist.length < 1, rowExist);
            if (vm.categoryListSelectedTemp.length < vm.propMaxSelect) {
              let temp = vm.categoryListSelectedTemp;
              temp.push(row);
              vm.$refs.multipleTable.toggleRowSelection(row, true);
            } else {
              vm.$message.warning(`可选择的Category不可超过${vm.propMaxSelect}个`);
              vm.$refs.multipleTable.toggleRowSelection(row, false);
              return false;
            }
          } else {
            vm.categoryListSelectedTemp.splice(vm.categoryListSelectedTemp.indexOf(row), 1);
            vm.$refs.multipleTable.toggleRowSelection(row, false)

            console.log('重复了就去掉', rowExist.length > 0, rowExist);
          }
        },
        //  Category 弹出框 cancel
        dialogCategorySelectCancelHandle: function () {
          let vm = this;
          // vm.skuListSelected = [];
          vm.$store.dispatch('updateCategorySelectedListData', []);
          vm.categorySelectShow = false;
        },
        //  Category 弹出框 submit
        dialogCategorySelectSubmitHandle: function () {
          let vm = this;
          if (vm.totalSelectCategoryItems.length > 20) {
            vm.$message.warning('选择的SKU超过20个');
            return false;
          }
          vm.categorySearchWord = '';
          vm.categoryListTableCurrentPage = 1;
          // vm.skuListData = [...vm.totalSelectCategoryItems];
          vm.$store.dispatch('updateCategorySelectedListData', [...vm.totalSelectCategoryItems]);
          vm.categoryListSelectedTemp = [];
          vm.categorySelectShow = false;

          //将子totalSelectCategoryItems赋值到父totalSelectCategoryItems
          vm.$parent.totalSelectCategoryItems = vm.totalSelectCategoryItems;
        },

        /**
         * 关键字搜索
         * @param val
         * @returns {Promise<void>}
         */
        categorySearchHandle: async function (val) {
          let vm = this;
          vm.skuListTableCurrentPage = 1;
          vm.dialogCategoryGetHandle(vm.categoryListTablePageFilter, vm.inputSearchWordFilter)
        },

        dialogCategoryFilterFunc: function (value, row, col) {
          console.log(value, '123');
        },

        categoryListTablePageChangeHandle: function (cp) {
          console.log(cp);
          let vm = this;
          vm.skuListTableCurrentPage = cp;
          vm.dialogCategoryGetHandle(vm.categoryListTablePageFilter, vm.inputSearchWordFilter)
        },
      },
      computed :{
        categoryListSelected: vm => vm.$store.getters.getFilterCategorySelectData,
        categoryListData: vm => vm.$store.getters.getFilterCategoryData,

        chartType: function () {
          let vm = this;
          vm.$store.dispatch('updatePageSeries', vm.$route.meta.series);
          return vm.$route.meta.series;
        },
        //  远程关键字搜索filter
        inputSearchWordFilter: function () {
          let vm = this;
          let _queryParams = [];
          vm.skuListTableCurrentPage = 1;
          if (!!vm.categorySearchWord) {
            _queryParams.push([{"title-ilk": vm.categorySearchWord}, {"code-ilk": vm.categorySearchWord}]);
          }
          return _queryParams;
        },
        //  sku表分页filter
        categoryListTablePageFilter: function () {
          let vm = this;
          return {page: vm.skuListTableCurrentPage, size: vm.skuListTablePageSize || Configs.system.query.pageSize};
        },
        categoryListTableFiltered: function () {
          let vm = this;
          let res = !!vm.skuSearch ? vm.skuListTable.filter(item => item.sku.match(new RegExp(vm.skuSearch, 'i'))) : vm.skuListTable;
          return res;
        },

        totalSelectCategoryItems: function () {
          let vm = this, _skuList;

          _skuList = vm.categoryListSelectedTemp.filter(item => {
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

          console.log('去重选择列表', _skuList);

          return _skuList.concat(vm.categoryListSelected);
        },

        beforeClose: function(){
          this.$emit('closeMe', this.categorySelectShow)
        }
      },
      watch: {
        propCategorySelectShow (val){
          this.categorySelectShow = val;//新增加的propCategorySelectShow，监变更并同步到productSelectShow
        }
      }
    }
</script>

<style scoped>

</style>
