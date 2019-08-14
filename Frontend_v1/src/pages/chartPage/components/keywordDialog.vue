<template>
  <el-dialog title="Keyword 选择"  :visible.sync="keywordSelectShow" :modal="true" top="5vh"
             :append-to-body="true"
             :close-on-click-modal="false"
             @opened="dialogKeywordShowHandle"
             :before-close="beforeClose">
    <el-row :gutter="24" style="height: 70vh;z-index:2048">
      <!--搜索栏-->
      <el-col :span="14">
        <el-input placeholder="输入Keyword进行搜索" v-model="keywordSearchWord"
                  class="input-with-select"
                  size="mini">
          <el-button slot="append" type="primary" icon="el-icon-third  el-icon-search"
                     @click="keywordSearchHandle"></el-button>
        </el-input>
      </el-col>
      <el-col :span="14">

        <el-table
          class="compact"
          ref="multipleTable"
          v-loading="keywordListTableLoading"
          :data="keywordListData"
          style="width: 100%;margin-top:.5em;min-height: 400px;max-height: 500px;"
          max-height="500"
          :select-on-indeterminate="false"
          :header-row-style="{height:'32px'}"
          @select="dialogKeywordListTableRowSelectedHandle"
          @row-click="dialogTableCheckSelect"
        >
          <el-table-column
            class="table-column"
            type="selection"
            @filter-method="dialogKeywordFilterFunc"
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
            label="Title">
          </el-table-column>

        </el-table>
        <el-row style="margin: 5px 0 0 0">
          <el-col align="center">
            <el-pagination
              small
              background
              layout="total, prev, pager, next, jumper"

              :page-count="keywordListTableTotalPage"
              :current-page.sync="keywordListTableCurrentPage"
              @current-change="keywordListTablePageChangeHandle">
            </el-pagination>
          </el-col>
        </el-row>

      </el-col>
      <el-col :span="10">
        <el-table
          class="compact"
          v-loading="keywordListTableLoading"
          :data="keywordListSelectedTemp"
          style="width: 100%;margin-top:.5em;min-height: 400px;max-height: 500px;"
          max-height="600">
          <el-table-column
            prop="title"
            label="Selected Keyword">
          </el-table-column>

        </el-table>
      </el-col>
    </el-row>
    <div slot="footer" class="dialog-footer" align="center">
      <el-button @click="dialogKeywordSelectCancelHandle" size="mini">取 消</el-button>
      <el-button type="primary" @click="dialogKeywordSelectSubmitHandle" size="mini">确 定</el-button>
    </div>
  </el-dialog>

</template>

