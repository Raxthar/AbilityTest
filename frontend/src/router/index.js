import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import AddEvaluationTitle from '@/components/AddEvaluationTitle'
import AddDimensions from '@/components/AddDimensions'
import CreateEvaluation from '@/components/CreateEvaluation'
import QuestionList from '@/components/QuestionList'
import AddQuestion from '@/components/AddQuestion'
import Welcome from '@/components/Welcome'

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
      path: '/AddEvaluationTitle/:u_id',
      name: 'AddEvaluationTitle',
      component: AddEvaluationTitle
    },
    {
      path: '/AddDimensions/:t_id/:u_id',
      name: 'AddDimensions',
      component: AddDimensions
    },
    {
      path: '/CreateEvaluation',
      name: 'CreateEvaluation',
      component: CreateEvaluation
    },
    {
      path: '/QuestionList/:t_id/:u_id',
      name: 'QuestionList',
      component: QuestionList
    },
    {
      path: '/AddQuestion/:t_id/:u_id',
      name: 'AddQuestion',
      component: AddQuestion
    },
    {
      path: '/Welcome',
      name: 'Welcome',
      component: Welcome
    }
  ]
})
