<template>
  <div>
    <i-card v-for="(questiondata,index) in questionData" v-bind:key="index" :title="questiondata.qName">
       <view slot="footer"><i-button  @click="questionEdit(index)">编辑</i-button></view>
    </i-card>
    <i-button type="primary" size="small" @click="0" >发布问卷</i-button>
  </div>
</template>

<script>
export default {
  mounted (options) {
    this.questionData.uId = this.$root.$mp.query.uId
    this.questionData.tId = this.$root.$mp.query.tId
    this.searchQuestion()
  },
  data () {
    return {
      uId: 1,
      tId: 2,
      questionData: []
    }
  },
  methods: {
    jumpToAddQuestion () {
      wx.navigateTo({
        url: '../create_question/main?uId=2&tId=2'
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
            console.log('can\'t search in database')
          }
        }
      })
      this.questionData = lists
    },
    questionEdit (index) {
      let qId = this.questionData[index].qId
      wx.navigateTo({
        url: '../question_edit/main?uId=' + this.questionData.uId + '&tId=' + this.questionData.tId + '&qId=' + qId
      })
    }
  }
}
</script>