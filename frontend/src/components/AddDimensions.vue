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
  data () {
    return {
      buttonSize: 'large',
      lists: [{
        getdimension: ''
      }],
      dimensionArray: {
        tID: this.$route.params.tID,
        uID: this.$route.params.uID,
        dimensions: {}
      }
    }
  },
  methods: {
    addDimension: function () {
      let cope = {
        index: ''
      }
      this.lists.push(cope)
    },
    delDimension: function (index) {
      this.lists.splice(index, 1)
    },
    setDimensions: function () {
      for (let i = 0; i < this.dimensionArray.dimensions.length; i++) {
        if (this.dimensionArray.dimensions[i] === '') {
          this.$Message.info('please input evaluation dimensions')
          return
        }
      }
      this.$axios.post('/dimension/', JSON.stringify(this.dimensionArray)).then(res => {
        if (res.data.code === 200) {
          this.$Message.success(`set dimensions success`)
          this.$router.push({name: 'HelloWorld'})
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
    width: 100px;
}

.ivu-card-bordered {
  border: 1px solid #f9f9fa;
  border-color: #fafafa;
}

.submit-button {
  background-color: rgb(97, 176, 255);
  border-color: rgb(97, 176, 255);
  font-size: 18px;
  width: 10%;
}
</style>
