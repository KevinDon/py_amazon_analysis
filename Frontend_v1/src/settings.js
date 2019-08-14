// config总入口

import Configs from "@/lib/sysConfig"
//  全局配置仓
import StoreGlobal from "@/store/globalStore"
//  Chart页面配置仓
import StoreChartPage from "@/pages/chartPage/charStore.js"

const Settings = {
  config: Configs,
  autoLoad: {
    store: [
      {
        name: 'global',
        path: StoreGlobal,
      },
      {
        name: 'chartPage',
        path: StoreChartPage,
      },
    ]
  }
};

export default Settings
