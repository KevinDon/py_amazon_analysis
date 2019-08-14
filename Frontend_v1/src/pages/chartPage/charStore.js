const pageSeriesDefault = ['sku', 'product_line'];
const state = {
  //  图表系列
  pageSeries: null,
  //  产品线选择列表
  lineListData: [],
  //  产品线已选择列表
  lineSelectedListData: [],
  skuListData: [],
  skuSelectedListData: [],
  categoryListData:[],
  categorySelectedListData:[],
  keywordListData:[],
  keywordSelectedListData:[]

};

const getters = {
  getPageSeries: state => state.pageSeries,
  getFilterLineData: state => state.lineListData,
  getFilterSkuData:state=>state.skuListData,
  getFilterLineSelectData: state => state.lineSelectedListData,
  getFilterSkuSelectData: state => state.skuSelectedListData,
  getFilterCategoryData: state => state.categoryListData,
  getFilterCategorySelectData: state => state.categorySelectedListData,
  getFilterKeywordSelectData: state => state.keywordSelectedListData,
  getFilterKeywordData:state=>state.keywordListData,
};



const mutations = {
  UPDATE_STATE: (state, keyVal) => {
    try {
      state[keyVal['key']] = keyVal['val'];
    } catch (e) {
      console.log('数据仓更新失败,查找不到当前数据路径' + keyVal['key']);
    }
  }
};

const actions = {
  updatePageSeries: (content, payload) => {
    content.commit('UPDATE_STATE',
      {
        key: 'pageSeries',
        val: payload
      }
    )
  },
  updateLineListData: (content, payload) => {
    content.commit('UPDATE_STATE',
      {
        key: 'lineListData',
        val: payload
      })
  },
  updateLineSelectedListData: (content, payload) => {
    content.commit('UPDATE_STATE',
      {
        key: 'lineSelectedListData',
        val: payload
      })
  },
  updateSkuListData: (content, payload) => {
    content.commit('UPDATE_STATE',
      {
        key: 'skuListData',
        val: payload
      })
  },
  updateSkuSelectedListData: (content, payload) => {
    content.commit('UPDATE_STATE', {
      key: 'skuSelectedListData',
      val: payload
    })
  },
  updateCategorySelectedListData: (content, payload) => {
    content.commit('UPDATE_STATE', {
      key: 'categorySelectedListData',
      val: payload
    })
  },
  updateKeywordListData:(content,payload)=>{
    content.commit('UPDATE_STATE', {
      key: 'keywordListData',
      val: payload
    })
  },
  updateKeywordSelectedListData:(content,payload)=>{
    content.commit('UPDATE_STATE',{
      key:'keywordSelectedListData',
      val:payload
    })
  },
  updateCategoryListData:(content,payload)=>{
    content.commit('UPDATE_STATE', {
      key: 'categoryListData',
      val: payload
    })
  },

};

const dislogShowStatus = {

};


/**
 * @name 图表数据仓
 */
export default {
  state,
  getters,
  mutations,
  actions,
};


