<template>
  <div class="layout">
    <Layout>
      <Header>
        <Button :size="buttonSize" type="primary" to="/HelloWorld">
          <Icon type="ios-arrow-back" />
          返回
        </Button>
      </Header>
      <Content>
        <Card>
          <Form :model="createData">
            <p class="title-text">测评标题</p>
            <Input placeholder="Enter title" style="width: 300px"  v-model="createData.title"/><br><br>
            <p class="title-text">测评描述</p>
            <Input type="textarea" :rows="4" placeholder="Enter describe"  v-model="createData.describe"/><br><br>
            <Button :size="buttonSize" type="primary" shape="circle" @click="handleCreate">创建测评</Button>
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
        title: '',
        describe: ''
      }
    }
  },
  methods: {
    handleCreate () {
      if (this.createData.title === '') {
        this.$Message.info('请输入标题')
        return
      }
      if (this.createData.describe === '') {
        this.$Message.info('请输入描述')
        return
      }
      this.$axios.post('/create/', JSON.stringify(this.createData)).then(res => {
        if (res.data.code === 200) {
          this.$Message.success(`create ${this.createData.title} success`)
          this.$router.push({name: 'AddDimensions'})
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

.title-text {
  font-family: "Helvetica Neue";
  font-size: 20px;
}

.ivu-input-wrapper {
    width: 50%;
}

.ivu-card-bordered {
    border: 1px solid #f9f9fa;
    border-color: #fafafa;
}
</style>
