<template>  
  <div class="img" :style="{backgroundImage: 'url(' + img + ')' }">
    <div class="start">        
      <Button :size='buttonSize' shape='circle' type="success" to="/CreateEvaluation">
        开始使用
      </Button>
      <p>欢迎使用测评</p> 
    </div>
  </div> 
</template>

<script>
import Img from '@/assets/Welcome.png'

export default {
  data () {
    return {
      buttonSize: 'large',
      img: Img,
    }
  }
}
</script>

<style>
.img{
  background-position: center center;
  background-repeat:  no-repeat;
  background-size: auto auto;
}
.start{
  width: 100%;
  height: 700px;
  text-align:center;
}
p{
  font-size: 50px;
  text-aligh: center;
  margin-top:200px; 
  color: green;
}
.ivu-btn {
  font-size: 20px;
}
</style>