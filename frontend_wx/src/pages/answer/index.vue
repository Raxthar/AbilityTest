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
  mounted (options) {
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
        question: [{
          qId: -1,
          qName: '',
          options: [{
            oId: -1,
            oName: ''
          }]
        }]
      },
      current: [{
        choice: ''
      }],
      choices: {
        tId: -1,
        options: [{
          qId: -1,
          oId: -1
        }]
      }
    }
  },

  methods: {
    handleTouchStart (ex) {
      $Message({
        content: '点击了第' + ex + '项',
        type: 'success'
      })
      this.currentEx = ex
    },
    handleChange ({mp}) {
      this.current[this.currentEx].choice = mp.detail.value
      this.choices.options[this.currentEx].qId = this.testing.question[this.currentEx].qId // 当前问题的id赋值给结果
      for (let i = 0; i < this.testing.question[this.currentEx].options.length; i++) { // 寻找当前选项对应的id存入结果中
        if (this.testing.question[this.currentEx].options.oName === this.current[this.currentEx].choice) {
          this.choices.options[this.currentEx].oId = this.testing.question[this.currentEx].options.oId
        }
      }
    },
    searchTest () {
      let list = this.testing
      wx.request({
        url: 'http://127.0.0.1:8000/show_atest/', // 仅为示例，并非真实的接口地址
        data: {tId: this.testing.tId},
        success (response) {
          console.log(response.data)
          if (response.data.code === 200) {
            list.tName = response.data.tName
            list.tDescribe = response.data.tDescribe
<<<<<<< HEAD
            for (let i = 0; i < response.data.question.length; i++) {
              list.question[i].qId = response.question[i].qId
              list.question[i].qName = response.question[i].qName
              for (let j = 0; j < response.question[i].options.length; j++) {
                response.question[i].options[j].oId = response.question[i]
              }
            }
=======
            list.question = response.data.question
            console.list
>>>>>>> Fix eslint errors. Ref #144
          } else {
            $Message({
              content: `无法读取数据库`,
              type: 'error'
            })
          }
        }
      })
      this.testing.tName = list.tName
      this.testing.tDescribe = list.tDescribe
      this.testing.question = list.question
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