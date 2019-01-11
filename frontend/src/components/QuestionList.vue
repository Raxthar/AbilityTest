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
      u_id: this.$route.params.u_id,
      t_id: this.$route.params.t_id,
      question_id: [],
      question_name: [],
      columns: [
        {
          title: '题号',
          key: 'q_id'
        },
        {
          title: '题目',
          key: 'q_name'
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
      this.$router.push('/AddQuestion/' + this.u_id + '/' + this.t_id)
    },
    searchQuestion () {
      this.$axios.get('search_all_questions', {
        params: {
          t_id: this.t_id
        }
      }).then(response => {
        if (response.data.code === 200) {
          if (response.data.question_id.length > 0) {
            this.questionData = []
            this.question_id = response.data.question_id
            this.question_name = response.data.question_name
            for (let i = 0; i < response.data.question_id.length; i++) {
              let obj = {
                q_id: this.question_id[i],
                q_name: this.question_name[i]
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
      let q_id = this.questionData[index].q_id
      this.$router.push('/QuestionEdit/' + this.u_id + '/' + this.t_id + '/' + q_id)
    },
    deleteQuestion (index) {
      this.$axios.post('/delete_question/', JSON.stringify(this.questionData[index])).then(response => {
        if (response.data.code === 200) {
          this.$Message.success(`delete ${this.questionData[index].q_name} success`)
          this.questionData.splice(index, 1)
        } else {
          this.$Message.info("can't read database")
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