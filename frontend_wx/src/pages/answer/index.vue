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
    this.choice.tId = this.$root.$mp.query.tId
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
        url: 'http://127.0.0.1:8000/search_dimensions/', // 仅为示例，并非真实的接口地址
        data: {content: this.testing.tId},
        success (response) {
          console.log(response.data)
          if (response.data.code === 200) {
            list.tName = response.data.tName
            list.tDescribe = response.data.tDescribe
            for (let i = 0; i < response.data.question.length; i++) {
              list.question[i].qId = response.question[i].qId
              list.question[i].qName = response.question[i].qName
              for (let j = 0; j < response.question[i].options.length; j++) {
                response.question[i].options[j].oId = response.question[i]
              }
            }
          } else {
            $Message({
              content: `无法读取数据库`,
              type: 'error'
            })
          }
        }
      })
      this.dimensionsData = list
    },
    setAnswer () {
      if (this.questionData.qName === '') {
        $Message({
          content: '请输入题目名',
          type: 'error'
        })
        return
      }
      for (let i = 0; i < this.lists.length; i++) {
        this.questionData.dId[i] = this.lists[i].dID
        this.questionData.score[i] = this.lists[i].score
        this.questionData.oName[i] = this.lists[i].oName
        console.log(this.questionData.oName[i])
        if (!this.questionData.dId[i]) {
          $Message({
            content: '请为选项选择关联维度',
            type: 'error'
          })
          return
        }
        if (!this.lists[i].oName) {
          $Message({
            content: '请输入选项内容',
            type: 'error'
          })
          return
        } else if (!this.lists[i].score) {
          this.questionData.score[i] = 1
        }
      }
      let uid = this.uId
      let tid = this.questionData.tId
      wx.request({
        url: 'http://127.0.0.1:8000/question_chat/', // 仅为示例，并非真实的接口地址
        method: "POST",
        header: {
          "content-type": "application/x-www-form-urlencoded"
        },
        data: JSON.stringify(this.questionData),
        success (response) {
          if (response.data.code === 200) {
            $Message({
              content: '添加题目成功',
              type: 'success'
            })
            wx.navigateTo({
              url: '../question_list/main?uId=' + uid + '&tId=' + tid
            })
          } else {
            $Message({
              content: '操作失败',
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