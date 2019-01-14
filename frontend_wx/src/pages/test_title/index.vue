<template>
  <div>
    <i-card >
      <view slot="content">{{titleData.qTitle}}</view>
    </i-card>
    <i-card >
      <view slot="content">{{titleData.qDescribe}}</view>
    </i-card>
    <i-button type="primary" size="small" @click="evaluationEdit()" >编辑</i-button>
  </div>
</template>

<script>
export default {
  mounted (options) {
    this.titleData.tId = this.$root.$mp.query.tId
    this.searchTitle()
  },
  data () {
    return {
      uId: 1,
      tId: 1,
      titleData: {
        qTitle: '',
        qDescribe: ''
      }
    }
  },
  methods: {
    searchTitle () {
      let list = this.titleData
      wx.request({
        url: 'http://127.0.0.1:8000/search_atest_by/',
        data: {
          tId: this.tId
        },
        success  (response) {
          if (response.data.code === 200) {
            if (response.data.tName.length > 0) {
              list.qTitle = response.data.tName
              list.qDescribe = response.data.tDescribe
            }
          } else {
            console.log('can\'t search in database')
          }
        }
      })
      this.titleData = list
    },
    evaluationEdit () {
      wx.navigateTo({
        url: '../evaluation_edit/main?uId=1&tId=1'
      })
    }
  }
}
</script>