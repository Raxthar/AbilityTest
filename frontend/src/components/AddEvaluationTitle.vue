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
          <Form :model="createData">
            <p class="title-text">测评标题</p>
            <Input placeholder="请输入测评标题" style="width: 600px"  v-model="createData.tName" id="createTitle"/><br><br><br><br>
            <p class="title-text">测评描述</p>
            <Input type="textarea" :rows="4" style="width: 600px" placeholder="请输入测评描述"  v-model="createData.tDescribe" id="createDesc"/><br><br><br><br>
            <Button :size="buttonSize" type="primary" shape="circle" @click="handleCreate" id="submitButton">创建测评</Button>
          </Form>
        </Card>
      </Content>
    </Layout>
  </div>
</template>

<script>
export default {
  data () {
    return {
      buttonSize: 'large',
      createData: {
        uId: this.$route.params.uId,
        tName: '',
        tDescribe: ''
      }
    }
  },
  methods: {
    jumpBack () {
      this.$router.push('/CreateEvaluation/')
    },
    handleCreate () {
      if (this.createData.tName === '') {
        this.$Message.info('请输入标题')
        return
      }
      if (this.createData.tDescribe === '') {
        this.$Message.info('请输入描述')
        return
      }
      this.$axios.post('/create/', JSON.stringify(this.createData)).then(response => {
        if (response.data.code === 200) {
          this.$Message.success(`创建${this.createData.tName} 成功`)
          let tId = response.data.tId
          this.$router.push('/AddDimensions/' + this.createData.uId + '/' + tId)
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
  background-color: rgb(97, 176, 255)
}

.ivu-layout-content {
  height: 100vmin;
}

.ivu-btn-primary {
  background-color: rgb(97, 176, 255);
  border-color: rgb(97, 176, 255);
}

.ivu-btn-large {
  font-size: 18px;
}

.ivu-layout-header {
  padding: 0 20px;
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

.ivu-input-wrapper {
    width: 50%;
}

.ivu-card-bordered {
    border: 1px solid #f9f9fa;
    border-color: #fafafa;
}
</style>
