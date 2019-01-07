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
          <Table :data="evaluationData">
          </Table>
        </card>
      </Footer>
    </Layout>
  </div>
</template>

<script>
export default {
  mounted () {
    this.searchEvaluation()
  },
  data () {
    return {
      uID: 1,
      columns: [
        {
          title: '测评号',
          key: 'tID'
        },
        {
          title: '测评名',
          key: 'tName'
        },
        {
          title: '测评状态',
          key: 'tStatus'
        },
        {
          title: '截止日期',
          key: 'tDue'
        }
      ],
      evaluationData: [],
      buttonSize: 'large'
    }
  },
  methods: {
    jumpToAddTitle () {
      this.$router.push('/AddEvaluationTitle/' + this.uID)
    },
    searchEvaluation () {
      this.$axios.get('searchEvalution', {
        params: {
          content: this.uID
        }
      }).then(res => {
        if (res.data.code === 200) {
          if (res.data.data && JSON.parse(res.data.data).length > 0) {
            this.evaluationData = []
            let evaluations = JSON.parse(res.data.data)
            for (let i in evaluations) {
              tStatus = Number(books[i].fields.tStatus)
              if (tSatus === 1){
                let obj = {
                  tID: evaluations[i].fields.tID,
                  tName: evaluations[i].fields.tName,
                  tStatus: '已发布',
                  tDue: evaluations[i].fields.tDue
                }
              } else {
                let obj = {
                  tID: evaluations[i].fields.tID,
                  tName: evaluations[i].fields.tName,
                  tStatus: '未发布',
                  tDue: evaluations[i].fields.tDue
                }
              }
              this.evaluationData.push(obj)
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
