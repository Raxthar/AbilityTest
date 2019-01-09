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
          render: (h, params) => {
            return h('div', [
              h('Button', {
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
              }, 'View')
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
      this.$axios.get('searchQuestion', {
        params: {
          content: this.t_id
        }
      }).then(response => {
        if (response.data.code === 200) {
          if (response.data.data && JSON.parse(response.data.data).length > 0) {
            this.questionData = []
            let questions = JSON.parse(response.data.data)
            for (let i in questions) {
                let obj = {
                  q_id: questions[i].fields.q_id,
                  q_name: questions[i].fields.q_name,
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
      this.$router.push('/QuestionEdit/' + this.t_id + '/' + this.questionData[index].q_id)
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