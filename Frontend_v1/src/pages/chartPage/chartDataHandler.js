import Configs from '@/lib/sysConfig'
const defaultColorHandler = {
  defaultColorList : ['#2D132C','#801336','#EE4540','#5BD1D7','#004D61','#FEB9C8','#FFE837','#FFD19A','#D2F3E0','#735372', '#BDF2D5','#5D13E7','#009975','#D9D872','#FF6337','#8A00D4','#94FC13','#EFB9C8','#EE5A5A','#FFF8A6'],
  //TODO 待定
  randomColorList : function(){
    let rgb='rgb('+Math.floor(Math.random()*255)+','
      +Math.floor(Math.random()*255)+','
      +Math.floor(Math.random()*255)+ ')';
    return rgb;

  }
};
const chartDataHandler = {
  chartResizeHandle: function (chart, width, Height) {
    chart.resize('auto', 'auto')
  },

  /**
   * sku日访问统计数据处理
   * @param chart echarts
   * @param data
   * @param vm
   */
  skuDailyChangHandle: function (chart, data, vm) {
    //  清除旧数据
    chart.clear();

    let _legend = [], _day = [], _series = {}, _seriesData = [];
    data.forEach((item, index) => {
      _legend.push(item['sku'])
      _day.push(item['dy'])
      if (_series[item['sku']] != undefined && _series[item['sku']]['data'] != undefined) {
        _series[item['sku']]['data'].push(item['num'])
      } else {
        var _data = [item['num']]
        _series[item['sku']] = {
          name: item['sku'],
          type: 'line',
          // stack: 'total',
          // smooth: true,
          label: {show: true, position: 'top'},
          encode: {
            x: 'dy', y: 'num'
          },
          data: _data
        }
      }
    });
    Object.keys(_series).forEach(function (key, index) {
      //获取生成的颜色代码
      let lineColor = defaultColorHandler.defaultColorList[index] || defaultColorHandler.randomColorList();
      _series[key].itemStyle = {
        normal: {
          lineStyle: {
            color: lineColor
          }
        }
      };
      _seriesData.push(_series[key])
    });

    let chartOptions = {
      title: {text: vm.$i18n.t('w.' + Configs.system.chartMode.daily.name)},
      tooltip: {trigger: 'axis'},
      color: defaultColorHandler.defaultColorList,
      legend: {
        type: 'scroll',
        orient: 'vertical',
        left: '85%',
        top: '10%',
        width: '8%',
        tooltip: {
          show: true
        },
        textStyle: {
          fontSize: 11
        },
        data: Array.from(new Set(_legend))
      },
      grid: {left: '5%', right: '15%', bottom: '5%', containLabel: true},
      toolbox: {
        feature: {
          saveAsImage: {},
          dataZoom: {yAxisIndex: false},
        }
      },
      dataZoom: [{type: 'slider', start: 0, end: 100, filterMode: 'weakFilter', realtime: false}],
      xAxis: {
        type: 'category',
        boundaryGap: false,
        data: Array.from(new Set(_day))
      },
      yAxis: {type: 'value'},
      series: _seriesData
    };
    !!!chart || chart.setOption(chartOptions);
    return chartOptions;
  },
  /**
   * sku月访问统计数据处理
   * @param chart
   * @param data
   * @param vm
   */
  skuMonthlyChangeHandle: function (chart, data, vm) {
    console.log('数据', data, chart);
    chart.clear();

    let _legend = [], _mon = [], _series = {}, _seriesData = [];
    data.forEach((item, index) => {
      _legend.push(item['sku'])
      _mon.push([item['yr'], item['mo']].join('-'));
      if (_series[item['sku']] != undefined && _series[item['sku']]['data'] != undefined) {
        _series[item['sku']]['data'].push(item['num'])
      } else {
        var _data = [item['num']]
        _series[item['sku']] = {
          name: item['sku'],
          type: 'line',
          // stack: 'total',
          // smooth: true,
          label: {show: true, position: 'top'},
          encode: {
            x: 'dy', y: 'num'
          },
          data: _data
        }
      }
    })
    Object.keys(_series).forEach(function (key, index) {
      //获取生成的颜色代码
      let lineColor = defaultColorHandler.defaultColorList[index] || defaultColorHandler.randomColorList();
      _series[key].itemStyle = {
        normal: {
          lineStyle: {
            color: lineColor
          }
        }
      };
      _seriesData.push(_series[key])
    });


    let chartOptions = {
      title: {text: vm.$i18n.t('w.' + Configs.system.chartMode.monthly.name)},
      tooltip: {trigger: 'axis'},
      color: defaultColorHandler.defaultColorList,
      legend: {
        type: 'scroll',
        orient: 'vertical',
        left: '85%',
        top: '10%',
        width: '8%',
        tooltip: {
          show: true
        },
        textStyle: {
          fontSize: 11
        }, data: Array.from(new Set(_legend))
      },
      grid: {left: '5%', right: '15%', bottom: '5%', containLabel: true},
      toolbox: {
        feature: {
          saveAsImage: {},
          dataZoom: {yAxisIndex: false},
        }
      },
      dataZoom: [{type: 'slider', start: 0, end: 100, filterMode: 'weakFilter', realtime: false}],
      xAxis: {
        type: 'category',
        boundaryGap: false,
        data: Array.from(new Set(_mon))
      },
      yAxis: {type: 'value'},
      series: _seriesData
    };
    !!!chart || chart.setOption(chartOptions);
    return chartOptions;
  },
  /**
   * 周表
   * @param chart
   * @param data
   * @param vm
   * @returns {{title: {text: string}, tooltip: {trigger: string}, legend: {data: any[]}, grid: {left: string, right: string, bottom: string, containLabel: boolean}, toolbox: {feature: {saveAsImage: {}, dataZoom: {yAxisIndex: boolean}}}, dataZoom: {type: string, start: number, end: number}[], xAxis: {type: string, boundaryGap: boolean, data: any[]}, yAxis: {type: string}, series: Array}}
   */
  skuWeeklyChangeHandle: function (chart, data, vm) {
    console.log('数据', data, chart);
    chart.clear();

    let _legend = [], _week = [], _series = {}, _seriesData = [];
    data.forEach((item, index) => {
      _legend.push(item['sku'])
      _week.push([item['yr'], 'w', item['wk']].join('-'));
      if (_series[item['sku']] != undefined && _series[item['sku']]['data'] != undefined) {
        _series[item['sku']]['data'].push(item['num'])
      } else {
        var _data = [item['num']]
        _series[item['sku']] = {
          name: item['sku'],
          type: 'line',
          // stack: 'total',
          // smooth: true,
          label: {show: true, position: 'top'},
          encode: {
            x: 'dy', y: 'num'
          },
          data: _data
        }
      }
    })
    Object.keys(_series).forEach(function (key, index) {
      //获取生成的颜色代码
      let lineColor = defaultColorHandler.defaultColorList[index] || defaultColorHandler.randomColorList();
      _series[key].itemStyle = {
        normal: {
          lineStyle: {
            color: lineColor
          }
        }
      };
      _seriesData.push(_series[key])
    });

    let chartOptions = {
      title: {text: vm.$i18n.t('w.' + Configs.system.chartMode.weekly.name)},
      tooltip: {trigger: 'axis'},
      color: defaultColorHandler.defaultColorList,
      legend: {
        type: 'scroll',
        orient: 'vertical',
        left: '85%',
        top: '10%',
        width: '8%',
        tooltip: {
          show: true
        },
        textStyle: {
          fontSize: 11
        }, data: Array.from(new Set(_legend))
      },
      grid: {left: '5%', right: '15%', bottom: '5%', containLabel: true},
      toolbox: {
        feature: {
          saveAsImage: {},
          dataZoom: {yAxisIndex: false},
        }
      },
      dataZoom: [{type: 'slider', start: 0, end: 100, filterMode: 'weakFilter', realtime: false}],
      xAxis: {
        type: 'category',
        boundaryGap: false,
        data: Array.from(new Set(_week))
      },
      yAxis: {type: 'value'},
      series: _seriesData
    };
    !!!chart || chart.setOption(chartOptions);
    return chartOptions;
  },


  /**
   * line 日访问统计数据处理
   * @param chart echarts
   * @param data
   * @param vm
   */
  lineDailyChangHandle: function (chart, data, vm) {
    //  清除旧数据
    chart.clear();

    let _legend = [], _day = [], _series = {}, _seriesData = [];
    data.forEach((item, index) => {
      _legend.push(item['title'])
      _day.push(item['dy'])
      if (_series[item['title']] != undefined && _series[item['title']]['data'] != undefined) {
        _series[item['title']]['data'].push(item['num'])
      } else {
        var _data = [item['num']]
        _series[item['title']] = {
          name: item['title'],
          type: 'line',
          // stack: 'total',
          // smooth: true,
          label: {show: true, position: 'top'},
          encode: {
            x: 'dy', y: 'num'
          },
          data: _data
        }
      }
    })
    Object.keys(_series).forEach(function (key, index) {
      //获取生成的颜色代码
      let lineColor = defaultColorHandler.defaultColorList[index] || defaultColorHandler.randomColorList();
      _series[key].itemStyle = {
        normal: {
          lineStyle: {
            color: lineColor
          }
        }
      };
      _seriesData.push(_series[key])
    });

    let chartOptions = {
      title: {text: vm.$i18n.t('w.' + Configs.system.chartMode.daily.name)},
      tooltip: {trigger: 'axis'},
      color: defaultColorHandler.defaultColorList,
      legend: {
        type: 'scroll',
        orient: 'vertical',
        left: '85%',
        top: '10%',
        width: '8%',
        tooltip: {
          show: true
        },
        textStyle: {
          fontSize: 11
        },
        data: Array.from(new Set(_legend))
      },
      grid: {left: '5%', right: '15%', bottom: '5%', containLabel: true},
      toolbox: {
        feature: {
          saveAsImage: {},
          dataZoom: {yAxisIndex: false},
        }
      },
      dataZoom: [{type: 'slider', start: 0, end: 100, filterMode: 'weakFilter', realtime: false}],
      xAxis: {
        type: 'category',
        boundaryGap: false,
        data: Array.from(new Set(_day))
      },
      yAxis: {type: 'value'},
      series: _seriesData
    };
    !!!chart || chart.setOption(chartOptions);
    return chartOptions;
  },
  /**
   * line月访问统计数据处理
   * @param chart
   * @param data
   * @param vm
   */
  lineMonthlyChangeHandle: function (chart, data, vm) {
    console.log('数据', data, chart);
    chart.clear();

    let _legend = [], _mon = [], _series = {}, _seriesData = [];
    data.forEach((item, index) => {
      _legend.push(item['title'])
      _mon.push([item['yr'], item['mo']].join('-'));
      if (_series[item['title']] != undefined && _series[item['title']]['data'] != undefined) {
        _series[item['title']]['data'].push(item['num'])
      } else {
        var _data = [item['num']]
        _series[item['title']] = {
          name: item['title'],
          type: 'line',
          // stack: 'total',
          // smooth: true,
          label: {show: true, position: 'top'},
          encode: {
            x: 'dy', y: 'num'
          },
          data: _data
        }
      }
    })
    Object.keys(_series).forEach(function (key, index) {
      //获取生成的颜色代码
      let lineColor = defaultColorHandler.defaultColorList[index] || defaultColorHandler.randomColorList();
      _series[key].itemStyle = {
        normal: {
          lineStyle: {
            color: lineColor
          }
        }
      };
      _seriesData.push(_series[key])
    });


    let chartOptions = {
      title: {text: vm.$i18n.t('w.' + Configs.system.chartMode.monthly.name)},
      tooltip: {trigger: 'axis'},
      color: defaultColorHandler.defaultColorList,
      legend: {
        type: 'scroll',
        orient: 'vertical',
        left: '85%',
        top: '10%',
        width: '8%',
        tooltip: {
          show: true
        },
        textStyle: {
          fontSize: 11
        }, data: Array.from(new Set(_legend))
      },
      grid: {left: '5%', right: '15%', bottom: '5%', containLabel: true},
      toolbox: {
        feature: {
          saveAsImage: {},
          dataZoom: {yAxisIndex: false},
        }
      },
      dataZoom: [{type: 'slider', start: 0, end: 100, filterMode: 'weakFilter', realtime: false}],
      xAxis: {
        type: 'category',
        boundaryGap: false,
        data: Array.from(new Set(_mon))
      },
      yAxis: {type: 'value'},
      series: _seriesData
    };
    !!!chart || chart.setOption(chartOptions);
    return chartOptions;
  },
  /**
   * line周表
   * @param chart
   * @param data
   * @param vm
   * @returns {{title: {text: string}, tooltip: {trigger: string}, legend: {data: any[]}, grid: {left: string, right: string, bottom: string, containLabel: boolean}, toolbox: {feature: {saveAsImage: {}, dataZoom: {yAxisIndex: boolean}}}, dataZoom: {type: string, start: number, end: number}[], xAxis: {type: string, boundaryGap: boolean, data: any[]}, yAxis: {type: string}, series: Array}}
   */
  lineWeeklyChangeHandle: function (chart, data, vm) {
    console.log('数据', data, chart);
    chart.clear();

    let _legend = [], _week = [], _series = {}, _seriesData = [];
    data.forEach((item, index) => {
      _legend.push(item['title'])
      _week.push([item['yr'], 'w', item['wk']].join('-'));
      if (_series[item['title']] != undefined && _series[item['title']]['data'] != undefined) {
        _series[item['title']]['data'].push(item['num'])
      } else {
        var _data = [item['num']]
        _series[item['title']] = {
          name: item['title'],
          type: 'line',
          // stack: 'total',
          // smooth: true,
          label: {show: true, position: 'top'},
          encode: {
            x: 'wk', y: 'num'
          },
          data: _data
        }
      }
    })
    Object.keys(_series).forEach(function (key, index) {
      //获取生成的颜色代码
      let lineColor = defaultColorHandler.defaultColorList[index] || defaultColorHandler.randomColorList();
      _series[key].itemStyle = {
        normal: {
          lineStyle: {
            color: lineColor
          }
        }
      };
      _seriesData.push(_series[key])
    });


    let chartOptions = {
      title: {text: vm.$i18n.t('w.' + Configs.system.chartMode.weekly.name)},
      tooltip: {trigger: 'axis'},
      color: defaultColorHandler.defaultColorList,
      legend: {
        type: 'scroll',
        orient: 'vertical',
        left: '85%',
        top: '10%',
        width: '8%',
        tooltip: {
          show: true
        },
        textStyle: {
          fontSize: 11
        }, data: Array.from(new Set(_legend))
      },
      grid: {left: '5%', right: '15%', bottom: '5%', containLabel: true},
      toolbox: {
        feature: {
          saveAsImage: {},
          dataZoom: {yAxisIndex: false},
        }
      },
      dataZoom: [{type: 'slider', start: 0, end: 100, filterMode: 'weakFilter', realtime: false}],
      xAxis: {
        type: 'category',
        boundaryGap: false,
        data: Array.from(new Set(_week))
      },
      yAxis: {type: 'value'},
      series: _seriesData
    };
    !!!chart || chart.setOption(chartOptions);
    return chartOptions;
  },

  /**
   *
   * @param chart
   * @param data
   * @param vm
   * @returns {{yAxis: {type: string}, xAxis: {data: *[], type: string, boundaryGap: boolean}, color: string[], legend: {orient: string, top: string, data: *[], left: string, width: string, tooltip: {show: boolean}, textStyle: {fontSize: number}, type: string}, grid: {left: string, bottom: string, right: string, containLabel: boolean}, series: Array, tooltip: {trigger: string}, toolbox: {feature: {saveAsImage: {}, dataZoom: {yAxisIndex: boolean}}}, dataZoom: {filterMode: string, realtime: boolean, start: number, end: number, type: string}[], title: {text: VueI18n.TranslateResult}}}
   */
  skuDayCompositeHandle: function (chart, data, vm) {
    console.log('skuCompositeHandle');
    //  清除旧数据
    chart.clear();

    let _legend = [], _day = [], _series = {}, _seriesData = [];
    data.forEach((item, index) => {
      _legend.push(item['sku'] + '_Total Order Items');
      _legend.push(item['sku'] + '_UV');
      _legend.push(item['sku'] + '_PV');
      //_legend.push(item['sku'])
      _day.push(item['dy']);

      _series = this.skuCompositeProcessData(item, _series);
    });
    console.log('-----------------------------------------------------------------------');
    console.log(_series);
    Object.keys(_series).forEach(function (key, index) {
      //获取生成的颜色代码
      let lineColor = defaultColorHandler.defaultColorList[index] || defaultColorHandler.randomColorList();

      if (!_series[key].itemStyle) {
        _series[key].itemStyle = {
          normal: {
            lineStyle: {
              color: lineColor
            }
          }
        };
      } else {
        let lineColorStyle = {
          lineStyle: {
            color: lineColor
          }
        };
        _series[key].itemStyle.normal = Object.assign(_series[key].itemStyle.normal, lineColorStyle);
      }
      // _series[key]['itemStyle']['normal']['lineStyle']['color'] = lineColor;
      _seriesData.push(_series[key])
    });

    let chartOptions = {
      title: {text: vm.$i18n.t('w.' + Configs.system.chartMode.daily.name)},
      tooltip: {trigger: 'axis'},
      color: defaultColorHandler.defaultColorList,
      legend: {
        type: 'scroll',
        orient: 'vertical',
        left: '85%',
        top: '10%',
        width: '8%',
        tooltip: {
          show: true
        },
        textStyle: {
          fontSize: 11
        },
        data: Array.from(new Set(_legend))
      },
      grid: {left: '5%', right: '15%', bottom: '5%', containLabel: true},
      toolbox: {
        feature: {
          saveAsImage: {},
          dataZoom: {yAxisIndex: false},
        }
      },
      dataZoom: [{type: 'slider', start: 0, end: 100, filterMode: 'weakFilter', realtime: false}],
      xAxis: {
        type: 'category',
        boundaryGap: false,
        data: Array.from(new Set(_day))
      },
      yAxis: {type: 'value'},
      series: _seriesData
    };
    !!!chart || chart.setOption(chartOptions);
    return chartOptions;
  },

  /**
   *
   * @param chart
   * @param data
   * @param vm
   * @returns {{yAxis: {type: string}, xAxis: {data: *[], type: string, boundaryGap: boolean}, color: string[], legend: {orient: string, top: string, data: *[], left: string, width: string, tooltip: {show: boolean}, textStyle: {fontSize: number}, type: string}, grid: {left: string, bottom: string, right: string, containLabel: boolean}, series: Array, tooltip: {trigger: string}, toolbox: {feature: {saveAsImage: {}, dataZoom: {yAxisIndex: boolean}}}, dataZoom: {filterMode: string, realtime: boolean, start: number, end: number, type: string}[], title: {text: VueI18n.TranslateResult}}}
   */
  skuMonthCompositeHandle: function (chart, data, vm) {
    console.log('数据', data, chart);
    chart.clear();

    let _legend = [], _mon = [], _series = {}, _seriesData = [];
    data.forEach((item, index) => {
      _legend.push(item['sku'] + '_Total Order Items');
      _legend.push(item['sku'] + '_UV');
      _legend.push(item['sku'] + '_PV');
      _mon.push([item['yr'], item['mo']].join('-'));

      _series = this.skuCompositeProcessData(item, _series);

    });
    console.log('**********************************************************************');
    console.log(_series);
    Object.keys(_series).forEach(function (key, index) {
      //获取生成的颜色代码
      let lineColor = defaultColorHandler.defaultColorList[index] || defaultColorHandler.randomColorList();
      if (!_series[key].itemStyle) {
        _series[key].itemStyle = {
          normal: {
            lineStyle: {
              color: lineColor
            }
          }
        };
      } else {
        let lineColorStyle = {
          lineStyle: {
            color: lineColor
          }
        };
        _series[key].itemStyle.normal = Object.assign(_series[key].itemStyle.normal, lineColorStyle);
      }
      _seriesData.push(_series[key])
    });


    let chartOptions = {
      title: {text: vm.$i18n.t('w.' + Configs.system.chartMode.monthly.name)},
      tooltip: {trigger: 'axis'},
      color: defaultColorHandler.defaultColorList,
      legend: {
        type: 'scroll',
        orient: 'vertical',
        left: '85%',
        top: '10%',
        width: '8%',
        tooltip: {
          show: true
        },
        textStyle: {
          fontSize: 11
        }, data: Array.from(new Set(_legend))
      },
      grid: {left: '5%', right: '15%', bottom: '5%', containLabel: true},
      toolbox: {
        feature: {
          saveAsImage: {},
          dataZoom: {yAxisIndex: false},
        }
      },
      dataZoom: [{type: 'slider', start: 0, end: 100, filterMode: 'weakFilter', realtime: false}],
      xAxis: {
        type: 'category',
        boundaryGap: false,
        data: Array.from(new Set(_mon))
      },
      yAxis: {type: 'value'},
      series: _seriesData
    };
    !!!chart || chart.setOption(chartOptions);
    return chartOptions;
  },

  /**
   *
   * @param chart
   * @param data
   * @param vm
   * @returns {{yAxis: {type: string}, xAxis: {data: *[], type: string, boundaryGap: boolean}, color: string[], legend: {orient: string, top: string, data: *[], left: string, width: string, tooltip: {show: boolean}, textStyle: {fontSize: number}, type: string}, grid: {left: string, bottom: string, right: string, containLabel: boolean}, series: Array, tooltip: {trigger: string}, toolbox: {feature: {saveAsImage: {}, dataZoom: {yAxisIndex: boolean}}}, dataZoom: {filterMode: string, realtime: boolean, start: number, end: number, type: string}[], title: {text: VueI18n.TranslateResult}}}
   */
  skuWeeklyCompositeHandle: function(chart, data, vm){
    console.log('数据', data, chart);
    chart.clear();

    let _legend = [], _week = [], _series = {}, _seriesData = [];
    data.forEach((item, index) => {
      _legend.push(item['sku'] + '_Total Order Items');
      _legend.push(item['sku'] + '_UV');
      _legend.push(item['sku'] + '_PV');

      _week.push([item['yr'], 'w', item['wk']].join('-'));
      _series = this.skuCompositeProcessData(item, _series);
    });
    console.log(_series);
    Object.keys(_series).forEach(function (key, index) {
      //获取生成的颜色代码
      let lineColor = defaultColorHandler.defaultColorList[index] || defaultColorHandler.randomColorList();
      if (!_series[key].itemStyle) {
        _series[key].itemStyle = {
          normal: {
            lineStyle: {
              color: lineColor
            }
          }
        };
      } else {
        let lineColorStyle = {
          lineStyle: {
            color: lineColor
          }
        };
        _series[key].itemStyle.normal = Object.assign(_series[key].itemStyle.normal, lineColorStyle);
      }
      _seriesData.push(_series[key])
    });

    let chartOptions = {
      title: {text: vm.$i18n.t('w.' + Configs.system.chartMode.weekly.name)},
      tooltip: {trigger: 'axis'},
      color: defaultColorHandler.defaultColorList,
      legend: {
        type: 'scroll',
        orient: 'vertical',
        left: '85%',
        top: '10%',
        width: '8%',
        tooltip: {
          show: true
        },
        textStyle: {
          fontSize: 11
        }, data: Array.from(new Set(_legend))
      },
      grid: {left: '5%', right: '15%', bottom: '5%', containLabel: true},
      toolbox: {
        feature: {
          saveAsImage: {},
          dataZoom: {yAxisIndex: false},
        }
      },
      dataZoom: [{type: 'slider', start: 0, end: 100, filterMode: 'weakFilter', realtime: false}],
      xAxis: {
        type: 'category',
        boundaryGap: false,
        data: Array.from(new Set(_week))
      },
      yAxis: {type: 'value'},
      series: _seriesData
    };
    !!!chart || chart.setOption(chartOptions);
    return chartOptions;
  },

  skuCompositeProcessData: function(item, series){
    let _series = series || [];
    if ((_series[item['sku'] + '-total_order_items_num'] != undefined && _series[item['sku'] + '-total_order_items_num']['data'] != undefined) ||
      (_series[item['sku'] + '-uv'] != undefined && _series[item['sku'] + '-uv']['data'] != undefined) ||
      (_series[item['sku'] + '-pv'] != undefined && _series[item['sku'] + '-pv']['data'] != undefined)) {
      _series[item['sku'] + '-total_order_items_num']['data'].push(item['total_order_items_num']);
      _series[item['sku'] + '-uv']['data'].push(item['uv_num']);
      _series[item['sku'] + '-pv']['data'].push(item['pv_num']);
    } else {
      let _totalOrderItemsData = [item['total_order_items_num']];
      let _uvData = [item['uv_num']];
      let _pvData = [item['pv_num']];

      _series[item['sku'] + '-total_order_items_num'] = {
        name: item['sku'] + '_Total Order Items',
        type: 'line',
        // stack: 'total',
        // smooth: true,
        label: {show: true, position: 'top'},
        encode: {
          x: 'dy', y: 'total_order_items_num'
        },
        data: _totalOrderItemsData
      };

      _series[item['sku'] + '-uv'] = {
        name: item['sku'] + '_UV',
        type: 'bar',
        // stack: 'total',
        // smooth: true,
        label: {show: true, position: 'top'},
        encode: {
          x: 'dy', y: 'uv_num'
        },
        data: _uvData
      };

      _series[item['sku'] + '-pv'] = {
        name: item['sku'] + '_PV',
        type: 'line',
        // stack: 'total',
        // smooth: true,
        label: {show: true, position: 'top'},
        encode: {
          x: 'dy', y: 'pv_num'
        },
        itemStyle: {normal: {areaStyle: {type: 'default'}}},
        data: _pvData
      };
    }

    return _series;
  }
};

export default chartDataHandler
