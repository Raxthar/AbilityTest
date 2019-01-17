<template>
  <div>
    <view style="margin-top: 10px">
      <i-panel title="测评结果">
          <view>{{result}}</view>
      </i-panel>
      <i-button type="primary" @click="back">返回首页</i-button>
    </view>
    <i-message id="message" />
  </div>
</template>
<script>
import {$Message} from '../../../static/iview/base/index'
export default {
  mounted (options) {
    this.judge()
  },
  data () {
    return {
      result: ''
    }
  },

  methods: {
    judge () {
      if (this.$root.$mp.query.result === '') {
        this.result = '谢谢参与！'
      } else {
        this.result = this.$root.$mp.query.result
      }
    },
    back () {
      wx.navigateTo({url: '../index/main'})
    }
  }
}
</script>

<style scoped>
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