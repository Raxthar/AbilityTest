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
          <Button :size="buttonSize" type="primary" @click="addDimension">添加维度</Button><br><br>
          <Button :size="buttonSize" type="primary" @click="delDimension">删除维度</Button><br><br>
          <Form :model="dimensions">
            <FormItem v-for="(list, index) in dimensions.dimensionName" :key="(list, index)">
              <Input v-model="dimensions.dimensionName[index]" size="large" placeholder="请输入维度" />
            </FormItem>
              <Button type="primary" class="submit-button" @click="editDimension">提交</Button>
          </Form>
        </Card>
      </Content>
    </Layout>
  </div>
</template>

<script>
export default {
  mounted () {
    this.searchDimensions()
  },
  data () {
    return {
      buttonSize: 'large',
      uId: this.$route.params.uId,
      dimensions: {
        dimensionId: [],
        dimensionName: [],
        tId: this.$route.params.tId
      }
    }
  },
  methods: {
    jumpBack () {
      this.$router.push('/EvaluationEdit/' + this.uId + '/' + this.dimensions.tId)
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
    searchDimensions () {
      this.$axios.get('search_dimensions', {
        params: {
          content: this.dimensions.tId
        }
      }).then(response => {
        if (response.data.code === 200) {
          if (response.data.dId.length > 0) {
            this.dimensions.dimensionId = response.data.dId
            this.dimensions.dimensionName = response.data.dName
          }
        } else {
          this.$Message.error(`无法读取数据库！`)
        }
      })
    },
    editDimension () {
      this.$axios.post('/update_dimension/', JSON.stringify(this.dimensions)).then(response => {
        if (response.data.code === 200) {
          this.$Message.success(`修改测评成功！`)
          this.$router.push('/QuestionList/' + this.uId + '/' + this.dimensions.tId)
        } else {
          this.$Message.error('无法读取数据库！')
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
</style>
