<template>
   <div>
    <i-message id="message" />
    <Form :model="dimensions">
      <FormItem v-for="(Item,index) in judges.dimensionName" v-bind:key="index">
        <p>{{Item}}</p>
        <Input :value="value" @click="handleClick(index)" @input="handleInput" size="large" placeholder="请输入评价" class="demo-input"/>
      </FormItem>
      <p>截止日期</p>
      <picker class="weui-btn" mode="date"  start="2015-09-01" end="2040-09-01" @change="bindDateChange">
      <button type="default" >{{judges.due}}</button>
      </picker>
      <i-button type="primary" @click="editJudge">提交</i-button>
    </Form>
 </div>
</template>

<script>
  import {$Message} from '../../../static/iview/base/index'
  export default {
    mounted (options) {
      this.tId = this.$root.$mp.query.tId
      this.judges.tId = this.$root.$mp.query.tId
      this.searchDimension()
    },
    data () {
      return {
        date: '2016-09-01',
        currentIndex: -1,
        tId: 3,
        value: "",
        judges: {
          dimensionId: [],
          dimensionName: [],
          judge: [],
          due: '2019-01-01',
          tId: 3
        }
      }
    },
    methods: {
      bindDateChange (e) {
        this.judges.due = e.mp.detail.value
      },
      handleClick (index) {
        this.currentIndex = index
      },
      handleInput (e) {
        this.judges.judge[this.currentIndex] = e.target.value
      },
      searchDimension () {
        let list = this.judges
        wx.request({
          url: 'http://127.0.0.1:8000/search_dimensions/', // 仅为示例，并非真实的接口地址
          method: "GET",
          header: {
            "content-type": "application/x-www-form-urlencoded"
          },
          data: {content: this.judges.tId},
          success (response) {
            console.log(response.data)
            if (response.data.code === 200) {
              if (response.data.dId.length > 0) {
                for (let i = 0; i < response.data.dId.length; i++) {
                  list.dimensionName = response.data.dName
                  list.dimensionId = response.data.dId
                  console.log(list.dimensionName)
                }
              }
            } else {
              $Message({
                content: `无法读取数据库`,
                type: 'error'
              })
            }
          }
        })
        this.judges = list
      },
      editJudge () {
        wx.request({
          url: 'http://127.0.0.1:8000/edit_judge/', // 仅为示例，并非真实的接口地址
          method: "POST",
          header: {
            "content-type": "application/x-www-form-urlencoded"
          },
          data: JSON.stringify(this.judges),
          success (response) {
            console.log(response.data)
            if (response.data.code === 200) {
              $Message({
                content: `设置评价成功`,
                type: 'success'
              })
              wx.navigateTo({
                url: '../index/main'
              })
            } else {
              $Message({
                content: `无法读取数据库`,
                type: 'error'
              })
            }
          }
        })
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
