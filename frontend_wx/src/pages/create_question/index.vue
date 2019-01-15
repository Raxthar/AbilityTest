<template>
  <div>
    <view style="margin-top: 10px">
    <form :model="questionData">
      <formitem label="input">
          <input v-model="questionData.qName" placeholder="Enter Title..."  class="demo-input"/>
      </formitem>
      <formitem v-for="(list, ex) in lists" >
          <input v-model="list.oName" placeholder="请输入选项" class="demo-input" />
          <input v-model="list.score" placeholder="请输入分数" class="demo-input"/>
          <i-radio-group  v-model="checkvalue[ex]"  :current="current"  @change="handleFruitChange">
            <i-radio v-for="(item,index) in dimensionsData"   :key="item.dId" :value="item.dName">
            </i-radio>
          </i-radio-group>
      </formitem>
      <i-button type="primary" @click="setQuestion">提交</i-button>
    </form>
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
    this.searchDimension()
    // this.uId = this.$root.$mp.query.uId
    // this.questionData.tId = this.$root.$mp.tId
  },
  data () {
    return {
      uId: 1,
      lists: [{
        oName: "123",
        score: 0,
        dID: 1
      }],
      dimensionsData: [],
      questionData: {
        tId: 3,
        qName: '',
        oName: [],
        dId: [],
        score: []
      },
      current: "",
      checkvalue: []
    }
  },

  methods: {
    handleFruitChange ({mp}) {
      this.current = mp.detail.value
    },
    addOption () {
      let cope = {
        oName: "",
        score: "",
        dID: ""
      }
      this.lists.push(cope)
    },
    delOption (ex) {
      this.lists.splice(ex, 1)
    },
    searchDimension () {
      let list = this.dimensionsData
      wx.request({
        url: 'http://127.0.0.1:8000/search_dimensions/', // 仅为示例，并非真实的接口地址
        // method: "GET",
        header: {
          "content-type": "application/x-www-form-urlencoded"
        },
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
