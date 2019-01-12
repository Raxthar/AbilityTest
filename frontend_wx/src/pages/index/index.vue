<template>
  <div >
    <i-button type="primary" size="small" @click="createbtn" >创建测评</i-button>
    <i-button type="primary" size="small" @click="testtitle" >测试</i-button>
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

export default {
  data () {
    return {
      msg: 'Hello',
      u_id: 2
    }
  },

  methods: {
    createbtn () {
      wx.navigateTo({
        url: '../create_demision/main'
      })
    },

    testtitle () {
      wx.navigateTo({
        url: '../creat_test/main?uId=2'
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
