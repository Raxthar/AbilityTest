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
                  <Input v-model="questionData.qName" placeholder="Enter Title..." />
              </FormItem>
              <FormItem v-for="(list, index) in lists.slice(0,4)" :key="(list, index)">
                  <Input v-model="questionData.oName[index]" size="large" placeholder="请输入选项" />
                  <InputNumber v-model="questionData.score[index]" size="small" placeholder="请输入分数" />
                  <RadioGroup v-model="questionData.dId[index]" type="button" name=index>
                    <Radio v-for="dimensions in dimensionsData" :key="dimensions" :label=dimensions.dId>{{dimensions.dName}}</Radio>
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
      uId: this.$route.params.uId,
      lists: [{
        index: {}
      }],
      dimensionsData: [],
      dimensionId: [],
      dimensionName: [],
      questionData: {
        tId: this.$route.params.tId,
        qName: '',
        oName: {},
        dId: {},
        score: {}
      }
    }
  },
  methods: {
    jumpBack () {
      this.$router.push('/QuestionList/' + this.uId + '/' + this.tId)
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
          content: this.questionData.tId
        }
      }).then(dimension => {
        if (dimension.data.code === 200) {
          if (dimension.data.dId.length > 0) {
            this.dimensionsData = []
            this.dimensionId = dimension.data.dId
            this.dimensionName = dimension.data.dName
            for (let i = 0; i < dimension.data.dId.length; i++) {
              let obj = {
                dName: this.dimensionName[i],
                dId: this.dimensionId[i]
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
      if (this.questionData.qName === '') {
        this.$Message.error('please enter question')
        return
      }
      for (let i = 0; i < this.lists.length; i++) {
        if (!this.questionData.dId[i]) {
          this.$Message.error('please choose a dimension for option')
          return
        } else if (!this.questionData.oName[i]) {
          this.$Message.error('please enter option')
          return
        } else if (!this.questionData.score[i]) {
          this.questionData.score[i] = 1
        }
      }
      this.$axios.post('/add_question/', JSON.stringify(this.questionData)).then(response => {
        if (response.data.code === 200) {
          this.$Message.success(`set questions success`)
          this.$router.push('/QuestionList/' + this.uId + '/' + this.questionData.tId)
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
