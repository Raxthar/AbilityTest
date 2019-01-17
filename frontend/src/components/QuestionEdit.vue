<template>
  <div class="layout">
    <Layout>
      <Header>
        <Button :size="buttonSize" type="primary" @click="jumpBack">
          <Icon type="ios-arrow-back" />
          返回
        </Button>
      </Header>
      <Footer>
        <card>
          <Content>
            <Form :model="questionData">
              <FormItem label=""><br>
                  <Input v-model="questionData.newQuestionName" size="large" style="width: 600px" placeholder="请输入题目名" />
              </FormItem>
              <FormItem v-for="(options, index) in questionData.newOptionData" :key="(options, index)">
                  <Input v-model="questionData.newOptionData[index].oName" style="width: 600px" placeholder="请输入选项" /><br>
                  <InputNumber v-model="questionData.newOptionData[index].score" size="small" placeholder="请输入分数" />
                  <RadioGroup v-model="questionData.newOptionData[index].dId" type="button">
                    <Radio v-for="item in dimensionsData" :key="item" :label=item.dId>{{item.dName}}</Radio>
                  </RadioGroup>
              </FormItem>
              <Button type="primary" class="submit-button" @click="editQuestion">提交</Button>
            </Form>
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
    this.searchDimension()
    this.searchQuestion()
  },
  data () {
    return {
      uId: this.$route.params.uId,
      tId: this.$route.params.tId,
      buttonSize: 'large',
      lists: [{
        list: ''
      }],
      oldOptionData: [],
      dimensionsData: [],
      dimensionId: [],
      dimensionName: [],
      oldQuestionName: '',
      questionData: {
        qId: this.$route.params.qId,
        newQuestionName: '',
        newOptionData: []
      }
    }
  },
  methods: {
    jumpBack () {
      this.$router.push('/QuestionList/' + this.uId + '/' + this.tId)
    },
    searchDimension () {
      this.$axios.get('search_dimensions', {
        params: {
          content: this.tId
        }
      }).then(dimension => {
        if (dimension.data.code === 200) {
          if (dimension.data.dId.length > 0) {
            this.dimensionsData = []
            this.dimensionId = dimension.data.dId
            this.dimensionName = dimension.data.dName
            for (let i = 0; i < this.dimensionId.length; i++) {
              let obj = {
                dName: this.dimensionName[i],
                dId: this.dimensionId[i]
              }
              console.log(obj.dName)
              this.dimensionsData.push(obj)
            }
          }
        } else {
          this.$Message.error(`无法读取数据库`)
        }
      })
    },
    searchQuestion () {
      this.$axios.get('edit_question', {
        params: {
          qId: this.questionData.qId
        }
      }).then(message => {
        if (message.data.code === 200) {
          if (message.data.oName.length > 0) {
            this.$Message.info(`can't ${message.data.oName} database`)
            this.oldOptionData = []
            let questionName = message.data.qName
            this.oldQuestionName = questionName
            let optionName = message.data.oName
            let dimensionName = message.data.dName
            let scoreData = message.data.score
            let dimensionId = message.data.dId
            for (let i = 0; i < message.data.oName.length; i++) {
              let obj = {
                oName: optionName[i],
                score: scoreData[i],
                dId: dimensionId[i]
              }
              this.oldOptionData.push(obj)
            }
            this.questionData.newOptionData = this.oldOptionData
            this.questionData.newQuestionName = this.oldQuestionName
            for (let i = 0; i < dimensionName.length; i++) {
              let obj = {
                dName: dimensionName[i],
                dId: dimensionId[i]
              }
              this.dimensionsData.push(obj)
            }
          }
        } else {
          this.$message.error(`无法读取数据库`)
        }
      })
    },
    editQuestion () {
      for (let i = 0; i < this.questionData.newOptionData.length; i++) {
        if (this.questionData.newOptionData[i].oName === '') {
          this.$Message.info('请输入选项内容')
          return
        }
        if (this.questionData.newOptionData[i].dId === 0) {
          this.$Message.info('请选择维度')
          return
        }
        if (this.questionData.newOptionData[i].score <= 0) {
          this.$Message.error('选项分数应该大于0')
          return
        }
      }
      this.$axios.post('/update_question/', JSON.stringify(this.questionData)).then(response => {
        if (response.data.code === 200) {
          this.$Message.success(`编辑题目成功`)
          this.$router.push('/QuestionList/' + this.uId + '/' + this.tId)
        } else {
          this.$Message.error('无法读取数据库')
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
