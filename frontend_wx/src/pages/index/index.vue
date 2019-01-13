<template>
  <div >
    <i-massage id="message" />
    <i-button type="primary" size="small" @click="testtitle" >创建测评</i-button>
    <i-card v-for="(evaluation, index) in evaluationLists" v-bind:key="index" :title="evaluation.tName" @click="handleOpen(index)">
      <view slot="footer">{{evaluation.tStatus}}</view>
    </i-card>
    <i-action-sheet :visible="visible" :actions="actions" show-cancel @cancel="handleCancel" @iclick="handleClickItem"
    :mask-closable="false" />
  </div>
</template>

<script>

export default {
  mounted () {
    this.searchEvaluation()
  },

  data () {
    return {
      currentIndex: -1,
      visible: false,
      actions: [
        {
          name: '查看详细信息'
        },
        {
          name: '修改测评'
        },
        {
          name: '去分享',
          icon: 'share',
          openType: 'share'
        },
        {
          name: '删除测评',
          color: '#ed3f14'
        },
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
          console.log(response.data)
          if(response.data.code === 200) {
            if(response.data.tName.length > 0) {
              for(let i = 0; i < response.data.tName.length; i++) {
                let obj = {
                  tId: response.data.tId[i],
                  tName: response.data.tName[i],
                  tStatus: response.data.tStatus[i] ? '已发布':'未发布'
                }
                lists.push(obj)
              }
            }
          } else {
            $Message({
              content: '读取信息错误！',
              type: 'error'
            })
          }
        }
      })
      this.evaluationLists = lists
    },

    handleOpen (index) {
      console.log(index)
      this.visible = true
      this.currentIndex = index
    },

    handleCancel () {
      this.visible = false
    },

    handleClickItem ({ mp }) {
      console.log(mp.detail.index)
      switch(mp.detail.index) {
        case 0:
          break
        case 1:
          break
        case 3:
          console.log(this.currentIndex)
          wx.request ({
            url: 'http://127.0.0.1:8000/delete_evaluation/',
            method: 'POST',
            header: {
              "content-type": "application/x-www-form-urlencoded"
            },
            data: JSON.stringify(this.evaluationLists[this.currentIndex]),
            success(response) {
              console.log(response.data)
              if(response.data.code === 200) {
                console.log("success")
              } else {
                console.log("delete failed")
              }
            }
          })
          break
      }
    },

    createbtn () {
      wx.navigateTo({
        url: '../create_demision/main'
      })
    },

    testtitle () {
      wx.navigateTo({
        url: '../creat_test/main?uId=' + this.uId
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
