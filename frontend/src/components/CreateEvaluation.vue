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
      u_id: 1,
      columns: [
        {
          title: '测评号',
          key: 't_id',
          width: 150
        },
        {
          title: '测评名',
          key: 't_name',
          width: 200
        },
        {
          title: '测评状态',
          key: 't_status',
          width: 150
        },
        {
          title: '截止日期',
          key: 't_due',
          width: 200
        },
        {
          title: '操作',
          key: 'action',
          //width: 150,
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
                    this.questionEdit(params.index)
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
                    this.questionEdit(params.index)
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
                    this.deleteQuestion(params.index)
                  }
                }
              }, '删除')
            ])
          }
        }
      ],
      evaluationData: [],
      t_id: [],
      t_name: [],
      t_due: [],
      t_status: [],
      buttonSize: 'large'
    }
  },
  methods: {
    jumpToAddTitle () {
      this.$router.push('/AddEvaluationTitle/' + this.u_id)
    },
    jumpToAddTitle () {
      this.$router.push('/AddEvaluationTitle/' + this.u_id)
    },
    searchEvaluation () {
      this.$axios.get('test_list', {
        params: {
          u_id: this.u_id
        }
      }).then(test_message => {
        if (test_message.data.code === 200) {
          if (test_message.data.t_name.length > 0) {
            this.evaluationData = []
            this.t_id = test_message.data.t_id
            this.t_name = test_message.data.t_name
            this.t_due = test_message.data.t_due
            this.t_status = test_message.data.t_status
            for (let i = 0; i < test_message.data.t_name.length; i++) {
              let t_status = this.t_status[i]
              if (t_status === 1){
                let obj = {
                  t_id: this.t_id[i],
                  t_name: this.t_name[i],
                  t_status: '已发布',
                  t_due: this.t_due[i]
                }
                this.evaluationData.push(obj)
              } else if (t_status === 0) {
                let obj = {
                  t_id: this.t_id[i],
                  t_name: this.t_name[i],
                  t_status: '未发布',
                  t_due: this.t_due[i]
                }
                this.evaluationData.push(obj)
              }
            }
            this.$Message.info(`Create ${this.evaluationData[0].t_name} Success`)
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
