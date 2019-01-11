<template>
  <div>
    <form title="测评维度">
      <input v-model="newAddText" placeholder="请输入要添加的内容" />	
        <i-button @click='addDimension'>添加</i-button>	
          <ul>		
            <formitem  v-for="(item,index) in lists"  v-bind:key="index.id">			
              <i-input  type="textarea" size="large" placeholder="请输入维度" />
              <i-button @click='delDimension(index)'>删除</i-button>		
            </formitem>
          </ul>     
        <i-button type="primary" size="small" @click="questionList" >下一步</i-button>
     </form>
  </div>
</template>

<script>
export default {
  data () {
    return {
	  lists: [
        {}
      ]

    }
  },

  methods: {
    questionList () {
      wx.navigateTo({
        url: '../question_list/main'
      })
    },
    addDimension () {
      console.log(this.lists)
		  let cope = {
        index: ''
      }
      this.lists.push({})
	  },
    delDimension (index) {
      this.lists.splice(index, 1)
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
