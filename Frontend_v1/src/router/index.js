import Vue from 'vue'
import Router from 'vue-router'
import PageHome from '@/components/PageHome'
import ChartRouter from '@/pages/chartPage/router.js'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/home',
      name: 'PageHome',
      component: PageHome
    },
    ChartRouter
  ]
});

// router.beforeEach((to, from, next) => {
//   /* 路由发生变化修改页面title */
//   if (to.meta.title) {
//     console.log(to);
//   }
//
//   next()
// });
//
// router.afterEach((to)=>{
//   window.$vm.store.dispatch('updateCurRouter', to);
// })

export default router
