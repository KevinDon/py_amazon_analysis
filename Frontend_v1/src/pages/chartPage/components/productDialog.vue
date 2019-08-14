<template>
  <el-dialog title="SKU 选择" v-if="chartType == 'sku'" :visible.sync="dialogSkuSelectShow" :modal="true" top="5vh"
             :append-to-body="true"
             :close-on-click-modal="false"
             @opened="dialogSkuShowHandle"
            :before-close="beforeClose">
    <el-row :gutter="24" style="height: 70vh;z-index:2048">
      <!--搜索栏-->
      <el-col :span="14">
        <el-input placeholder="输入SKU或ASIN进行搜索" v-model="skuSearchWord"
                  class="input-with-select"
                  size="mini">
          <el-button slot="append" type="primary" icon="el-icon-third  el-icon-search"
                     @click="skuSearchHandle"></el-button>
        </el-input>
      </el-col>
      <el-col :span="14">

        <el-table
          class="compact"
          ref="multipleTable"
          v-loading="skuListTableLoading"
          :data="skuListData"
          style="width: 100%;margin-top:.5em;min-height: 400px;max-height: 500px;"
          max-height="500"
          :select-on-indeterminate="false"
          :header-row-style="{height:'32px'}"
          @select="dialogSkuListTableRowSelectedHandle"
          @row-click="dialogTableCheckSelect"
        >
          <el-table-column
            class="table-column"
            type="selection"
            @filter-method="dialogSkuFilterFunc"
            width="55">
          </el-table-column>
          <el-table-column
            class="table-column"
            prop="sku"
            label="SKU">
          </el-table-column>
          <el-table-column
            class="table-column"
            prop="asin"
            label="ASIN"
            width="150">
          </el-table-column>
        </el-table>
        <el-row style="margin: 5px 0 0 0">
          <el-col align="center">
            <el-pagination
              small
              background
              layout="total, prev, pager, next, jumper"

              :page-count="skuListTableTotalPage"
              :current-page.sync="skuListTableCurrentPage"
              @current-change="skuListTablePageChangeHandle">
            </el-pagination>
          </el-col>
        </el-row>

      </el-col>
      <el-col :span="10">
        <el-table
          class="compact"
          v-loading="skuListTableLoading"
          :data="skuListSelectedTemp"
          style="width: 100%;margin-top:.5em;min-height: 400px;max-height: 500px;"
          max-height="600">
          <el-table-column
            prop="sku"
            label="Selected SKU">
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
    <div slot="footer" class="dialog-footer" align="center">
      <el-button @click="dialogSkuSelectCancelHandle" size="mini">取 消</el-button>
      <el-button type="primary" @click="dialogSkuSelectSubmitHandle" size="mini">确 定</el-button>
    </div>
  </el-dialog>

</template>

