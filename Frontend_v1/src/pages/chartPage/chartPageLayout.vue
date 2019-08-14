<template>
  <div>
    <el-container>
      <el-header class="top-header" style="margin:0;position: fixed;width: 100%;z-index: 1000;" v-show="topNavShow">

        <!--导航头-->
        <div class="el-header-title" v-if="false">
          {{$t('w.chart_home_title')}}
        </div>

        <el-menu ref="topNav"
                 mode="horizontal"
                 :default-active="route_cur_path"
                 background-color="#545c64"
                 text-color="#fff"
                 active-text-color="#ffd04b"
                 router>

          <!--导航菜单-->
          <el-menu-item v-if='topNavList.length > 0 && item.disabled==false' v-for="item,index in topNavList"
                        :key="item.name"
                        :index="item.path"
                        :disabled="item.disabled"
          >
            {{$t('w.'+item.name)}}
          </el-menu-item>
          <!--多语言-->
          <el-submenu index="lang" style="float:right;" v-if="false">
            <template slot="title" class="el-dropdown-link">
              {{$t('system.lang.title')}}
            </template>
            <el-menu-item index="lang-en" disabled>{{$t('system.lang.english')}}</el-menu-item>
            <el-menu-item index="lang-zh" disabled>{{$t('system.lang.chinese')}}</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-header>
      <el-main style="padding: 0; ">
        <transition name="fade" mode="out-in">
          <router-view name="chart"></router-view>
        </transition>
      </el-main>
    </el-container>
  </div>
</template>

<script>
  import Configs from '@/lib/sysConfig'

  export default {
    name: "chartPageLayout",

    data() {
      return {
        //  导航列表,实例化时候动态加载
        topNavList: [],
        topNavListActiveIndex: '/chart',
        // topNavShow: process.env.NODE_ENV == 'development'
        topNavShow: true,
      }
    },
    mounted() {
      let vm = this;
      if (!!Configs.system.router.pages) {
        Configs.system.router.pages.forEach(item => {
          vm.topNavList.push({
            path: '/chart/' + item.path,
            title: vm.$i18n.t(item.title),
            name: item.name,
            disabled: !!item.disabled,
          })
        })
      }
    },
    methods: {},
    computed: {
      route_cur_path: function () {
        return this.$route.path
      },
      test_counter: _ => this.$store.getters.getConfig

    },
    watch: {
      route_cur_path: (nv, ov) => {
        this.topNavListActiveIndex = nv
      }
    }
  };
</script>

<style lang="stylus">
  .top-header
    box-sizing content-box
    transition all .6s
    top: -60px
    border-bottom 14px rgb(255, 208, 75) solid
    & > .el-menu
      border-bottom:none
    &:hover
      top: 0
      height: 60px
      border-bottom 0 rgb(255, 208, 75) solid

  .fade-enter-active, .fade-leave-active
    transition: opacity .5s;

  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
    opacity: 0;

  .el-header
    padding 0

    &-title
      float: left
      position: relative;
      z-index: 1;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 1.2em;
      color: white;


  .aside
    z-index: 1200

    & > .main
      /*position: fixed*/
      /*top 64px*/
      /*left: 1.5em;*/
      padding: auto
      margin: auto
      z-index 1000
      width 300px;

    &-toggle
      &-btn
        padding-top: 14px;
        /*position: fixed*/
        z-index: 1000
        transition all .3s
        //min-height: calc(100vh - 60px)
        text-align: right;
        margin: 8px 0 0 0;

    &-show
      background #eee
      width 270px !important
      transition all .3s

      .aside
        &-toggle
          &-btn
            top 64px
            left 300px
            z-index: 1200

    &-hide
      width: 15px !important
      transition all .5s

      .aside
        &-toggle
          &-btn
            top 64px
            left 0

      .main

        display none;

  .show
    display: inline-block;

  .hide
    display: none;
</style>
