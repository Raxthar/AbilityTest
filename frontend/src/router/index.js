import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import AddEvaluationTitle from '@/components/AddEvaluationTitle'
import AddDimensions from '@/components/AddDimensions'
import CreateEvaluation from '@/components/CreateEvaluation'
import QuestionList from '@/components/QuestionList'

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
      path: '/AddEvaluationTitle/:uID',
      name: 'AddEvaluationTitle',
      component: AddEvaluationTitle
    },
    {
      path: '/AddDimensions/:tID/:uID',
      name: 'AddDimensions',
      component: AddDimensions
    },
    {
      path: '/CreateEvaluation',
      name: 'CreateEvaluation',
      component: CreateEvaluation
    },
    {
      path: '/QuestionList',
      name: 'QuestionList',
      component: QuestionList
    }
  ]
})
