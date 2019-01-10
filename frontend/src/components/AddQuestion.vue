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
      </Content>
      <Footer>
        <card>
          <Content>
            <Form :model="questionData">
              <FormItem label="input">
                  <Input v-model="questionData.q_name" placeholder="Enter Title..." />
              </FormItem>
              <FormItem v-for="(list, index) in lists.slice(0,4)" :key="(list, index)">
                  <Input v-model="questionData.o_name[index]" size="large" placeholder="请输入选项" />
                  <Input v-model="questionData.score[index]" size="small" placeholder="请输入分数" />
                  <RadioGroup type="button" v-model="questionData.d_id[index]">
                    <Radio v-for="dimensions in dimensionsData" :key="dimensions" :label="dimensions.d_id">{{dimensions.d_name}}</Radio>
                  </RadioGroup>
              </FormItem>
              <Button type="primary" class="submit-button" @click="setQuestion">提交</Button>
            </Form>
            <Button :size="buttonSize" type="primary" @click="addOption">添加选项</Button><br><br>
            <Button :size="buttonSize" type="primary" @click="delOption">删除选项</Button><br><br>
          </Content>
        </card>
      </Footer>
    </Layout>
  </div>
</template>
<script>
export default {
  mounted () {
    this.searchDimension()
  },
  data () {
    return {
      u_id: this.$route.params.u_id,
      lists: [{
        index: {}
      }],
      dimensionsData: [],
      dimension_id: [],
      dimension_name: [],
      questionData: {
        t_id: this.$route.params.t_id,
        q_name: '',
        o_name: {},
        d_id: {},
        score: {}
      }
    }
  },
  methods: {
    jumpBack () {
      this.$router.push('/QuestionList/' + this.u_id + '/' + this.t_id)
    },
    addOption: function () {
      let cope = {
        index: ''
      }
      this.lists.push(cope)
    },
    delOption: function (index) {
      this.lists.splice(index, 1)
    },
    searchDimension () {
      this.$axios.get('search_dimensions', {
        params: {
          content: this.questionData.t_id
        }
      }).then(dimension => {
        if (dimension.data.code === 200) {
          if (dimension.data.d_id.length > 0) {
            this.dimensionsData = []
            this.dimension_id = dimension.data.d_id
            this.dimension_name = dimension.data.d_name
            for (let i = 0; i < dimension.data.d_id.length; i++) {
              let obj = {
                d_name: this.dimension_name[i],
                d_id: this.dimension_id[i]
              }
              this.dimensionsData.push(obj)
            }
          }
        } else {
          this.$Message.error(`can't search in database`)
        }
      })
    },
    setQuestion () {
      for (let i = 0; i < this.lists.length; i++) {
        if (this.questionData.d_id[i] === 0) {
          this.$Message.info('please choose a dimension for option')
          return
        }
        if (!this.questionData.q_name[i]) {
          this.$Message.info('please enter question')
          return
        }
        if (!this.questionData.score[i]) {
          this.$Message.info('please enter the score for question')
          return
        }
      }
      this.$axios.post('/add_question/', JSON.stringify(this.questionData)).then(response => {
        if (response.data.code === 200) {
          this.$Message.success(`set questions success`)
          this.$router.push('/QusetionList/' + this.u_id + '/' + this.questionData.t_id)
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