import Vue from "vue"
import Vuex from "vuex"
import Settings from "@/settings"

Vue.use(Vuex);

const modules = {};

//  根据 Setting 中的 autoLoad / store 中的数据进行store加载
try {
  if (Settings.autoLoad.store.length > 0) {
    Settings.autoLoad.store.map(item => {
      console.log(item);
      modules[item['name']] = item['path']
    })
  }
} catch (e) {
  console.log(e);
}

console.log(modules);


const Store = new Vuex.Store({
  modules: modules,
  strict: process.env.NODE_ENV !== "production",
})

export default Store
