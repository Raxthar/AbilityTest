import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import addtitle from '@/components/AddEvaluationTitle'
import adddims from '@/components/AddDimensions'

Vue.use(Router)

export default new Router({
  model: 'hash',
  routes: [
    {
      path: '/HelloWorld',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/addtitle',
      name: 'addtitle',
      component: addtitle
    },
    {
      path: '/adddims',
      name: 'adddims',
      component: adddims
    }
  ]
})
