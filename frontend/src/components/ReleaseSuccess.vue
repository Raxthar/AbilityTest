<template>
    <div class="start">
      <p>发布成功！</p>
      <div class="content">
      <Button :size='buttonSize' shape='circle' type="success" to="/">
        分享
      </Button><br><br><br><br><br><br>
      <Button :size='buttonSize' shape='circle' type="success" to="/CreateEvaluation">
        返回测评列表
      </Button>
      </div>
    </div>
</template>

<script>
export default {
  data () {
    return {
      buttonSize: 'large'
    }
  }
}
</script>

<style scoped>
.start{
  width: 100%;
  height: 700px;
  text-align:center;
}
p{
  font-size: 50px;
  text-align: center;
  margin-top:50px;
  color: red;
}
.ivu-btn {
  font-size: 20px;
}
.content {
  margin-top:100px;
}
</style>
