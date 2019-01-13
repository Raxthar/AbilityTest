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
        <Button :size="buttonSize" type="primary" @click="jumpToAdd">
          创建测评
        </Button>
      </Content>
      <Footer>
        <card>
          <Table border :columns="columns" :data="evaluationData">
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
      uId: 1,
      columns: [
        {
          title: '测评号',
          key: 'tId',
          width: 150
        },
        {
          title: '测评名',
          key: 'tName',
          width: 200
        },
        {
          title: '测评状态',
          key: 'tStatus',
          width: 150
        },
        {
          title: '截止日期',
          key: 'tDue',
          width: 200
        },
        {
          title: '操作',
          key: 'action',
          align: 'center',
          render: (buttonmethod, params) => {
            return buttonmethod('div', [
              buttonmethod('Button', {
                props: {
                  type: 'primary',
                  size: 'small'
                },
                style: {
                  marginRight: '5px'
                },
                on: {
                  click: () => {
                    this.evaluationEdit(params.index)
                  }
                }
              }, '编辑'),
              buttonmethod('Button', {
                props: {
                  type: 'primary',
                  size: 'small'
                },
                style: {
                  marginRight: '5px'
                },
                on: {
                  click: () => {
                    this.questionEdit(params.index)
                  }
                }
              }, '发布'),
              buttonmethod('Button', {
                props: {
                  type: 'primary',
                  size: 'small'
                },
                style: {
                  marginRight: '5px'
                },
                on: {
                  click: () => {
                    this.questionEdit(params.index)
                  }
                }
              }, '分享'),
              buttonmethod('Button', {
                props: {
                  type: 'primary',
                  size: 'small'
                },
                style: {
                  marginRight: '5px'
                },
                on: {
                  click: () => {
                    this.questionEdit(params.index)
                  }
                }
              }, '统计'),
              buttonmethod('Button', {
                props: {
                  type: 'primary',
                  size: 'small'
                },
                style: {
                  marginRight: '5px'
                },
                on: {
                  click: () => {
                    this.editJudge(params.index)
                  }
                }
              }, '设置'),
              buttonmethod('Button', {
                props: {
                  type: 'error',
                  size: 'small'
                },
                on: {
                  click: () => {
                    this.deleteEvaluation(params.index)
                  }
                }
              }, '删除')
            ])
          }
        }
      ],
      evaluationData: [],
      tId: [],
      tName: [],
      tDue: [],
      tStatus: [],
      buttonSize: 'large'
    }
  },
  methods: {
    jumpToAdd () {
      this.$router.push('/AddEvaluationTitle/' + this.uId)
    },
    jumpBack () {
      this.$router.push('/Welcome/')
    },
    searchEvaluation () {
      this.$axios.get('test_list', {
        params: {
          uId: this.uId
        }
      }).then(message => {
        if (message.data.code === 200) {
          if (message.data.tName.length > 0) {
            this.evaluationData = []
            this.tId = message.data.tId
            this.tName = message.data.tName
            this.tDue = message.data.tDue
            this.tStatus = message.data.tStatus
            for (let i = 0; i < message.data.tName.length; i++) {
              let tStatus = this.tStatus[i]
              if (tStatus === 1) {
                let obj = {
                  tId: this.tId[i],
                  tName: this.tName[i],
                  tStatus: '已发布',
                  tDue: this.tDue[i]
                }
                this.evaluationData.push(obj)
              } else if (tStatus === 0) {
                let obj = {
                  tId: this.tId[i],
                  tName: this.tName[i],
                  tStatus: '未发布',
                  tDue: this.tDue[i]
                }
                this.evaluationData.push(obj)
              }
            }
            this.$Message.info(`Create ${this.evaluationData[0].tName} Success`)
          }
        } else {
          this.$Message.error(`can't search in database`)
        }
      })
    },
    deleteEvaluation (index) {
      this.$axios.post('/delete_evaluation/', JSON.stringify(this.evaluationData[index])).then(response => {
        if (response.data.code === 200) {
          this.$Message.success(`delete ${this.evaluationData[index].tName} success`)
          this.evaluationData.splice(index, 1)
        } else {
          this.$Message.info("can't read database")
        }
      })
    },
    evaluationEdit (index) {
      this.$router.push('/EvaluationEdit/' + this.uId + '/' + this.evaluationData[index].tId)
    },
    questionStat (index) {
      this.$router.push('/EvaluationStat/' + this.evaluationData[index].tId)
    },
    editJudge (index) {
      this.$router.push('/AddJudge/' + this.evaluationData[index].tId)
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
