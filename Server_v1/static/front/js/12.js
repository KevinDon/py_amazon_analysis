webpackJsonp([12],{Gqli:function(e,t){},cqkT:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var n=a("Xxa5"),i=a.n(n),s=a("exGp"),r=a.n(s),o=a("bQLH"),l=a("x2f6"),c=a("gUwQ"),d={name:"chartSkuCompositeReportChart",components:{sideFilter:function(){return a.e(1).then(a.bind(null,"LvtV"))}},data:function(){return{chartModes:[{label:"日统计表",name:"chart_daily"},{label:"月统计表",name:"chart_monthly"},{label:"周统计表",name:"chart_weekly"}],screenWidth:document.body.clientWidth,fullscreenLoading:!1,fixShow:!0,asideShow:!0,queryForm:[],dailyChart:null,monthlyChart:null,weeklyChart:null,chartData:[],chartSelected:["chart_daily","chart_monthly","chart_weekly"]}},mounted:function(){var e=this;e.dailyChart=c.init(document.getElementById("chartDaily"),"canvas","auto","auto"),window.onresize=function(){return window.screenWidth=document.body.clientWidth,void(e.screenWidth=window.screenWidth)}},methods:{asideToggleHandler:function(e){var t=this;console.log("切换侧栏"),t.asideShow=!!t.fixShow||e,setTimeout(function(){l.default.chartResizeHandle(t.dailyChart)},500)},filterSubmitHandle:function(){var e=r()(i.a.mark(function e(t){var a,n,s,r,c,d,h,u;return i.a.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:if(a=this,n=[],t.skuSelected.length>0&&(s=[],t.skuSelected.forEach(function(e){void 0!=e&&s.push({"sku-eq":e.sku})}),n.push(s)),r=void 0,c=void 0,r=t.dateSelected[0],c=t.dateSelected[1],!(t.chartSelected.length>0)){e.next=26;break}if(a.chartSelected=t.chartSelected,!a.showDailyChart){e.next=14;break}return(d=[].concat(n)).push([{"dy-gte-and":r}]),d.push([{"dy-lte-and":c}]),e.next=14,o.default.statamazonskutotalitemsday("/v1/statamazonskureviewrankday/",{},d).then(function(e){a.daliyChartOptions=l.default.skuDailyChangHandle(a.dailyChart,e.data,a)});case 14:if(!a.showMonthlyChart){e.next=20;break}return(h=[].concat(n)).push([{"first_day-gte-and":r}]),h.push([{"last_day-lte-and":c}]),e.next=20,o.default.statamazonskutotalitemsmonth("/v1/statamazonskureviewrankmonth/",{},h).then(function(e){a.monthlyChartOptions=l.default.skuMonthlyChangeHandle(a.monthlyChart,e.data,a)});case 20:if(!a.showWeeklyChart){e.next=26;break}return(u=[].concat(n)).push([{"first_day-gte-and":r}]),u.push([{"last_day-lte-and":c}]),e.next=26,o.default.statamazonskutotalitemsweek("/v1/statamazonskureviewrankweek/",{},u).then(function(e){a.weeklyChartOptions=l.default.skuWeeklyChangeHandle(a.weeklyChart,e.data,a)});case 26:case"end":return e.stop()}},e,this)}));return function(t){return e.apply(this,arguments)}}(),filterSubmit:function(){var e=r()(i.a.mark(function e(t){var a;return i.a.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return(a=this).fullscreenLoading=!0,e.next=4,a.filterSubmitHandle(t).then(function(e){a.fullscreenLoading=!1,a.$message.success(a.$i18n.t("message.success"))}).catch(function(e){a.fullscreenLoading=!1,a.$message.error(e)});case 4:case"end":return e.stop()}},e,this)}));return function(t){return e.apply(this,arguments)}}(),chartResizeHandle:function(){}},computed:{showDailyChart:function(){return this.chartSelected.indexOf("chart_daily")>=0}},watch:{screenWidth:function(e){if(!this.timer){this.screenWidth=e,this.timer=!0;var t=this;setTimeout(function(){console.log(t.screenWidth),l.default.chartResizeHandle(t.dailyChart),t.timer=!1},500)}}}},h={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("el-container",[a("div",{staticClass:"side-box mark el-icon-d-arrow-right",class:e.asideShow||e.fixShow?"hide":"show",on:{mouseover:function(t){return e.asideToggleHandler(!e.asideShow)}}}),e._v(" "),a("el-aside",{staticClass:"aside",class:e.asideShow?"aside-show":"aside-hide",staticStyle:{background:"rgb(48, 65, 86)",float:"left",position:"fixed",height:"100%",bottom:"0",left:"0",right:"0","z-index":"99"},nativeOn:{mouseleave:function(t){return e.asideToggleHandler(!1)}}},[a("div",{staticClass:"aside-toggle-btn"},[a("el-button",{staticClass:"el-icon-third el-icon-ping",class:e.fixShow?"fix":"nofix",staticStyle:{border:"none",padding:"5px",margin:"0 5px 0 0"},on:{click:function(t){e.fixShow=!e.fixShow}}})],1),e._v(" "),a("side-filter",{directives:[{name:"loading",rawName:"v-loading.fullscreen.lock",value:e.fullscreenLoading,expression:"fullscreenLoading",modifiers:{fullscreen:!0,lock:!0}}],attrs:{chartModes:e.chartModes,getSkuUrl:"/v1/statamazonsku/"},on:{listenFilterSubmit:e.filterSubmit}})],1),e._v(" "),a("el-container",[a("el-main",{style:e.fixShow?"margin :0 0 0 270px;":"",attrs:{id:"main-box"}},[a("h1",[e._v("Report List")]),e._v(" "),a("div",{directives:[{name:"show",rawName:"v-show.sync",value:e.showDailyChart,expression:"showDailyChart",modifiers:{sync:!0}}],staticClass:"chart-box"},[a("div",{staticClass:"chart",attrs:{id:"chartDaily"}})])])],1)],1)},staticRenderFns:[]};var u=a("VU/8")(d,h,!1,function(e){a("Gqli")},"data-v-8040a606",null);t.default=u.exports}});
//# sourceMappingURL=12.js.map