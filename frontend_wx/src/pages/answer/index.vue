<template>
  <div>
    <view style="margin-top: 10px">
      <i-panel title="测评标题">
          <view>{{testing.tName}}</view>
      </i-panel>
      <i-panel title="测评描述">
          <view>{{testing.tDescribe}}</view>
      </i-panel>
      <i-panel title="题目">
        <i-panel v-for="(list, ex) in testing.question" v-bind:key="ex">
          <i-panel title="题目名称">
            <view>{{list.qName}}</view>
          </i-panel>
          <i-radio-group :current="current[ex].choice" @change="handleChange">
            <i-radio v-for="(item,index) in testing.question[ex].options" :key="index" :value="item.oName" @touchstart="handleTouchStart(ex)">
            </i-radio>
          </i-radio-group>
        </i-panel>
      </i-panel>
      <i-button type="primary" @click="setAnswer">提交</i-button>
    </view>
    <i-message id="message" />
  </div>
</template>
<script>
import {$Message} from '../../../static/iview/base/index'
export default {
  mounted () {
    this.testing = {
      tId: -1,
      tName: '',
      tDescribe: '',
      question: []
    }
    this.current = []
    this.choices = {
      tId: -1,
      options: []
    }
    this.testing.tId = this.$root.$mp.query.tId
    this.choices.tId = this.$root.$mp.query.tId
    this.uId = this.$root.$mp.query.uId
    this.currentEx = -1
    this.searchTest()
  },
  data () {
    return {
      currentEx: -1,
      uId: -1,
      testing: {
        tId: -1,
        tName: '',
        tDescribe: '',
        question: []
      },
      current: [],
      choices: {
        tId: -1,
        options: []
      }
    }
  },

  methods: {
    handleTouchStart (ex) {
      this.currentEx = ex
    },
    handleChange ({mp}) {
      this.current[this.currentEx].choice = mp.detail.value
      this.choices.options[this.currentEx].qId = this.testing.question[this.currentEx].qId
      for (let i = 0; i < this.testing.question[this.currentEx].options.length; i++) {
        if (this.testing.question[this.currentEx].options[i].oName === this.current[this.currentEx].choice) {
          this.choices.options[this.currentEx].oId = this.testing.question[this.currentEx].options[i].oId
        }
      }
    },
    searchTest () {
      let list = this.testing
      let cur = this.current
      let options = this.choices.options
      wx.request({
        url: 'http://127.0.0.1:8000/show_atest/', // 仅为示例，并非真实的接口地址
        data: {tId: this.testing.tId},
        success (response) {
          console.log(response.data)
          if (response.data.code === 200) {
            list.tName = response.data.tName
            list.tDescribe = response.data.tDescribe
            for (let i = 0; i < response.data.question.length; i++) {
              let obj = {
                qId: response.data.question[i].qId,
                qName: response.data.question[i].qName,
                options: response.data.question[i].options
              }
              let current = {
                choice: ''
              }
              let opt = {
                qId: -1,
                oId: -1
              }
              list.question.push(obj)
              cur.push(current)
              options.push(opt)
            }
          } else {
            $Message({
              content: `读取失败！`,
              type: 'error'
            })
          }
        }
      })
      console.log(list)
      this.current = cur
      this.choices.options = options
      this.testing.tName = list.tName
      this.testing.tDescribe = list.tDescribe
      this.testing.question = list.question
    },
    setAnswer () {
      for (let i = 0; i < this.testing.question.length; i++) {
        if (this.choices.options[i].oId === -1) {
          $Message({
            content: '请答完所有题目！',
            type: 'warning'
          })
        }
      }
      console.log(this.choices)
      wx.request({
        url: 'http://127.0.0.1:8000/add_record/',
        method: 'POST',
        header: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: JSON.stringify(this.choices),
        success (response) {
          if (response.data.code === 200) {
            $Message({
              content: '提交成功！',
              type: 'success'
            })
            wx.navigateTo({url: '../answer_success/main?result=' + response.data.result})
          } else {
            $Message({
              content: '提交失败！',
              type: 'error'
            })
          }
        }
      })
    }
  }
}
</script>

<style scoped>
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