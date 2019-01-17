<template>
  <div>
    <i-message id="message" />
    <form :model="titleData">
      <p class="title-text">测评标题</p>
      <input placeholder="Enter title" style="width: 300px"  v-model="titleData.evaluationName"/><br><br>
      <p class="title-text">测评描述</p>
      <input type="textarea" :rows="4" placeholder="Enter describe"  v-model="titleData.evaluationDescribe"/><br><br>
      <i-button :size="buttonSize" type="primary" shape="circle" @click="editEvaluation">提交</i-button>
    </form>
  </div>
</template>

<script>
import {$Message} from '../../../static/iview/base/index'
export default {
  mounted () {
    this.uId = this.$root.$mp.query.uId
    this.titleData.tId = this.$root.$mp.query.tId
    this.searchEvaluation()
  },
  data () {
    return {
      buttonSize: 'large',
      uId: 1,
      tId: 1,
      titleData: {
        tId: 1,
        evaluationName: '',
        evaluationDescribe: ''
      }
    }
  },
  methods: {
    searchEvaluation () {
      let list = this.titleData
      wx.request({
        url: 'http://127.0.0.1:8000/search_atest_by/',
        data: {
          tId: this.titleData.tId
        },
        success  (response) {
          if (response.data.code === 200) {
            if (response.data.tName.length > 0) {
              list.evaluationName = response.data.tName
              list.evaluationDescribe = response.data.tDescribe
            }
          } else {
            $Message({
              content: '查找失败！',
              type: 'error'
            })
          }
        }
      })
      this.titleData = list
    },
    editEvaluation () {
      wx.request({
        url: 'http://127.0.0.1:8000/update_atest/', // 仅为示例，并非真实的接口地址
        method: 'POST',
        header: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: JSON.stringify(this.titleData),
        success (response) {
          if (response.data.code === 200) {
            $Message({
              content: '修改成功！',
              type: 'success'
            })
            wx.navigateTo({url: '../index/main'})
          } else {
            $Message({
              content: '修改失败！',
              type: 'success'
            })
          }
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
