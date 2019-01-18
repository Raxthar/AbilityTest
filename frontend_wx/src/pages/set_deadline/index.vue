<template>
   <div>
    <i-message id="message" />
    <Form :model="dimensions">
      <FormItem v-for="(Item,index) in judges.dimensionName" v-bind:key="index">
        <p>维度：{{Item}}</p>
        <Input :value="value" @click="handleClick(index)" @input="handleInput" size="large" placeholder="请输入评价" class="demo-input"/>
      </FormItem>
       <picker mode="multiSelector" @change="bindMultiPickerChange" :value="multiIndex" :range="newMultiArray">
            <p>设置截止日期</p>
            <i-button type="default" >{{time}}</i-button>    
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
        time: "2019-01-01 00:00",
        multiArray: [],
        multiIndex: [0, 0, 0, 0, 0],
        currentIndex: -1,
        tId: 3,
        value: "",
        judges: {
          dimensionId: [],
          dimensionName: [],
          judge: [],
          due: '',
          tId: 3
        }
      }
    },
    computed: {newMultiArray: () => {
      let array = [];
      const date = new Date();
      const years = [];
      const months = [];
      const days = [];
      const hours = [];
      const minutes = [];
      for (let i = 2018; i <= date.getFullYear() + 10; i++) {        
        years.push("" + i);      
      }      
      array.push(years);      
      for (let i = 1; i <= 12; i++) {        
        if (i < 10) {          
          i = "0" + i;        
          }       
           months.push("" + i);      
           }      
           array.push(months);      
           for (let i = 1; i <= 31; i++) {       
            if (i < 10) {          
              i = "0" + i;        
              }        
              days.push("" + i);      
              }      
              array.push(days);      
              for (let i = 0; i < 24; i++) {        
                if (i < 10) {          
                  i = "0" + i;        
                  }        
                  hours.push("" + i);      
                  }     
                   array.push(hours);      
                   for (let i = 0; i < 60; i++) {     
                      if (i < 10) {          
                        i = "0" + i;        
                        }      
                        minutes.push("" + i);      
                        }      
                        array.push(minutes);      
                        return array;    
                        }  
                        },
    methods: {
        bindMultiPickerChange(e) {      
          this.multiIndex = e.target.value;      
          console.log("当前选择的时间", this.multiIndex);      
          const index = this.multiIndex;      
          const year = this.newMultiArray[0][index[0]];      
          const month = this.newMultiArray[1][index[1]];      
          const day = this.newMultiArray[2][index[2]];      
          const hour = this.newMultiArray[3][index[3]];      
          const minute = this.newMultiArray[4][index[4]];      
          this.time = year + "-" + month + "-" + day + " " + hour + ":" + minute;
          this.judges.due = this.time;
          console.log(this.judges.due)  
          },
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
