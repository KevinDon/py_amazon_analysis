webpackJsonp([8],{LU9U:function(e,t){},QVAg:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var i=n("Xxa5"),a=n.n(i),r=n("exGp"),s=n.n(r),c=n("bQLH"),l=n("x2f6"),o=n("gUwQ"),d={name:"chartLineBuyBoxPerChart",components:{sideFilter:function(){return n.e(2).then(n.bind(null,"x8HV"))}},data:function(){return{chartModes:[{label:"日统计表",name:"chart_daily"}],screenWidth:document.body.clientWidth,fullscreenLoading:!1,asideShow:!0,queryForm:[],dailyChart:null,monthlyChart:null,weeklyChart:null,chartData:[],chartSelected:["chart_daily","chart_monthly","chart_weekly"]}},mounted:function(){var e=this;e.dailyChart=o.init(document.getElementById("chartDaily"),"canvas","auto","auto"),window.onresize=function(){return window.screenWidth=document.body.clientWidth,void(e.screenWidth=window.screenWidth)}},methods:{asideToggleHandler:function(e){var t=this;console.log("切换侧栏"),t.asideShow=e,setTimeout(function(){l.default.chartResizeHandle(t.dailyChart)},500)},filterSubmitHandle:function(){var e=s()(a.a.mark(function e(t){var n,i,r,s,o,d;return a.a.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:if(n=this,i=[],t.itemSelected.length>0&&(r=[],t.itemSelected.forEach(function(e){void 0!=e&&r.push({"line_id-eq":e.id})}),i.push(r)),s=void 0,o=void 0,s=t.dateSelected[0],o=t.dateSelected[1],!(t.chartSelected.length>0)){e.next=14;break}if(n.chartSelected=t.chartSelected,!n.showDailyChart){e.next=14;break}return(d=[].concat(i)).push([{"dy-gte-and":s}]),d.push([{"dy-lte-and":o}]),e.next=14,c.default.fetchstatamazonlinedaily("/v1/statamazonlinebuyboxday/",{order:["dy","line_id"],size:5e5},d).then(function(e){console.log(e),n.daliyChartOptions=l.default.lineDailyChangHandle(n.dailyChart,e.data,n)}).catch(function(e){console.log(e)});case 14:case"end":return e.stop()}},e,this)}));return function(t){return e.apply(this,arguments)}}(),filterSubmit:function(){var e=s()(a.a.mark(function e(t){var n;return a.a.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return(n=this).fullscreenLoading=!0,e.next=4,n.filterSubmitHandle(t).then(function(e){n.fullscreenLoading=!1,n.$message.success(n.$i18n.t("message.success"))}).catch(function(e){n.fullscreenLoading=!1,n.$message.error(e)});case 4:case"end":return e.stop()}},e,this)}));return function(t){return e.apply(this,arguments)}}(),chartResizeHandle:function(){}},computed:{showDailyChart:function(){return this.chartSelected.indexOf("chart_daily")>=0}},watch:{screenWidth:function(e){if(!this.timer){this.screenWidth=e,this.timer=!0;var t=this;setTimeout(function(){console.log(t.screenWidth),l.default.chartResizeHandle(t.dailyChart),t.timer=!1},500)}}}},h={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("el-container",[n("el-aside",{staticClass:"aside",class:e.asideShow?"aside-show":"aside-hide"},[n("div",{staticClass:"aside-toggle-btn"},[e.asideShow?n("el-button",{attrs:{icon:"el-icon-d-arrow-left",circle:"",size:"mini"},on:{click:function(t){return e.asideToggleHandler(!e.asideShow)}}}):n("el-button",{attrs:{icon:"el-icon-d-arrow-right",circle:"",size:"mini"},on:{click:function(t){return e.asideToggleHandler(!e.asideShow)}}})],1),e._v(" "),n("side-filter",{directives:[{name:"loading",rawName:"v-loading.fullscreen.lock",value:e.fullscreenLoading,expression:"fullscreenLoading",modifiers:{fullscreen:!0,lock:!0}}],attrs:{chartModes:e.chartModes,getLineUrl:"/v1/statamazonline/"},on:{listenFilterSubmit:e.filterSubmit}})],1),e._v(" "),n("el-container",[n("el-main",{style:e.fixShow?"margin :0 0 0 270px;":"",attrs:{id:"main-box"}},[n("h1",[e._v("Report List")]),e._v(" "),n("div",{directives:[{name:"show",rawName:"v-show.sync",value:e.showDailyChart,expression:"showDailyChart",modifiers:{sync:!0}}],staticClass:"chart-box"},[n("div",{staticClass:"chart",attrs:{id:"chartDaily"}})])])],1)],1)},staticRenderFns:[]};var u=n("VU/8")(d,h,!1,function(e){n("LU9U")},"data-v-e21ea816",null);t.default=u.exports}});
//# sourceMappingURL=8.js.map