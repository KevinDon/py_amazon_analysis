import Configs from '@/lib/sysConfig'

let charPageRouter = {
  path: '/chart',
  name: 'chart router',
  component: () => import('./chartPageLayout'),
  children: [],
  beforeEnter: (to, from, next) => {
    console.log(to, charPageRouter.children);
    let routeExist = charPageRouter.children.filter(item => {
      return to.path == '/chart/' + item.path
    });
    console.log(routeExist);
    if (routeExist.length < 1) {
      next('/chart/' + charPageRouter.children[0]['path'])
    }
    // console.log(this, window.$vm);

    next()
  },
};

//  动态加载路由
for (let index in Configs.system.router.pages) {
  let item = Configs.system.router.pages[index];
  charPageRouter.children.push({
    path: item.path,
    name: item.name,
    meta: {...item, title:item.title},
    components: {
      chart: () => import('./' + item.component_name)
    }
  })
}
export default charPageRouter
