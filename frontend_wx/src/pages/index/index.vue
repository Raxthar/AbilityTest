<template>
  <div>
    <i-message id="message" />
    <i-button type="primary" size="small" @click="testtitle" >创建测评</i-button>
    <i-card v-for="(evaluation, index) in evaluationLists" v-bind:key="index" :title="evaluation.tName" @click="handleOpen(index)">
      <view slot="footer">{{evaluation.tId}}</view>
    </i-card>
    <i-action-sheet :visible="visible" :actions="actions" show-cancel @cancel="handleCancel" @iclick="handleClickItem"
    :mask-closable="false" />
  </div>
</template>

<script>
import { $Message } from '../../../static/iview/base/index'
export default {
  onShow () {
    this.evaluationLists = []
    this.searchEvaluation()
  },

  data () {
    return {
      currentIndex: -1,
      visible: false,
      actions: [
        {
          name: '查看/修改测评标题、描述'
        },
        {
          name: '查看/修改测评维度'
        },
        {
          name: '查看/修改测评题目'
        },
        {
          name: '设置截止时间、自动评价'
        },
        {
          name: '去分享',
          icon: 'share',
          openType: 'share'
        },
        {
          name: '删除测评',
          color: '#ed3f14'
        }
      ],
      msg: 'Hello',
      uId: 2,
      evaluationLists: []
    }
  },

  methods: {
    searchEvaluation () {
      let lists = this.evaluationLists
      wx.request({
        url: 'http://127.0.0.1:8000/test_list/',
        data: {
          uId: this.uId
        },
        success (response) {
          if (response.data.code === 200) {
            if (response.data.tName.length > 0) {
              for (let i = 0; i < response.data.tName.length; i++) {
                let obj = {
                  tId: response.data.tId[i],
                  tName: response.data.tName[i],
                  tStatus: response.data.tStatus[i] ? '已发布' : '未发布'
                }
                lists.push(obj)
              }
            }
          } else {
            $Message ({
              content: '读取数据失败！',
              type: 'error'
            })
          }
        }
      })
      this.evaluationLists = lists
    },

    handleOpen (index) {
      this.visible = true
      this.currentIndex = index
    },

    handleCancel () {
      this.visible = false
    },

    handleClickItem ({ mp }) {
      let obj = {
        cIndex: this.currentIndex,
        list: this.evaluationLists,
        visible: this.visible
      }
      switch (mp.detail.index) {
        case 0:
          this.visible = false
          wx.navigateTo({
            url: '../test_title/main?uId=' + this.uId + '&tId=' + this.evaluationLists[this.currentIndex].tId
          })
          break
        case 1:
          this.visible = false
          wx.navigateTo({
            url: '../test-dimension/main?tId=' + this.evaluationLists[this.currentIndex].tId
          })
          break
        case 2:
          break
        case 3:
          break
        case 4:
          break
        case 5:
          wx.request({
            url: 'http://127.0.0.1:8000/delete_evaluation/',
            method: 'POST',
            header: {
              'content-type': 'application/x-www-form-urlencoded'
            },
            data: JSON.stringify(this.evaluationLists[this.currentIndex]),
            success (response) {
              if (response.data.code === 200) {
                obj.list.splice(obj.cIndex, 1)
                $Message({
                  content: '删除成功！',
                  type: 'success'
                })
              } else {
                $Message({
                  content: '删除失败！',
                  type: 'error'
                })
              }
            }
          })
          this.visible = false
          this.evaluationLists = obj.list
          break
        }
    },

    testtitle () {
      wx.navigateTo({
        url: '../creat_test/main?uId=' + this.uId
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
