<template>
  <div>
    <i-message id="message" />
    <form :model="createData">
      <i-panel title="测评标题">
        <input v-model="createData.tName"  maxLength="20" class="demo-input" mode="wrapped"/>
      </i-panel>
      <i-panel title="测评内容介绍">
        <input v-model="createData.tDescribe" type="textarea" class="demo-input" mode="wrapped"/>
      </i-panel>
      <i-panel>
        <i-button :size="buttonSize" type="primary" shape="circle" @click="handleCreate" >下一步</i-button>
      </i-panel>
      </form>
  </div>
</template>

<script>
import {$Message} from '../../../static/iview/base/index'
export default {
  mounted (options) {
    this.createData = {
      uId: 1,
      tName: '',
      tDescribe: ''
    }
    this.createData.uId = this.$root.$mp.query.uId
  },
  data () {
    return {
      createData: {
        uId: 1,
        tName: '',
        tDescribe: ''
      }
    }
  },

  methods: {
    handleCreate () {
      if (this.createData.tName === '' || this.createData.tName === '') {
        $Message({
          content: '请输入内容！',
          type: 'warning'
        })
        return
      }
      let uid = this.createData.uId
      wx.request({
        url: 'http://127.0.0.1:8000/create/', // 仅为示例，并非真实的接口地址
        method: 'POST',
        header: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: JSON.stringify(this.createData),
        success (response) {
          if (response.data.code === 200) {
            wx.navigateTo({
              url: '../create_demision/main?uId=' + uid + '&tId=' + response.data.tId
            })
          } else {
            console.log("failed!")
          }
        }
      })
    }
  }
}
</script>

<style scoped>
.message {
  color: red;
  padding: 10px;
  text-align: center;
}

.demo-input{
    color:black;
    padding: 7px 15px;
    border-radius: 4px;
    min-width: 65px;
    flex: 1;
    line-height: 1.6;
    padding: 4px 0;
    min-height: 22px;
    font-size: 14px;
    border: 1px solid;
    border-color: rgb(103, 103, 241);
    width:auto;
 }
    
</style>