<script>
  import Configs from '@/lib/sysConfig';
  import ChartApi from '@/pages/chartPage/lib/chartApiHandler.js';

  export default {
      name: "keywordDialog",
      props: {
        propGetKeywordUrl: '',
        getDailyReportUrl: '',
        getMonthlyReportUrl: '',
        getWeeklyReportUrl: '',
        propKeywordSelectShow : {
          default :false
        },
        propMaxSelect: {
          default: 20
        }
      },
      data() {
        return {
          keywordSelectShow : false,
          //  选择临时表
          keywordListSelectedTemp: [],
          keywordSearchWord:'',
          keywordListTableCurrentPage: 1,
          keywordListTableTotalPage: 1,
          keywordListTotalRecord: 0,
          keywordListTablePageSize: Configs.system.query.pageSize + 0,
          keywordListTableLoading: false,
          keywordListTableInit: true,
        }
      },
      methods:{
        //  Keyword选择弹框初始化
        dialogKeywordShowHandle: function () {
          console.log('test');
          let vm = this;
          if (!!vm.keywordListTableInit) {
            vm.dialogKeywordGetHandle(vm.keywordListTablePageFilter, vm.inputSearchWordFilter)
          }
          // vm.keywordListTableInit = false;
        },
        //  Keyword获取处理
        dialogKeywordGetHandle: async function (form = {}, filter = []) {
          console.log('dialogKeywordGetHandle');
          let vm = this;
          vm.dialogKeywordSelectShow = true;
          vm.keywordListTableLoading = true;
          await ChartApi.statamazonkeyword(vm.propGetKeywordUrl, form, filter).then(response => {
            vm.$store.dispatch('updateKeywordListData', response.data);
            // vm.keywordListTable = [...response.data];
            if (response.tp < 1) {
              // vm.keywordListTable = [];
              vm.$store.dispatch('updateKeywordListData', [])
            }
            vm.keywordListTotalRecord = !!response.tr ? response.tr : 0;
            vm.keywordListTableTotalPage = response.tp;
            vm.keywordListTableLoading = false;
          }).catch(err => {
            vm.$message.error(err.message || vm.$i18n.t('操作失败'));
            vm.keywordListTableLoading = false;
          });
        },
        //  单击选中SKu row
        dialogTableCheckSelect: function (row, col, event) {
          console.log(row);
          let vm = this;
          vm.dialogKeywordListTableRowSelectedHandle(vm.$refs.multipleTable.selection, row)
        },
        //  Keyword List Table 选择区域变更
        dialogKeywordListTableSelectionChange(val) {
          let vm = this;
          console.log('补勾选keyword');
          //  根据已选择的keyword勾选左侧keyword
          vm.totalSelectKeywordItems.forEach(item => {
            for (let index in vm.keywordListTable) {
              let row = vm.keywordListTable[index];
              console.log(row);
              if (item.id == row.id) {
                vm.$refs.multipleTable.toggleRowSelection(item, true)
                vm.$refs.multipleTable.toggleRowSelection(row, true)
              }
            }
          })
        },
        //  勾选左侧keyword table
        dialogKeywordListTableRowSelectedHandle(selection, row) {
          let vm = this;
          let rowExist = vm.keywordListSelectedTemp.filter(val => row.id == val.id);

          if (rowExist.length < 1) {
            console.log('没有重复就加入', rowExist.length < 1, rowExist);
            if (vm.keywordListSelectedTemp.length < vm.propMaxSelect) {
              let temp = vm.keywordListSelectedTemp;
              temp.push(row);
              vm.$refs.multipleTable.toggleRowSelection(row, true);
            } else {
              vm.$message.warning(`可选择的SKU不可超过${vm.propMaxSelect}个`);
              vm.$refs.multipleTable.toggleRowSelection(row, false);
              return false;
            }
          } else {
            vm.keywordListSelectedTemp.splice(vm.keywordListSelectedTemp.indexOf(row), 1);
            vm.$refs.multipleTable.toggleRowSelection(row, false)

            console.log('重复了就去掉', rowExist.length > 0, rowExist);
          }
        },
        //  keyword 弹出框 cancel
        dialogKeywordSelectCancelHandle: function () {
          let vm = this;
          // vm.keywordListSelected = [];
          vm.$store.dispatch('updateKeywordSelectedListData', []);
          vm.dialogKeywordSelectShow = false;
        },
        //  keyword 弹出框 submit
        dialogKeywordSelectSubmitHandle: function () {
          let vm = this;
          if (vm.totalSelectKeywordItems.length > 20) {
            vm.$message.warning('选择的SKU超过20个');
            return false;
          }
          vm.keywordSearchWord = '';
          vm.keywordListTableCurrentPage = 1;
          // vm.keywordListData = [...vm.totalSelectKeywordItems];
          vm.$store.dispatch('updateKeywordSelectedListData', [...vm.totalSelectKeywordItems]);
          vm.keywordListSelectedTemp = [];
          vm.keywordSelectShow = false;

          //将子totalSelectKeywordItems赋值到父totalSelectKeywordItems
          vm.$parent.totalSelectKeywordItems = vm.totalSelectKeywordItems;
        },

        /**
         * 关键字搜索
         * @param val
         * @returns {Promise<void>}
         */
        keywordSearchHandle: async function (val) {
          let vm = this;
          vm.keywordListTableCurrentPage = 1;
          vm.dialogKeywordGetHandle(vm.keywordListTablePageFilter, vm.inputSearchWordFilter)
        },

        dialogKeywordFilterFunc: function (value, row, col) {
          console.log(value, '123');
        },

        keywordListTablePageChangeHandle: function (cp) {
          console.log(cp);
          let vm = this;
          vm.keywordListTableCurrentPage = cp;
          vm.dialogKeywordGetHandle(vm.keywordListTablePageFilter, vm.inputSearchWordFilter)
        },
      },
      computed :{
        keywordListSelected: vm => vm.$store.getters.getFilterKeywordSelectData,
        keywordListData: vm => vm.$store.getters.getFilterKeywordData,

        chartType: function () {
          let vm = this;
          vm.$store.dispatch('updatePageSeries', vm.$route.meta.series);
          return vm.$route.meta.series;
        },
        //  远程关键字搜索filter
        inputSearchWordFilter: function () {
          let vm = this;
          let _queryParams = [];
          vm.keywordListTableCurrentPage = 1;
          if (!!vm.keywordSearchWord) {
            _queryParams.push([{"title-ilk": vm.keywordSearchWord}]);
          }
          return _queryParams;
        },
        //  keyword表分页filter
        keywordListTablePageFilter: function () {
          let vm = this;
          return {page: vm.keywordListTableCurrentPage, size: vm.keywordListTablePageSize || Configs.system.query.pageSize};
        },
        keywordListTableFiltered: function () {
          let vm = this;
          let res = !!vm.keywordSearch ? vm.keywordListTable.filter(item => item.keyword.match(new RegExp(vm.keywordSearch, 'i'))) : vm.keywordListTable;
          return res;
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

        beforeClose: function(){
          this.$emit('closeMe', this.keywordSelectShow)
        }
      },
      watch: {
        propKeywordSelectShow (val){
          this.keywordSelectShow = val;//新增加的propKeywordSelectShow，监变更并同步到keywordSelectShow
        }
      }
    }
</script>

<style scoped>

</style>
