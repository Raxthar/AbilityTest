<template>
  <div class="layout">
    <Layout>
      <Header>
        <Button :size="buttonSize" type="primary" to="/HelloWorld">
          <Icon type="ios-arrow-back" />
          返回
        </Button>
      </Header>
      <Content>
        <Button :size="buttonSize" type="primary" @click="jumpToAddTitle">
          创建测评
        </Button>
      </Content>
      <Footer>
        <card>
        </card>
      </Footer>
    </Layout>
  </div>
</template>

<script>
export default {
  mounted () {
    this.searchStat()
  },
  data () {
    return {
      tId: this.$route.params.tId,
      pNumber: [],
      dName: [],
      statData: []
    }
  },
  methods: {
      searchStat () {
        this.$axios.get('test_stat', {
        params: {
          tId: this.tId
        }
      }).then(message => {
        if (message.data.code === 200) {
          if (message.data.pNumber.length > 0) {
            this.pNumber = message.data.pNumber
            this.dName = message.data.dName
            for (let i = 0; i < dName.length; i++) {
              let obj = {
                number: pNumber[i],
                name: dName[i]
              }
              this.statData.push(obj)
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
</style>
