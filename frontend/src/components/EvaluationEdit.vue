<template>
  <div class="layout">
    <Layout>
      <Header>
        <Button :size="buttonSize" type="Default" @click="jumpBack" id="backButton">
          <Icon type="ios-arrow-back" />
          返回
        </Button>
      </Header>
      <Content>
        <Card>
          <Form :model="evaluationData">
            <p>测评标题</p>
            <Input placeholder="请输入测评标题" style="width: 600px"  v-model="evaluationData.evaluationName"/><br><br><br><br>
            <p>测评描述</p>
            <Input type="textarea" :rows="4" style="width: 600px" placeholder="请输入测评描述"  v-model="evaluationData.evaluationDescribe"/><br><br><br><br>
            <Button :size="buttonSize" type="primary" shape="circle" @click="editEvaluation" id="submitButton">提交</Button>
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
      uId: this.$route.params.uId,
      tId: this.$route.params.tId,
      evaluationData: {
        tId: this.$route.params.tId,
        evaluationName: '',
        evaluationDescribe: ''
      }
    }
  },
  methods: {
    jumpBack () {
      this.$router.push('/CreateEvaluation/')
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
          this.$Message.error(`无法读取数据库`)
        }
      })
    },
    editEvaluation () {
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
          this.$router.push('/DimensionsEdit/' + this.uId + '/' + this.tId)
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

p {
  font-size: 22px;
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
