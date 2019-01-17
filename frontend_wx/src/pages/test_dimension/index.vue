<template>
  <div>
    <i-card v-for="(dimension,index) in dimensions.dimensionName" v-bind:key="index" title="维度">
      <view slot="content">{{dimensions.dimensionName[index]}}</view>
    </i-card>
    <i-button type="primary" size="small" @click="dimensionEdit" >编辑</i-button>
  </div>
</template>

<script>
export default {
  mounted (options) {
    this.dimensions = {
      dimensionId: [],
      dimensionName: [],
      tId: 1
    }
    this.uId = this.$root.$mp.query.uId
    this.dimensions.tId = this.$root.$mp.query.tId
    this.searchDimensions()
  },
  data () {
    return {
      uId: 1,
      tId: 1,
      dimensions: {
        dimensionId: [],
        dimensionName: [],
        tId: 1
      }
    }
  },
  methods: {
    searchDimensions () {
      var that = this
      wx.request({
        url: 'http://127.0.0.1:8000/search_dimensions/',
        data: {
          content: this.dimensions.tId
        },
        success  (response) {
          console.log(response.data)
          if (response.data.code === 200) {
            if (response.data.dId.length > 0) {
              that.dimensions.dimensionId = response.data.dId
              that.dimensions.dimensionName = response.data.dName
            }
          } else {
            console.log(`can't search in database`)
          }
        }
      })
    },
    dimensionEdit () {
      wx.navigateTo({
        url: '../dimension_edit/main?tId=' + this.dimensions.tId +'&uId=' + this.uId
      })
    }
  }
}
</script>