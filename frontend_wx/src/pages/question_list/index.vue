<template>
  <div>
    <i-button :size="buttonSize" type="primary" @click="jumpToAddQuestion">
       创建题目
    </i-button>
    <i-card v-for="(questiondata,index) in questionData" v-bind:key="index" :title="questiondata.qName">
      <view slot="footer"><i-button  @click="deleteQuestion(index)">删除</i-button></view>
    </i-card>
    <i-button type="primary" size="small" @click="goToIndex" >发布问卷</i-button>
  </div>
</template>

<script>
export default {
  mounted (options) {
    this.uId = this.$root.$mp.query.uId
    this.tId = this.$root.$mp.query.tId
    this.questionData = []
    this.searchQuestion()
  },
  data () {
    return {
      uId: 1,
      tId: 1,
      questionData: []
    }
  },
  methods: {
    deleteQuestion (index) {
      wx.request({
        url: 'http://127.0.0.1:8000/delete_question/',
        method: "POST",
        header: {
          "content-type": "application/x-www-form-urlencoded"
        },
        data: JSON.stringify(this.questionData[index]),
        success  (response) {
          console.log(response.data)
          if (response.data.code === 200) {
            console.log("delete success")
          } else {
            console.log(`can't search in database`)
          }
        }
      })
      this.questionData.splice(index, 1)
    },

    jumpToAddQuestion () {
      wx.navigateTo({
        url: '../create_question/main?uId=' + this.uId + '&tId=' + this.tId
      })
    },
    goToIndex () {
      wx.navigateTo({
        url: '../index/main'
      })
    },
    searchQuestion () {
      let lists = this.questionData
      wx.request({
        url: 'http://127.0.0.1:8000/search_all_questions/',
        data: {
          tId: this.tId
        },
        success  (response) {
          console.log(response.data)
          if (response.data.code === 200) {
            if (response.data.questionId.length > 0) {
              for (let i = 0; i < response.data.questionId.length; i++) {
                let obj = {
                  qId: response.data.questionId[i],
                  qName: response.data.questionName[i]
                }
                lists.push(obj)
              }
            }
          } else {
            console.log(`can't search in database`)
          }
        }
      })
      this.questionData = lists
    }
  }
}
</script>