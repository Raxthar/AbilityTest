<template>
  <div>
    <i-button type="primary" size="small" @click="createQuestion" >创建题目</i-button>
    <i-button type="primary" size="small" @click="returnIndex" >发布问卷</i-button>
  </div>
</template>

<script>
export default {
  data () {
    return {
      lists: [{
        index: {}
      }]
    }
  },

  methods: {
    createQuestion () {
      wx.navigateTo({
        url: '../create_question/main'
      })
    },
    returnIndex () {
      wx.navigateTo({
        url: '../index/main'
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
</style>
