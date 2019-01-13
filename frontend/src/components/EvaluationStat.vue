<template>
  <div class="layout">
    <Layout>
      <Header>
        <Button :size="buttonSize" type="primary" @click="jumpBack">
          <Icon type="ios-arrow-back" />
          返回
        </Button>
      </Header>
      <Content>
      </Content>
      <Footer>
        <card>
          <div id="statChart" class="chartSize"></div>
          <Table border :columns="columns" :data="option.series.statData"></Table>
        </card>
      </Footer>
    </Layout>
  </div>
</template>

<script>
export default {
  mounted () {
    this.searchStat()
    let myChart = this.$echarts.init(document.getElementById('statChart'))
    myChart.setOption(this.option)
  },
  data () {
    return {
      tId: this.$route.params.tId,
      pNumber: [],
      dName: [],
      columns: [
        {
          title: '维度',
          key: 'name',
          width: 150
        },
        {
          title: '人数',
          key: 'value',
          width: 200
        }
      ],
      option: {
        backgroundColor: '#2c343c',
        title: {
          text: 'Customized Pie',
          left: 'center',
          top: 20,
          textStyle: {
            color: '#ccc'
          }
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        visualMap: {
          show: false,
          min: 80,
          max: 600,
          inRange: {
            colorLightness: [0, 1]
          }
        },
        series: [{
          name: '维度',
          type: 'pie',
          radius: '55%',
          center: ['50%', '50%'],
          statData: [].sort(function (a, b) { return a.value - b.value }),
          roseType: 'radius',
          label: {
            normal: {
              textStyle: {
                color: 'rgba(255, 255, 255, 0.3)'
              }
            }
          },
          labelLine: {
            normal: {
              lineStyle: {
                color: 'rgba(255, 255, 255, 0.3)'
              },
              smooth: 0.2,
              length: 10,
              length2: 20
            }
          },
          itemStyle: {
            normal: {
              color: '#c23531',
              shadowBlur: 200,
              shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
          },
          animationType: 'scale',
          animationEasing: 'elasticOut',
          animationDelay: function (idx) {
            return Math.random() * 200
          }
        }]
      }
    }
  },
  methods: {
    jumpBack () {
      this.$router.push('/CreateEvaluation/')
    },
    searchStat () {
      this.$axios.get('search_stat', {
        params: {
          tId: this.tId
        }
      }).then(message => {
        if (message.data.code === 200) {
          if (message.data.pNumber.length > 0) {
            this.pNumber = message.data.pNumber
            this.dName = message.data.dName
            for (let i = 0; i < this.dName.length; i++) {
              let obj = {
                value: this.pNumber[i],
                name: this.dName[i]
              }
              this.option.series.statData.push(obj)
            }
          }
        } else {
          this.$Message.error(`can't search in database`)
        }
      })
    }
  }
}
</script>

<style>
.layout {
  height: 100vmin;
}

.ivu-layout-header {
  background-color: rgb(97, 176, 255);
  padding: 0 20px;
}

.ivu-layout-content {
  height: 80px;
  padding: 20px;
}

.ivu-btn-primary {
  background-color: rgb(97, 176, 255);
  border-color: rgb(97, 176, 255);
}

.ivu-btn-large {
  font-size: 18px;
}

.ivu-card {
  height: 100vmin;
  margin: auto auto;
  text-align: center;
}

.ivu-card-body {
  height: 500px;
  padding: 100px;
}

.ivu-card-bordered {
  border: 1px solid #f9f9fa;
  border-color: #fafafa;
}

.chartSize {
    width: 200px;
    height: 200px;
}
</style>
