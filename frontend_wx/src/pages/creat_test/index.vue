<template>
  <div>
    <i-panel title="测评标题">
    <i-input value="value1" type="title"  mode="wrapped"/>
    </i-panel>
    <i-panel title="测评内容介绍">
    <i-input value="value1" type="textarea" autosize="{minRows: 3,maxRows: 5}" mode="wrapped"/>
    </i-panel>
    <i-panel>
    <i-button type="primary" size="small" @click="createdemision" >下一步</i-button>
    </i-panel>
  </div>
</template>

<script>

export default {
 

  data () {
    return {
      msg: 'Hello'
    }
        value1: '';
        value2: '';
        value3: '';
        value4: '输入框已禁用';
        value5: '';
        value6: '';
        value7: ''
  },

  methods: {
    createbody () {
      wx.navigateTo({
        url: ''
      })
    },
    handleClickNum (data) {
      console.log('>>>>>>', data.num)
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
