// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'element-ui/lib/theme-chalk/index.css';
import './assets/icon/iconfont.css';

import Vue from 'vue'
import App from './App'
import Vuex from 'vuex'
import ElementUI from 'element-ui'
import router from './router'
import VueCookies from 'vue-cookies'
import Axios from 'axios'
//  element 多语言
// import locale from 'element-ui/lib/locale/lang/en'
//  vue 多语言
import i18n from '@/lib/i18nLang'
//  引用VUEX数据仓集合
import store from '@/store/index.js'
//  引用VUEX-ROUTER同步类
import {sync} from 'vuex-router-sync'
// import Mock from 'mockjs'
// import Echart from 'echarts'
Vue.use(Vuex);
Vue.use(ElementUI);
Vue.use(VueCookies);
console.log('main')
// 根据路由设置标题
router.beforeEach((to, from, next) => {
  if(to.meta.title) {
    document.title = to.meta.title
  }
  next();
});

Vue.prototype.$http = Axios;
Vue.config.productionTip = false;
//  路由对象挂载到数据仓
sync(store, router);
/* eslint-disable no-new */
//  window全局挂在vue实例
window.$vm = new Vue({
  el: '#app',
  store,
  i18n,
  router,
  components: {App},
  template: '<App/>'
});


