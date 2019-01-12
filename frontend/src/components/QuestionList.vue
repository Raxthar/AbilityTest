<template>
  <div class="layout">
    <Layout>
      <Header>
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
          title: 'Action',
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
                    this.questionView(params.index)
                  }
                }
              }, 'View'),
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
              }, 'Edit'),
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
              }, 'Delete')
            ])
          }
        }
      ],
      questionData: [],
      buttonSize: 'large'
    }
  },
  methods: {
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
          this.$Message.error(`can't search in database`)
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
          this.$Message.success(`delete ${this.questionData[index].qName} success`)
          this.questionData.splice(index, 1)
        } else {
          this.$Message.info("can't read database")
        }
      })
    },
    questionView (index) {
      this.$axios.get('edit_question', {
        params: {
          qId: this.questionData[index].qId
        }
      }).then(message => {
        if (message.data.code === 200) {
          if (message.data.oName.length > 0) {
            let theQuestionData
            let questionName = message.data.qName
            let optionName = message.data.oName
            let dimensionName = message.data.dName
            let scoreData = message.data.score
            for (let i = 0; i < message.data.oName.length; i++) {
              let obj = {
                oName: optionName[i],
                score: scoreData[i],
                dName: dimensionName[i]
              }
              theQuestionData.push(obj)
            }
            this.$Modal.info({
              title: 'Question Info',
              content: `Question：${questionName}<br>Options：${theQuestionData}`
            })
          }
        } else {
          this.$message.error(`can't search in database`)
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
