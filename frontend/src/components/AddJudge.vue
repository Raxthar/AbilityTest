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
          <Form :model="dimensions">
            <FormItem v-for="(list, index) in judges.dimensionName" :key="(list, index)">
              <p>{{judges.dimensionName[index]}}
              <Input v-model="judges.judge[index]" size="large" placeholder="请输入评价" /></p>
            </FormItem><br><br><br>
            <p>截止日期</p>
            <DatePicker type="date" placeholder="Select date" style="width: 200px" v-model="judges.due"></DatePicker>
              <Button type="primary" class="submit-button" @click="editJudge" id="submitButton">提交</Button>
          </Form>
        </Card>
      </Content>
    </Layout>
  </div>
</template>

<script>
export default {
  mounted () {
    this.searchDimension()
    this.searchJudge()
  },
  data () {
    return {
      buttonSize: 'large',
      tId: this.$route.params.tId,
      judges: {
        dimensionId: [],
        dimensionName: [],
        judge: [],
        due: '',
        tId: this.$route.params.tId
      }
    }
  },
  methods: {
    jumpBack () {
      this.$router.push('/CreateEvaluation/')
    },
    searchDimension () {
      this.$axios.get('search_dimensions', {
        params: {
          content: this.tId
        }
      }).then(dimension => {
        if (dimension.data.code === 200) {
          if (dimension.data.dId.length > 0) {
            this.judges.dimensionId = dimension.data.dId
            this.judges.dimensionName = dimension.data.dName
          }
        } else {
          this.$Message.error(`无法读取数据库`)
        }
      })
    },
    searchJudge () {
      this.$axios.get('search_judge', {
        params: {
          tId: this.tId
        }
      }).then(response => {
        if (response.data.code === 200) {
          if (response.data.jContent.length > 0) {
            this.judges.judge = response.data.jContent
            this.judges.due = response.data.due
          }
        } else {
          this.$Message.error(`无法读取数据库`)
        }
      })
    },
    editJudge () {
      this.$axios.post('/edit_judge/', JSON.stringify(this.judges)).then(response => {
        if (response.data.code === 200) {
          this.$Message.success(`设置评价成功`)
          this.$router.push('/CreateEvaluation/')
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
  font-family: 楷体;
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
