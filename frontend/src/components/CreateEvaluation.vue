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
      u_id: 1,
      columns: [
        {
          title: '测评号',
          key: 't_id'
        },
        {
          title: '测评名',
          key: 't_name'
        },
        {
          title: '测评状态',
          key: 't_status'
        },
        {
          title: '截止日期',
          key: 't_due'
        }
      ],
      evaluationData: [],
      buttonSize: 'large'
    }
  },
  methods: {
    jumpToAddTitle () {
      this.$router.push('/AddEvaluationTitle/' + this.u_id)
    },
    searchEvaluation () {
      this.$axios.get('searchEvalution', {
        params: {
          content: this.u_id
        }
      }).then(response => {
        if (response.data.code === 200) {
          if (response.data.data && JSON.parse(response.data.data).length > 0) {
            this.evaluationData = []
            let evaluations = JSON.parse(response.data.data)
            for (let i in evaluations) {
              let t_status = Number(evaluations[i].fields.t_status)
              if (t_status === 1){
                let obj = {
                  t_id: evaluations[i].fields.t_id,
                  t_name: evaluations[i].fields.t_name,
                  t_status: '已发布',
                  t_due: evaluations[i].fields.t_due
                }
                this.evaluationData.push(obj)
              } else if (t_status === 0) {
                let obj = {
                  t_id: evaluations[i].fields.t_id,
                  t_name: evaluations[i].fields.t_name,
                  t_status: '未发布',
                  t_due: evaluations[i].fields.t_due
                }
                this.evaluationData.push(obj)
              }
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
