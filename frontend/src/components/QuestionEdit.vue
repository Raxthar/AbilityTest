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
                  <Input v-model="questionData.new_q_name" placeholder="Enter Title..." />
              </FormItem>
              <FormItem v-for="(options, index) in questionData.newOptionData" :key="(options, index)">
                  <Input v-model="questionData.newOptionData[index].o_name" size="large" placeholder="请输入选项" />
                  <InputNumber v-model="questionData.newOptionData[index].score" size="small" placeholder="请输入分数" />
                  <RadioGroup v-model="questionData.newOptionData[index].d_id" type="button">
                    <Radio v-for="(dimension, item) in dimensionsData" :key="(dimension, item)" :label=dimensionsData[item].d_id>{{dimensionsData[item].d_name}}</Radio>
                  </RadioGroup>
              </FormItem>
              <Button type="primary" class="submit-button" @click="editQuestion">提交</Button>
            </Form>
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
    this.searchQuestion()
  },
  data () {
    return {
      u_id: this.$route.params.u_id,
      t_id: this.$route.params.t_id,
      buttonSize: 'large',
      lists: [{
        list: ''
      }],
      oldOptionData: [],
      dimensionsData: [],
      dimension_id: [],
      dimension_name: [],
      old_q_name: '',
      questionData: {
        q_id: this.$route.params.q_id,
        new_q_name: '',
        newOptionData: []
      }
    }
  },
  methods: {
    jumpBack () {
      this.$router.push('/QuestionList/' + this.t_id + '/' + this.u_id)
    },
    searchDimension () {
      this.$axios.get('search_dimensions', {
        params: {
          content: this.t_id
        }
      }).then(dimension => {
        if (dimension.data.code === 200) {
          if (dimension.data.d_id.length > 0) {
            this.dimensionsData = []
            this.dimension_id = dimension.data.d_id
            this.dimension_name = dimension.data.d_name
            for (let i = 0; i < this.dimension_id.length; i++) {
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
    searchQuestion () {
      this.$axios.get('edit_question', {
        params: {
          q_id: this.questionData.q_id
        }
      }).then(message => {
        if (message.data.code === 200) {
          if (message.data.o_name.length > 0) {
            this.$Message.info(`can't ${message.data.o_name} database`)
            this.oldOptionData = []
            let questionName = message.data.q_name
            this.old_q_name = questionName
            let optionName = message.data.o_name
            let dimensionName = message.data.d_name
            let scoreData = message.data.score
            let dimensionId = message.data.d_id
            for (let i = 0; i < message.data.o_name.length; i++) {
              let obj = {
                o_name: optionName[i],
                score: scoreData[i],
                d_id: dimensionId[i]
              }
              this.oldOptionData.push(obj)
            }
            this.questionData.newOptionData = this.oldOptionData
            this.questionData.new_q_name = this.old_q_name
            for (let i = 0; i < dimensionName.length; i++) {
              let obj = {
                d_name: dimensionName[i],
                d_id: dimensionId[i]
              }
              this.dimensionsData.push(obj)
            }
          }
        } else {
          this.$message.error(`can't search in database`)
        }
      })
    },
    editQuestion () {
      for (let i = 0; i < this.questionData.newOptionData.length; i++) {
        if (this.questionData.newOptionData[i].o_name === '') {
          this.$Message.info('请输入选项内容')
          return
        }
        if (this.questionData.newOptionData[i].d_id === 0) {
          this.$Message.info('请选择维度')
          return
        }
        if (this.questionData.newOptionData[i].score === 0) {
          this.$Message.info('请确定选项分数')
          return
        }
      }
      this.$axios.post('/update_question/', JSON.stringify(this.questionData)).then(response => {
        if (response.data.code === 200) {
          this.$Message.success(`edit questions success`)
          this.$router.push('/QuestionList/' + this.u_id + '/' + this.t_id)
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
