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
            <Table :data="questionData">
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
      uID: this.$route.params.uID,
      tID: this.$route.params.tID,
      columns: [
        {
          title: '题号',
          key: 'qID'
        },
        {
          title: '题目',
          key: 'qName'
        }
      ],
      questionData: [],
      buttonSize: 'large'
    }
  },
  methods: {
    jumpToAddQuestion () {
      this.$router.push('/AddQuestion/' + this.uID + '/' + this.tID)
    },
    searchQuestion () {
      this.$axios.get('searchQuestion', {
        params: {
          content: this.tID
        }
      }).then(response => {
        if (response.data.code === 200) {
          if (response.data.data && JSON.parse(response.data.data).length > 0) {
            this.questionData = []
            let questions = JSON.parse(response.data.data)
            for (let i in questions) {
                let obj = {
                  qID: questions[i].fields.qID,
                  qName: questions[i].fields.qName,
                }
              this.questionData.push(obj)
            }
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