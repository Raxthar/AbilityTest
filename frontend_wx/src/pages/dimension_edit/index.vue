<template>
  <div>
    <i-message id="message" />
    <i-button type="primary" size="small" @click="editDimension" >保存</i-button>
    <i-panel v-for="(item,index) in lists"  v-bind:key="index">
      <i-panel title="请输入维度">
        <input :value="item.dName" @click="handleClick(index)" @input="handleInput" class="demo-input" type="text" placeholder="请输入维度名称"/>
      </i-panel>
    </i-panel>
   
  </div>
</template>

<script>
import {$Message} from '../../../static/iview/base/index'
export default {
  mounted (options) {
    this.dimensionLists.uId = this.$root.$mp.query.uId
    this.dimensionLists.tId = this.$root.$mp.query.tId
    this.dimensionLists.dimensions.tId = this.$root.$mp.query.tId
    this.searchDimensions()
  },

  data () {
    return {
      currentIndex: -1,
      lists: [
      ],
      dimensionLists: {
        uId: -1,
        tId: -1,
        dimensions: {
          dimensionId: [],
          dimensionName: [],
          tId: 1
        }
      }
    }
  },

  methods: {
    searchDimensions () {
      var that = this
      wx.request({
        url: 'http://127.0.0.1:8000/search_dimensions/',
        data: {
          content: this.dimensionLists.dimensions.tId
        },
        success  (response) {
          console.log(response.data)
          if (response.data.code === 200) {
            if (response.data.dId.length > 0) {
              that.dimensionLists.dimensions.dimensionId = response.data.dId
              that.dimensionLists.dimensions.dimensionName = response.data.dName
              for (let i = 0; i < response.data.dName.length; i++) {
                let obj = {
                  dName: response.data.dName[i]
                }
                that.lists.push(obj)
              }
            }
          } else {
            console.log(`can't search in database`)
          }
        }
      })
    },

    handleClick (index) {
      this.currentIndex = index
    },

    handleInput (e) {
      this.lists[this.currentIndex].dName = e.target.value
      this.dimensionLists.dimensions.dimensionName[this.currentIndex] = e.target.value
      console.log(this.dimensionLists.dimensions.dimensionName[this.currentIndex])
    },

    editDimension () {
      for (let i = 0; i < this.dimensionLists.dimensions.dimensionName.length; i++) {
        if (this.dimensionLists.dimensions.dimensionName[i] === '') {
          $Message({
            content: '维度不能为空！',
            type: 'warning'
          })
          return
        }
      }
      console.log(this.dimensionLists.dimensions)
      wx.request({
        url: 'http://127.0.0.1:8000/update_dimension/', // 仅为示例，并非真实的接口地址
        method: 'POST',
        header: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: JSON.stringify(this.dimensionLists.dimensions),
        success (response) {
          console.log(response.data.code)
          if (response.data.code === 200) {
            $Message({
              content: '修改成功！',
              type: 'success'
            })
          }
        }
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