<script>
  import Configs from '@/lib/sysConfig';
  import ChartApi from '@/pages/chartPage/lib/chartApiHandler.js';

  export default {
        name: "productDialog",
        props: {
          propGetSkuUrl: '',
          getDailyReportUrl: '',
          getMonthlyReportUrl: '',
          getWeeklyReportUrl: '',
          propProductSelectShow : {
            default :false
          },
          propMaxSelect: {
            default: 20
          }
        },
        data() {
          return {
             dialogSkuSelectShow : false,
            //  选择临时表
            skuListSelectedTemp: [],
            skuSearchWord:'',
            skuListTableCurrentPage: 1,
            skuListTableTotalPage: 1,
            skuListTotalRecord: 0,
            skuListTablePageSize: Configs.system.query.pageSize + 0,
            skuListTableLoading: false,
            skuListTableInit: true,
          }
        },
        methods:{
          //  Sku选择弹框初始化
          dialogSkuShowHandle: function () {
            let vm = this;
            if (!!vm.skuListTableInit) {
              vm.dialogSkuGetHandle(vm.skuListTablePageFilter, vm.inputSearchWordFilter)
            }
            // vm.skuListTableInit = false;
          },
          //  Sku获取处理
          dialogSkuGetHandle: async function (form = {}, filter = []) {
            console.log('dialogSkuGetHandle');
            let vm = this;
            vm.dialogSkuSelectShow = true;
            vm.skuListTableLoading = true;
            await ChartApi.statamazonsku(vm.propGetSkuUrl, form, filter).then(response => {
              vm.$store.dispatch('updateSkuListData', response.data);
              // vm.skuListTable = [...response.data];
              if (response.tp < 1) {
                // vm.skuListTable = [];
                vm.$store.dispatch('updateSkuListData', [])
              }
              vm.skuListTotalRecord = !!response.tr ? response.tr : 0;
              vm.skuListTableTotalPage = response.tp;
              vm.skuListTableLoading = false;
            }).catch(err => {
              vm.$message.error(err.message || vm.$i18n.t('操作失败'));
              vm.skuListTableLoading = false;
            });
          },
          //  单击选中SKu row
          dialogTableCheckSelect: function (row, col, event) {
            console.log(row);
            let vm = this;
            vm.dialogSkuListTableRowSelectedHandle(vm.$refs.multipleTable.selection, row)
          },
          //  Sku List Table 选择区域变更
          dialogSkuListTableSelectionChange(val) {
            let vm = this;
            console.log('补勾选sku');
            //  根据已选择的sku勾选左侧sku
            vm.totalSelectSkuItems.forEach(item => {
              for (let index in vm.skuListTable) {
                let row = vm.skuListTable[index];
                console.log(row);
                if (item.id == row.id) {
                  vm.$refs.multipleTable.toggleRowSelection(item, true)
                  vm.$refs.multipleTable.toggleRowSelection(row, true)
                }
              }
            })
          },
          //  勾选左侧sku table
          dialogSkuListTableRowSelectedHandle(selection, row) {
            let vm = this;
            let rowExist = vm.skuListSelectedTemp.filter(val => row.id == val.id);

            if (rowExist.length < 1) {
              console.log('没有重复就加入', rowExist.length < 1, rowExist);
              if (vm.skuListSelectedTemp.length < vm.propMaxSelect) {
                let temp = vm.skuListSelectedTemp;
                temp.push(row);
                vm.$refs.multipleTable.toggleRowSelection(row, true);
              } else {
                vm.$message.warning(`可选择的SKU不可超过${vm.propMaxSelect}个`);
                vm.$refs.multipleTable.toggleRowSelection(row, false);
                return false;
              }
            } else {
              vm.skuListSelectedTemp.splice(vm.skuListSelectedTemp.indexOf(row), 1);
              vm.$refs.multipleTable.toggleRowSelection(row, false)

              console.log('重复了就去掉', rowExist.length > 0, rowExist);
            }
          },
          //  sku 弹出框 cancel
          dialogSkuSelectCancelHandle: function () {
              console.log('2');
              let vm = this;
              // vm.skuListSelected = [];
              vm.$store.dispatch('updateSkuSelectedListData', []);
              vm.dialogSkuSelectShow = false;
          },

          //  sku 弹出框 submit
          dialogSkuSelectSubmitHandle: function () {
            let vm = this;
            if (vm.totalSelectSkuItems.length > 20) {
              vm.$message.warning('选择的SKU超过20个');
              return false;
            }
            vm.skuSearchWord = '';
            vm.skuListTableCurrentPage = 1;
            // vm.skuListData = [...vm.totalSelectSkuItems];
            vm.$store.dispatch('updateSkuSelectedListData', [...vm.totalSelectSkuItems]);
            vm.skuListSelectedTemp = [];
            vm.dialogSkuSelectShow = false;

            //将子totalSelectSkuItems赋值到父totalSelectSkuItems
            vm.$parent.totalSelectSkuItems = vm.totalSelectSkuItems;
          },

          /**
           * 关键字搜索
           * @param val
           * @returns {Promise<void>}
           */
          skuSearchHandle: async function (val) {
            let vm = this;
            vm.skuListTableCurrentPage = 1;
            vm.dialogSkuGetHandle(vm.skuListTablePageFilter, vm.inputSearchWordFilter)
          },

          dialogSkuFilterFunc: function (value, row, col) {
            console.log(value, '123');
          },

          skuListTablePageChangeHandle: function (cp) {
            console.log(cp);
            let vm = this;
            vm.skuListTableCurrentPage = cp;
            vm.dialogSkuGetHandle(vm.skuListTablePageFilter, vm.inputSearchWordFilter)
          },
        },
        computed :{
          skuListSelected: vm => vm.$store.getters.getFilterSkuSelectData,
          skuListData: vm => vm.$store.getters.getFilterSkuData,

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
            if (!!vm.skuSearchWord) {
              _queryParams.push([{"sku-ilk": vm.skuSearchWord}, {"asin-ilk": vm.skuSearchWord}]);
            }
            return _queryParams;
          },
          //  sku表分页filter
          skuListTablePageFilter: function () {
            let vm = this;
            return {page: vm.skuListTableCurrentPage, size: vm.skuListTablePageSize || Configs.system.query.pageSize};
          },
          skuListTableFiltered: function () {
            let vm = this;
            let res = !!vm.skuSearch ? vm.skuListTable.filter(item => item.sku.match(new RegExp(vm.skuSearch, 'i'))) : vm.skuListTable;
            return res;
          },

          totalSelectSkuItems: function () {
            let vm = this, _skuList;

            _skuList = vm.skuListSelectedTemp.filter(item => {
              let _repeated;
              for (let index in vm.skuListSelected) {
                _repeated = vm.skuListSelected[index]['id'] == item['id'];
                if (_repeated == true) {
                  break;
                } else {
                  _repeated = false
                }
              }
              return !_repeated
            });

            console.log('去重选择列表', _skuList);

            return _skuList.concat(vm.skuListSelected);
          },

          beforeClose: function(){
            this.$emit('closeMe', this.dialogSkuSelectShow)
          }
        },
        watch: {
          propProductSelectShow (val){
            this.dialogSkuSelectShow = val;//新增加的propProductSelectShow，监变更并同步到dialogSkuSelectShow
          }
        }
    }
</script>

<style scoped>

</style>
