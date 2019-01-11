<template>
  <div>
    <form :model="createData">
      <i-panel title="测评标题">
      <i-input v-model="createData.t_name" type="title"  mode="wrapped"/>
      </i-panel>
      <i-panel title="测评内容介绍">
        <i-input v-model="createData.t_describe" type="textarea" autosize="{minRows: 3,maxRows: 5}" mode="wrapped"/>
      </i-panel>
      <i-panel>
        <i-button :size="buttonSize" type="primary" shape="circle" @click="handleCreate" >下一步</i-button>
      </i-panel>
      </form>
  </div>
</template>

<script>

export default {
  data () {
    return {
      buttonSize: 'large',
      createData: {
        u_id: 1,
        t_name: '',
        t_describe: ''
      }
    }
  },

  methods: {
    handleCreate () {
      if (this.createData.t_name === '') {
        this.$Message.info('请输入标题')
        return
      }
      if (this.createData.t_describe === '') {
        this.$Message.info('请输入描述')
        return
      }
      wx.request({
        url: 'create/', // 仅为示例，并非真实的接口地址
        data: {
          x: '',
          y: ''
        },
        header: {
          'content-type': 'application/json' // 默认值
        },
        success (res) {
          console.log(res.data)
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
</style>
