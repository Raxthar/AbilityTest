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
        <Card>
          <Button :size="buttonSize" type="primary" @click="addDimension" id = "addButton">添加维度</Button>
          <Button :size="buttonSize" type="primary" @click="delDimension" id = "delButton">删除维度</Button><br><br>
          <Form :model="dimensions">
            <FormItem v-for="(list, index) in dimensionArray.dimensions.slice(0,4)" :key="(list, index)">
              <Input v-model="list.dName" size="large" placeholder="请输入维度" />
            </FormItem>
              <Button type="primary" class="submit-button" @click="updateDimensions" id="updateButton">提交</Button>
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
      dimensionArray: {
        tId: this.$route.params.tId,
        uId: this.$route.params.uId,
        dimensions: [{
          dName: ''
        }]
      }
    }
  },
  methods: {
    jumpBack () {
      this.$router.push('/EvaluationEdit/' + this.dimensionArray.uId + '/' + this.dimensionArray.tId)
    },
    addDimension: function () {
      if (this.dimensionArray.dimensions.length < 4) {
        let cope = {
          dName: ''
        }
        this.dimensionArray.dimensions.push(cope)
      } else {
        return
      }
    },
    delDimension: function () {
      let count = this.dimensionArray.dimensions.length - 1
      this.dimensionArray.dimensions.splice(count, 1)
    },
    updateDimensions: function () {
      for (let i = 0; i < this.dimensionArray.dimensions.length; i++) {
        if (this.dimensionArray.dimensions[i].dName === '') {
          this.$Message.info('请输入维度名')
          return
        }
      }
      this.$axios.post('/create_dimension/', JSON.stringify(this.dimensionArray)).then(response => {
        if (response.data.code === 200) {
          this.$Message.success(`设置维度成功`)
          this.$router.push('/QuestionList/' + this.dimensionArray.uId + '/' + this.dimensionArray.tId)
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
