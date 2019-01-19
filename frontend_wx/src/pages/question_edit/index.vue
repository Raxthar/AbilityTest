<template>
   <div>
     <i-message id="message" />
     <Form :model="questionData">
       <FormItem label="input">
         <view>题目名</view>
         <input v-model="questionData.newQuestionName" placeholder="Enter Title..." class="demo-input"/>
       </FormItem>
          <i-panel v-for="(options,ex) in questionData.newOptionData" v-bind:key="ex">
            <view>选项——该选项分数</view>
            <input v-model="options.oName" size="large" placeholder="请输入选项" class="demo-input" />
            <i-input-number :value="options.score"  min="-2" max="100"  @change="handleChange" @touchstart="handleTouchStart(ex)" />
          <i-panel title="请选择维度">
              <i-radio-group :current="current[ex].choice" @change="handleFruitChange">
                <i-radio v-for="(item,index) in dimensions" v-bind:key="index" :value="item.dName" @touchstart="handleTouchStart(ex)">
                </i-radio>
              </i-radio-group>
            </i-panel>
          </i-panel>
          <Button type="primary" class="submit-button" @click="editQuestion">提交</Button>
      </Form>
  </div>
</template>

<script>
import {$Message} from '../../../static/iview/base/index'
export default {
  mounted () {
    this.current = [{
      choice: ''
    }]
    this.questionData = {
      qId: 1,
      tId: -1,
      qName: '',
      oName: [],
      dId: [],
      score: [],
      newQuestionName: '',
      newOptionData: []
    }
    this.oldOptionData = []
    this.dimensionsData = []
    this.dimensionsDatas = []
    this.dimensionId = []
    this.dimensionName = []
    this.dimensions = []
    this.oldQuestionName = ''
    this.dimensionsDatas = []
    this.currentEx = -1
    this.uId = this.$root.$mp.query.uId
    this.questionData.tId = this.$root.$mp.query.tId
    this.questionData.qId = this.$root.$mp.query.qId
    this.searchDimensions()
    this.searchQuestion()
  },
  data () {
    return {
      currentEx: -1,
      uId: -1,
      oldOptionData: [],
      dimensionsData: [],
      dimensionsDatas: [],
      dimensionId: [],
      dimensionName: [],
      dimensions: [],
      oldQuestionName: '',
      questionData: {
        qId: 1,
        tId: -1,
        qName: '',
        oName: [],
        dId: [],
        score: [],
        newQuestionName: '',
        newOptionData: []
      },
      current: [{
        choice: ''
      }]
    }
  },

  methods: {
    handleTouchStart (ex) {
      this.currentEx = ex
    },
    handleFruitChange ({mp}) {
      this.current[this.currentEx].choice = mp.detail.value
      for (let i = 0; i < this.dimensions.length; i++) {
        if (this.dimensions[i].dName === this.current[this.currentEx].choice) {
          this.questionData.newOptionData[this.currentEx].dId = this.dimensions[i].dId
        }
      }
    },
    handleChange ({mp}) {
      $Message({
        content: '当前数值为' + mp.detail.value,
        type: 'warning'
      })
      this.questionData.newOptionData[this.currentEx].score = mp.detail.value
    },
    searchDimensions () {
      var that = this
      wx.request({
        url: 'http://127.0.0.1:8000/search_dimensions/',
        data: {
          content: this.questionData.tId
        },
        success  (response) {
          if (response.data.code === 200) {
            for (let i = 0; i < response.data.dId.length; i++) {
              let obj = {
                dName: response.data.dName[i],
                dId: response.data.dId[i]
              }
              that.dimensions.push(obj)
            }
          } else {

          }
        }
      })
    },
    searchQuestion () {
      var that = this
      wx.request({
        url: 'http://127.0.0.1:8000/edit_question/',
        data: {
          qId: that.questionData.qId
        },
        success  (response) {
          if (response.data.code === 200) {
            if (response.data.oName.length > 0) {
              let oldOptionData = []
              let oldQuestionName = ''
              let questionName = response.data.qName
              oldQuestionName = questionName
              let optionName = response.data.oName
              let dimensionName = response.data.dName
              let scoreData = response.data.score
              let dimensionId = response.data.dId
              for (let i = 0; i < response.data.oName.length; i++) {
                let obj = {
                  oName: optionName[i],
                  score: scoreData[i],
                  dId: dimensionId[i]
                }
                oldOptionData.push(obj)
              }
              that.questionData.newOptionData = oldOptionData
              that.questionData.newQuestionName = oldQuestionName
              for (let i = 0; i < dimensionName.length; i++) {
                let obj = {
                  dName: dimensionName[i],
                  dId: dimensionId[i]
                }
                that.dimensionsData.push(obj)
              }
            }
          } else {

          }
        }
      })
    },
    editQuestion () {
      if (this.questionData.newQuestionName === '') {
        $Message({
          content: '标题不能为空！',
          type: 'warning'
        })
        return
      }
      for (let i = 0; i < this.questionData.newOptionData.length; i++) {
        if (this.questionData.newOptionData[i].oName === '') {
          $Message({
            content: '选项名不能为空！',
            type: 'warning'
          })
          return
        }
        if (this.questionData.newOptionData[i].score === '') {
          $Message({
            content: '请输入选项分数',
            type: 'error'
          })
        }
      }
      wx.request({
        url: 'http://127.0.0.1:8000/update_question/', // 仅为示例，并非真实的接口地址
        method: 'POST',
        header: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: JSON.stringify(this.questionData),
        success (response) {
          if (response.data.code === 200) {
            $Message({
              content: '修改成功！',
              type: 'success'
            })
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
