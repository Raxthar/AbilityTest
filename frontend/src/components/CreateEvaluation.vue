<template>
  <div class="layout">
    <Layout>
      <Header>
        <Button :size="buttonSize" type="primary" @click="jumpBack" id="backButton">
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
          <Modal
            v-model="modal"
            title="Common Modal dialog box title"
            @on-ok="deleteEvaluation(getindex)"
            @on-cancel="cancel">
            <p>确认删除该测评吗？</p>
          </Modal>
          <BackTop :height="100" :bottom="200">
            <div class="top">返回顶端</div>
          </BackTop>
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
      getindex: 0,
      uId: 1,
      modal: false,
      columns: [
        {
          title: '测评名',
          key: 'tName',
          width: 200
        },
        {
          title: '测评描述',
          key: 'tDescribe',
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
                    this.getStat(params.index)
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
                    this.modal = true
                    this.getindex = params.index
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
      tDescribe: [],
      buttonSize: 'large'
    }
  },
  methods: {
    jumpToAdd () {
      this.$router.push('/AddEvaluationTitle/' + this.uId)
    },
    jumpBack () {
      this.$router.push('/')
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
            this.tDescribe = message.data.tDescribe
            for (let i = 0; i < message.data.tName.length; i++) {
              let obj = {
                tId: this.tId[i],
                tName: this.tName[i],
                tDescribe: this.tDescribe[i],
                tDue: this.tDue[i]
              }
              this.evaluationData.push(obj)
            }
          }
        } else {
          this.$Message.error(`无法读取数据库！`)
        }
      })
    },
    deleteEvaluation (index) {
      this.$axios.post('/delete_evaluation/', JSON.stringify(this.evaluationData[index])).then(response => {
        if (response.data.code === 200) {
          this.$Message.success(`删除 ${this.evaluationData[index].tName} 成功！`)
          this.getindex = 0
          this.evaluationData.splice(index, 1)
        } else {
          this.$Message.error('无法读取数据库！')
        }
      })
    },
    evaluationEdit (index) {
      this.$router.push('/EvaluationEdit/' + this.uId + '/' + this.evaluationData[index].tId)
    },
    getStat (index) {
      this.$router.push('/EvaluationStat/' + this.evaluationData[index].tId)
    },
    editJudge (index) {
      this.$router.push('/AddJudge/' + this.evaluationData[index].tId)
    },
    cancel () {
      this.$Message.info('您已取消')
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

.top {
  padding: 10px;
  background: rgba(0, 153, 229, .7);
  color: #fff;
  text-align: center;
  border-radius: 2px;
  margin-right: 60px;
}
</style>
