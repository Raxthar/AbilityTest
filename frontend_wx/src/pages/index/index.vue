<template>
  <div >
    <i-button type="primary" size="small" @click="createbtn" >创建测评</i-button>
    <i-card title="龙卷风摧毁停车场" extra="额外内容" >
      <view slot="footer">测评编号</view>
    </i-card>
    <i-card title="乌鸦坐飞机" extra="额外内容" >
      <view slot="footer">测评编号</view>
    </i-card>
    <i-card title="poipoipoi" extra="额外内容" >
      <view slot="footer">测评编号</view>
    </i-card>
  </div>
</template>

<script>
// 导入 click-counter 组件
import ClickCounter from '@/components/click-counter'

export default {
  // 声明在当前组件下使用 counter-click 组件
  components: { ClickCounter },

  data () {
    return {
      msg: 'Hello'
    }
  },

  methods: {
    createbtn () {
      wx.navigateTo({
        url: '../creat_test/main'
      })
    },

    clickHandle () {
      this.msg = 'Clicked!!!!!!'
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
