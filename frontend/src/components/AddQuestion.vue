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
            <Button :size="buttonSize" type="primary" @click="addOption">添加选项</Button>
            <Button :size="buttonSize" type="primary" @click="delOption">删除选项</Button><br><br>
            <Form :model="questionData">
              <FormItem label="input"><br>
                  <Input v-model="questionData.qName" size="large" style="width: 600px" placeholder="请输入题目名" />
              </FormItem>
              <FormItem v-for="(list, index) in lists" :key="(list, index)">
                  <Input v-model="questionData.oName[index]" style="width: 600px" placeholder="请输入选项" /><br>
                  <InputNumber v-model="questionData.score[index]" size="small" placeholder="请输入分数" />
                  <RadioGroup v-model="questionData.dId[index]" type="button" name=index>
                    <Radio v-for="dimensions in dimensionsData" :key="dimensions" :label=dimensions.dId>{{dimensions.dName}}</Radio>
                  </RadioGroup>
              </FormItem>
              <Button type="primary" class="submit-button" @click="setQuestion">提交</Button>
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
  },
  data () {
    return {
      buttonSize: 'large',
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
      this.$router.push('/QuestionList/' + this.uId + '/' + this.questionData.tId)
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
          this.$Message.error(`无法读取数据库`)
        }
      })
    },
    setQuestion () {
      if (this.questionData.qName === '') {
        this.$Message.error('请输入题目名')
        return
      }
      for (let i = 0; i < this.lists.length; i++) {
        if (!this.questionData.dId[i]) {
          this.$Message.error('请为选项选择关联维度')
          return
        } else if (!this.questionData.oName[i]) {
          this.$Message.error('请输入选项内容')
          return
        } else if (!this.questionData.score[i]) {
          this.questionData.score[i] = 1
        } else if (this.questionData.score[i] <= 0) {
          this.$Message.error('选项分数应该大于0')
          return
        }
      }
      this.$axios.post('/add_question/', JSON.stringify(this.questionData)).then(response => {
        if (response.data.code === 200) {
          this.$Message.success(`添加题目成功`)
          this.$router.push('/QuestionList/' + this.uId + '/' + this.questionData.tId)
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
