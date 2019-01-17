<template>
  <div>
    <i-message id="message" />
    <i-button @click='addDimension'>新维度</i-button>
    <i-panel v-for="(item,index) in lists"  v-bind:key="index">
      <i-panel title="请输入维度">
        <input :value="item.dName" @click="handleClick(index)" @input="handleInput" class="demo-input" type="text" placeholder="请输入维度名称"/>
        <i-button @click='delDimension(index)'>删除</i-button>
      </i-panel>
    </i-panel>
    <i-button type="primary" size="small" @click="questionList" >下一步</i-button>
  </div>
</template>

<script>
import {$Message} from '../../../static/iview/base/index'
export default {
  mounted (options) {
    this.currentIndex = -1
    this.lists = [{dName: ''}]
    this.dimensionLists = {
      uId: -1,
      tId: -1,
      dimensions: []
    }
    this.dimensionLists.uId = this.$root.$mp.query.uId
    this.dimensionLists.tId = this.$root.$mp.query.tId
  },

  data () {
    return {
      currentIndex: -1,
      lists: [
        {
          dName: ''
        }
      ],
      dimensionLists: {
        uId: -1,
        tId: -1,
        dimensions: []
      }
    }
  },

  methods: {
    questionList () {
      let tid = this.dimensionLists.tId
      let uid = this.dimensionLists.uId
      if (this.dimensionLists.dimensions.length !== 0) {
        for(let i = 0; i < this.dimensionLists.dimensions.length; i++) {
          if (this.dimensionLists.dimensions[i].dName === '') {
            $Message ({
              content: '请输入维度！',
              type: 'warning'
            })
            return
          }
        }
      } else {
        $Message ({
              content: '请输入维度！',
              type: 'warning'
        })
        return
      }
      wx.request({
        url: 'http://127.0.0.1:8000/create_dimension/', // 仅为示例，并非真实的接口地址
        method: 'POST',
        header: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: JSON.stringify(this.dimensionLists),
        success (response) {
          console.log(response.data)
          if (response.data.code === 200) {
            wx.navigateTo({
              url: '../create_question/main?tId=' + tid + '&uId=' + uid
            })
          } else {
            console.log("failed!")
          }
        }
      })
    },

    handleClick (index) {
      this.currentIndex = index
    },

    handleInput (e) {
      this.lists[this.currentIndex].dName = e.target.value
      this.dimensionLists.dimensions = this.lists
    },

    addDimension () {
      let cope = {
        dName: ''
      }
      this.lists.push(cope)
    },
    delDimension (index) {
      console.log(index)
      this.dimensionLists.dimensions.splice(index, 1)
      this.lists.splice(index, 1)
      console.log(this.dimensionLists.dimensions)
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
