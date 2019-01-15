<template>
  <Carousel autoplay>
    <Carousel-item>
      <div class="img" :style="{backgroundImage: 'url(' + img1 + ')' }">
        <div class="start">
          <Button :size='buttonSize' shape='circle' type="primary" to="/CreateEvaluation">
            开始使用
          </Button>
          <p>欢迎使用测评</p>
        </div>
      </div>
    </Carousel-item>
    <Carousel-item>
      <div class="img" :style="{backgroundImage: 'url(' + img1 + ')' }">
        <div class="start">
          <Button :size='buttonSize' shape='circle' type="primary" to="/CreateEvaluation">
            开始使用
          </Button>
          <p>提供最专业的测评</p>
        </div>
      </div>
    </Carousel-item>
    <Carousel-item>
      <div class="img" :style="{backgroundImage: 'url(' + img1 + ')' }">
        <div class="start">
          <Button :size='buttonSize' shape='circle' type="primary" to="/CreateEvaluation">
            开始使用
          </Button>
          <p>轻松拥有在线测评系统</p>
        </div>
      </div>
    </Carousel-item>
    <Carousel-item>
      <div class="img" :style="{backgroundImage: 'url(' + img1 + ')' }">
        <div class="start">
          <Button :size='buttonSize' shape='circle' type="primary" to="/CreateEvaluation">
            开始使用
          </Button>
          <p>简单易上手的测评平台</p>
        </div>
      </div>
    </Carousel-item>
  </Carousel>
</template>

<script>
import Img1 from '@/assets/Welcome.png'

export default {
  data () {
    return {
      buttonSize: 'large',
      img1: Img1
    }
  }
}
</script>

<style scoped>
.img {
  background-position: center center;
  background-repeat:  no-repeat;
  background-size: auto auto;
  width: 100%;
  height: 700px
}
.start {
  width: 100%;
  height: 700px;
  text-align:center
}
p {
  font-size: 50px;
  font-family: 楷体;
  text-align: center;
  margin-top:200px;
  color: blue
}
.ivu-btn {
  font-size: 20px
}
</style>
