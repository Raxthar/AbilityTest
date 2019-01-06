<template>
  <div >
    <navigator url="../creat_test/main">123</navigator>
       <i-button type="primary" bind:click="creatbtn">这是一个按钮</i-button>

     <i-card full title="卡片标题" extra="额外内容" thumb="https://i.loli.net/2017/08/21/599a521472424.jpg">
     <view slot="content">内容不错</view>
     <view slot="footer">尾部内容</view>
     </i-card>
     <i-button>123</i-button>
    <div class="message">{{msg}}</div>
    <!-- 使用 click-counter 组件 -->
    <click-counter :init-num="10" @clicknum="handleClickNum" ><input type="checkbox" /> 禁用</click-counter>
    <click-counter :init-num="10" @clicknum="handleClickNum" />
    <click-counter :init-num="10" @clicknum="handleClickNum" />
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
    creatbtn: function (options) {
      wx.switchTab({
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
