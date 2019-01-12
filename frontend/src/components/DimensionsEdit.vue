<template>
  <div class="layout">
    <Layout>
      <Header>
        <Button :size="buttonSize" type="primary" to="/AddEvaluationTitle">
          <Icon type="ios-arrow-back" />
          返回
        </Button>
      </Header>
      <Content>
        <Card>
          <Button :size="buttonSize" type="primary" @click="addDimension">添加维度</Button><br><br>
          <Button :size="buttonSize" type="primary" @click="delDimension">删除维度</Button><br><br>
          <Form :model="dimensions">
            <FormItem v-for="(list, index) in lists.slice(0,4)" :key="(list, index)">
              <Input v-model="dimensionArray.dimensions[index]" size="large" placeholder="请输入维度" />
            </FormItem>
              <Button type="primary" class="submit-button" @click="setDimensions">提交</Button>
          </Form>
        </Card>
      </Content>
    </Layout>
  </div>
</template>

<script>
export default {
  mounted () {
    this.searchEvaluation()
  },
  data () {
    return {
      buttonSize: 'large',
      lists: [{
        index: {}
      }],
      dimensionArray: {
        tId: this.$route.params.tId,
        uId: this.$route.params.uId,
        dimensions: {}
      }
    }
  },
  methods: {
    jumpBack () {
      this.$router.push('/CreateEvaluation/' + this.uId + '/' + this.tId)
    },
    addDimension: function () {
      let cope = {
        index: ''
      }
      this.lists.push(cope)
    },
    delDimension: function (index) {
      this.lists.splice(index, 1)
    },
    searchEvaluation () {
      this.$axios.get('search_atest_by', {
        params: {
          tId: this.tId
        }
      }).then(response => {
        if (response.data.code === 200) {
          this.evaluationData.evaluationName = response.data.tName
          this.evaluationData.evaluationDescribe = response.data.tDescribe
        } else {
          this.$Message.error(`can't search in database`)
        }
      })
    },
    editQuestion () {
      if (this.evaluationData.evaluationName === '') {
        this.$Message.info('请输入测评标题')
        return
      }
      if (this.evaluationData.evaluationDescribe === '') {
        this.$Message.info('请输入测评描述')
        return
      }
      this.$axios.post('/update_atest/', JSON.stringify(this.evaluationData)).then(response => {
        if (response.data.code === 200) {
          this.$Message.success(`修改测评成功`)
          this.$router.push('/QuestionList/' + this.uId + '/' + this.tId)
        } else {
          this.$Message.info("can't read database!")
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
