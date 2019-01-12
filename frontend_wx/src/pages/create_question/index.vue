<template>
  <div>
    <form>
      <formitem label="input">
          <i-input  placeholder="Enter Title..." />
      </formitem>
      <formitem v-for="(list, index) in lists" v-bind:key="index">
          <i-input size="large" placeholder="请输入选项" />
          <i-input  size="small" placeholder="请输入分数" />
          <i-radio-group  bindchange="handleFruitChange">
            <i-radio >
            </i-radio>
          </i-radio-group>
      </formitem>
      <i-button type="primary" @click="setQuestion">提交</i-button>
    </form>
            <i-button type="primary" @click="addOption">添加选项</i-button><br><br>
            <i-button type="primary" @click="delOption">删除选项</i-button><br><br>
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
    addOption () {
      let cope = {
        index: ''
      }
      this.lists.push(cope)
    },
    delOption (index) {
      this.lists.splice(index, 1)
    },
    handleFruitChange ({ detail = {} }) {
      this.setData({
        current: detail.value
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
