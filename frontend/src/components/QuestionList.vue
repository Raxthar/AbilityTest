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
        <Button :size="buttonSize" type="primary" @click="jumpToAddQuestion">
          创建题目
        </Button>
      </Content>
      <Footer>
        <card>
          <Content>
            <Table border :columns="columns" :data="questionData">
            </Table>
          </Content>
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
    this.searchQuestion()
  },
  data () {
    return {
      uId: this.$route.params.uId,
      tId: this.$route.params.tId,
      questionId: [],
      questionName: [],
      columns: [
        {
          title: '题号',
          key: 'qId'
        },
        {
          title: '题目',
          key: 'qName'
        },
        {
          title: '操作',
          key: 'action',
          width: 150,
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
      questionData: [],
      buttonSize: 'large'
    }
  },
  methods: {
    jumpBack () {
      this.$router.push('/CreateEvaluation/')
    },
    jumpToAddQuestion () {
      this.$router.push('/AddQuestion/' + this.uId + '/' + this.tId)
    },
    searchQuestion () {
      this.$axios.get('search_all_questions', {
        params: {
          tId: this.tId
        }
      }).then(response => {
        if (response.data.code === 200) {
          if (response.data.questionId.length > 0) {
            this.questionData = []
            this.questionId = response.data.questionId
            this.questionName = response.data.questionName
            for (let i = 0; i < response.data.questionId.length; i++) {
              let obj = {
                qId: this.questionId[i],
                qName: this.questionName[i]
              }
              this.questionData.push(obj)
            }
          }
        } else {
          this.$Message.error('无法读取数据库！')
        }
      })
    },
    questionEdit (index) {
      let qId = this.questionData[index].qId
      this.$router.push('/QuestionEdit/' + this.uId + '/' + this.tId + '/' + qId)
    },
    deleteQuestion (index) {
      this.$axios.post('/delete_question/', JSON.stringify(this.questionData[index])).then(response => {
        if (response.data.code === 200) {
          this.$Message.success(`删除 ${this.questionData[index].qName} 成功！`)
          this.questionData.splice(index, 1)
        } else {
          this.$Message.error('无法读取数据库！')
        }
      })
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
