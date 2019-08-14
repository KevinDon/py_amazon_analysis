import httpAxios from '@/lib/axiosRequest'
import sysConfigs from '@/lib/sysConfig'

/**
 * api 分页对象
 * @type {function(*=, *=): {size: (*|string), page: (*|string)}}
 */
let _pager = (page, size) => {
  return {
    page: page || sysConfigs.system.query.page || '1',
    size: size || sysConfigs.system.query.pageSize || '500',
  }
};

/**
 * api 排序对象
 * @type {function(Array): *[]}
 */
let _order = (sort = []) => {
  return [...sort]
};

/**
 *
 * @param filter
 * @returns {...*[]}
 */
let _filter = (filter = []) => {
  return [...filter]
}

const apihandler = {
  /**
   * 格式化url
   * @param url
   * @param form
   * @returns {*}
   * @private
   */
  _init_page_url(url, form = {page: 1, size: 500}) {
    if (!!form['page']) {
      return `${url}?page=${form['page'] || 1}` + (!!form['size'] ? `&size=${form['size']}` : '')
    } else {
      return url;
    }
  },

  /**
   * apiRequest底层
   * @param url
   * @param form
   * @param filter
   * @param order
   * @param size
   * @param page
   * @returns {Promise<T>}
   */
  async apiRequest(url, form = {}, filter = [], order = [], page, size) {
    let apiUrl = this._init_page_url(url, form);
    console.log('发起交互:' + url, form, filter);
    return await httpAxios.post(apiUrl, {
      pager: _pager(page, size),
      order: _order(order),
      filter: _filter(filter),
    }).then(res => {
      console.log('交互完毕', res);
      if (res.status != 200) {
        throw res.msg
      }
      return res
    }).catch(error => {
      throw error;
    })
  },

  async statamazonskutotalitemsday(url = '', form = {}, filter = []) {
    return await httpAxios.post(url || '/v1/statamazonskutotalitemsday/', {
        "pager": {"size": 20000, "page": 1}
        , "order": ["dy", "sku"]
        , "filter": filter
      }
    ).then(res => {
      if (res.status != 200) {
        throw res.msg
      }
      return res
    }).catch(function (error) {
      throw error;
    });
  },

  async statamazonskutotalitemsmonth(url = '', form = {}, filter = []) {
    return await httpAxios.post(url || '/v1/statamazonskutotalitemsmonth/', {
        "pager": {"size": 10000, "page": 1}
        , "order": ["yr", "mo", "sku"]
        , "filter": filter
      }
    ).then(res => {
      if (res.status != 200) {
        throw res.msg
      }
      return res
    }).catch(function (error) {
      throw error;
    });
  },

  async statamazonskutotalitemsweek(url = '', form = {}, filter = []) {
    return await httpAxios.post(url || '/v1/statamazonskutotalitemsweek/', {
        "pager": {"size": 10000, "page": 1}
        , "order": ["yr", "wk", "sku"]
        , "filter": filter
      }
    ).then(res => {
      if (res.status != 200) {
        throw res.msg
      }
      return res
    }).catch(function (error) {
      throw error;
    });
  },

  /**
   * 获取Sku list
   * @param url 交互api
   * @param form 传参
   * @param filter 过滤器
   * @returns {Promise<T>}
   */
  async statamazonsku(url = '', form = {}, filter = []) {
    let apiUrl = this._init_page_url(url || '/v2/statamazonsku/', form);
    console.log(url, form, filter);

    return await httpAxios.post(apiUrl, {
        "pager": {"size": sysConfigs.system.query.pageSize, "page": form['page'] || 1}
        , "order": ["sku", "asin"],
        "filter": filter
      }
    ).then(res => {
      if (res.status != 200) {
        throw res.msg
      }
      return res
    }).catch(function (error) {
      throw error;
    });
  },


  /******  line api   ******/

  /**
   * 获取产品线
   * @param url
   * @param form 包括page,size和order数组
   * @param filter
   * @returns {Promise<T>}
   */
  async fetchProductLineData(url = '', form, filter = []) {
    console.log(form);
    return await apihandler.apiRequest(url, form, filter, form['order'], form['page'], form['size'],)
  },

  /**
   * 获取产品线日数据
   * @param url
   * @param form
   * @param filter
   * @returns {Promise<T>}
   */
  async fetchstatamazonlinedaily(url = '', form, filter = []) {
    return await apihandler.apiRequest(url, form, filter, form['order'], form['page'], form['size'])
  },
  async fetchstatamazonlinemonthly(url = '', form, filter = []) {
    return await apihandler.apiRequest(url, form, filter, form['order'], form['page'], form['size'])
  },
  async fetchstatamazonlineweekly(url = '', form, filter = []) {
    return await apihandler.apiRequest(url, form, filter, form['order'], form['page'], form['size'])
  },
  async statamazonkeyword(url = '', form, filter = []) {
    return await apihandler.apiRequest(url, form, filter, form['order'], form['page'], form['size'])
  },

  async statamazoncategory(url = '', form, filter = []) {
    return await apihandler.apiRequest(url, form, filter, form['order'], form['page'], form['size'])
  }


}
export default apihandler
