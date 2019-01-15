<template>
  <div>
    <view style="margin-top: 10px">
      <i-panel title="题干">
          <input v-model="questionData.qName" placeholder="请输入题干" class="demo-input"/>
      </i-panel>
      <i-panel title="选项">
        <i-panel v-for="(list, ex) in lists" v-bind:key="ex">
          <i-panel title="名称">
            <input v-model="list.oName" placeholder="请输入选项" class="demo-input" />
          </i-panel>
          <i-panel title="对应分数及维度">
            <i-panel title="请选择维度">
              <i-radio-group :current="current[ex].choice" @change="handleFruitChange">
                <i-radio v-for="(item,index) in dimensionsData" :key="index" :value="item.dName" @touchstart="handleTouchStart(ex)">
                </i-radio>
              </i-radio-group>
            </i-panel>
            <input v-model="list.score" placeholder="请输入选项分数" class="demo-input" />
          </i-panel>
        </i-panel>
      </i-panel>
      <i-button type="primary" @click="setQuestion">提交</i-button>
      <i-button type="primary" @click="addOption">添加选项</i-button><br><br>
      <i-button type="primary" @click="delOption">删除选项</i-button><br><br>
    </view>
    <i-message id="message" />
  </div>
</template>
<script>
import {$Message} from '../../../static/iview/base/index'
export default {
  mounted (options) {
    this.uId = this.$root.$mp.query.uId
    this.questionData.tId = this.$root.$mp.query.tId
    this.searchDimension()
  },
  data () {
    return {
      currentEx: -1,
      uId: 1,
      lists: [{
        oName: '',
        score: 0,
        dID: 1
      }],
      dimensionsData: [],
      questionData: {
        tId: -1,
        qName: '',
        oName: [],
        dId: [],
        score: []
      },
      current: [{
        choice: ''
      }],
      checkvalue: []
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
    handleFruitChange ({mp}) {
      this.current[this.currentEx].choice = mp.detail.value
    },
    addOption () {
      let obj = {
        choice: ''
      }
      let cope = {
        oName: "",
        score: "",
        dID: ""
      }
      this.lists.push(cope)
      this.current.push(obj)
    },
    delOption (ex) {
      this.lists.splice(ex, 1)
    },
    searchDimension () {
      let list = this.dimensionsData
      wx.request({
        url: 'http://127.0.0.1:8000/search_dimensions/', // 仅为示例，并非真实的接口地址
        data: {content: this.questionData.tId},
        success (response) {
          console.log(response.data)
          if (response.data.code === 200) {
            if (response.data.dId.length > 0) {
              for (let i = 0; i < response.data.dId.length; i++) {
                let obj = {
                  dName: response.data.dName[i],
                  dId: response.data.dId[i]
                }
                list.push(obj)
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
    setQuestion () {
      if (this.questionData.qName === '') {
        $Message({
          content: '请输入题目名',
          type: 'error'
        })
        return
      }
      console.log("7")
      for (let i = 0; i < this.lists.length; i++) {
        this.questionData.dId[i] = 1
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
              url: '../question_list/main'
            })
          } else {
            $Message({
              content: '无法读取数据库',
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
/*.message {
  color: red;
  padding: 10px;
  text-align: center;
}*/
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
