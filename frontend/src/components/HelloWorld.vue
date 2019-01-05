<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Essential Links</h2>
    <ul>
      <li>
        <a
          href="https://vuejs.org"
          target="_blank"
        >
          Core Docs
        </a>
      </li>
      <li>
        <a
          href="https://forum.vuejs.org"
          target="_blank"
        >
          Forum
        </a>
      </li>
      <li>
        <a
          href="https://chat.vuejs.org"
          target="_blank"
        >
          Community Chat
        </a>
      </li>
      <li>
        <a
          href="https://twitter.com/vuejs"
          target="_blank"
        >
          Twitter
        </a>
      </li>
      <br>
      <li>
        <a
          href="http://vuejs-templates.github.io/webpack/"
          target="_blank"
        >
          Docs for This Template
        </a>
      </li>
    </ul>
    <h2>Ecosystem</h2>
    <ul>
      <li>
        <a
          href="http://router.vuejs.org/"
          target="_blank"
        >
          vue-router
        </a>
      </li>
      <li>
        <a
          href="http://vuex.vuejs.org/"
          target="_blank"
        >
          vuex
        </a>
      </li>
      <li>
        <a
          href="http://vue-loader.vuejs.org/"
          target="_blank"
        >
          vue-loader
        </a>
      </li>
      <li>
        <a
          href="https://github.com/vuejs/awesome-vue"
          target="_blank"
        >
          awesome-vue
        </a>
      </li>
    </ul>
    <div id="myChart" :style="{width: '300px', height: '300px'}"></div>
    <div><Table :columns="columns1" :data="data1"></Table></div>
  </div>
</template>

<script>
  //引入基本模板
  let echarts = require('echarts/lib/echarts')
  //引入柱状图组件
  require('echarts/lib/chart/bar')
  require('echarts/lib/component/tooltip')
  require('echarts/lib/component/title')
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      columns1: [
        {
            title: 'No',
            key: 'no'
        },
        {
            title: 'Book_name',
            key: 'book_name'
        },
        {
            title: 'Add_Time',
            key: 'add_time'
        }
      ],
      data1: []
    }
  },
  mounted() {
    this.drawLine()
    this.showBooks()
  },
  methods: {
    drawLine() {
      //基于准备好的dom，初始化echarts示例
      let myChart = echarts.init(document.getElementById('myChart'))
      //绘制图表
      myChart.setOption({
        title: { text: '示例'},
        tooltip: {},
        xAxis: {
          data:["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        },
        yAxis: {},
        series:[{
          name: '销量',
          type: 'bar',
          data: [5, 20, 36, 10, 10, 20]
        }]
      });
    },
    showBooks () {
      this.axios
        .get('http://127.0.0.1:8000/api/show_books')
        .then((response) => {
          let res = response.data
          console.log(res)
          if(res['error_num'] === 0) {
            let list  = res['list']
            for(let a in list) {
              let obj = {
                no: list[a].pk,
                book_name: list[a].fields.book_name,
                add_time: list[a].fields.add_time,
              }
              this.data1.push(obj)
            }
          } else {
            this.$Message.error("读取失败")
          }
        })
        .catch((error) => {
          console.log(error)
        })
        .finally(() => this.loading = false)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
