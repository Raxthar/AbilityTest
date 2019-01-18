<template>
  <div class="layout">
    <Layout>
      <Header>
        <Button :size="buttonSize" type="primary" @click="jumpBack" id="backButton">
          <Icon type="ios-arrow-back" />
          返回
        </Button>
      </Header>
      <Footer>
        <card>
          <div id="statChart" class="chartSize"></div>
          <Table class="list" border :columns="columns" :data="tableData" style="width: 600px"></Table><br><br>
          <Button :size="buttonSize" icon="ios-download-outline" type="primary" @click="exportCsv" id="exportButton">导出</Button>
        </card>
      </Footer>
    </Layout>
  </div>
</template>

<script>
import CsvExportor from 'csv-exportor'
export default {
  mounted () {
    this.searchStat()
    this.getStatResult()
  },
  data () {
    return {
      buttonSize: 'large',
      tId: this.$route.params.tId,
      resultId: [],
      resultName: [],
      csvData: [],
      csvHeader: ['流水号', '测评结果'],
      pNumber: [],
      dName: [],
      tableData: [],
      columns: [
        {
          title: '维度',
          key: 'name',
          width: 400
        },
        {
          title: '人数',
          key: 'value',
          width: 200
        }
      ]
    }
  },
  methods: {
    jumpBack () {
      this.$router.push('/CreateEvaluation/')
    },
    searchStat () {
      let statData = []
      this.$axios.get('search_stat', {
        params: {
          tId: this.tId
        }
      }).then(response => {
        if (response.data.code === 200) {
          if (response.data.stat.length > 0) {
            this.pNumber = response.data.stat
            this.dName = response.data.dName
            for (let i = 0; i < this.dName.length; i++) {
              let obj = {
                value: this.pNumber[i],
                name: this.dName[i]
              }
              statData.push(obj)
            }
            this.tableData = statData
          }
        } else {
          this.$Message.error(`无法读取数据库`)
        }
        let myChart = this.$echarts.init(document.getElementById('statChart'))
        myChart.setOption({
          title: {
            text: '测评统计结果',
            x: 'center'
          },
          tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
          },
          legend: {
            orient: 'vertical',
            left: 'left',
            data: this.dName
          },
          series: [
            {
              name: '总数',
              type: 'pie',
              radius: '55%',
              center: ['50%', '60%'],
              data: statData,
              itemStyle: {
                emphasis: {
                  shadowBlur: 10,
                  shadowOffsetX: 0,
                  shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
              }
            }
          ]
        })
      })
    },
    getStatResult () {
      this.$axios.get('load_result', {
        params: {
          tId: this.tId
        }
      }).then(response => {
        if (response.data.code === 200) {
          if (response.data.resultId.length > 0) {
            this.resultId = response.data.resultId
            this.resultName = response.data.dName
            for (let i = 0; i < this.resultId.length; i++) {
              let obj = {
                rId: this.resultId[i],
                rName: this.resultName[i]
              }
              this.csvData.push(obj)
            }
          }
        } else {
          this.$Message.error(`无法读取数据库`)
        }
      })
    },
    exportCsv () {
      CsvExportor.downloadCsv(
        this.csvData,
        { header: this.csvHeader },
        'result.csv')
    }
  }
}
</script>

<style scoped>
.layout {
  height: 100vmin;
}

.ivu-layout-header {
  background-color: rgb(97, 176, 255);
  padding: 0 20px;
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
  margin-left: 800px;
}

.ivu-card-bordered {
  border: 1px solid #f9f9fa;
  border-color: #fafafa;
}

.chartSize {
  width: 400px;
  height: 400px;
  margin-left: 400px;
}

.list {
  margin-left: 300px;
}
</style>
