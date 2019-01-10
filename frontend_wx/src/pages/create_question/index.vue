<template>
  <div>
    <form :model="questionData">
              <formitem label="input">
                  <i-input  placeholder="Enter Title..." />
              </formitem>
              <formitem v-for="(list, index) in lists" v-bind:key="index">
                  <i-input size="large" placeholder="请输入选项" />
                  <i-input  size="small" placeholder="请输入分数" />
                  <i-radio-group current="{{current}}" bindchange="handleFruitChange">
                    <i-radio v-for="(fruit, index) in fruit" v-bind:key="index">
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
      }],

      fruit: [{
        id: 1,
        name: '香蕉'
      }, {
        id: 2,
        name: '苹果'
      }, {
        id: 3,
        name: '西瓜'
      }, {
        current: '苹果',
        id: 4,
        name: '葡萄'
      }],
      position: 'left',
      animal: '熊猫'

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
