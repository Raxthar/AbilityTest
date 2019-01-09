import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import AddEvaluationTitle from '@/components/AddEvaluationTitle'
import AddDimensions from '@/components/AddDimensions'
import CreateEvaluation from '@/components/CreateEvaluation'
import QuestionList from '@/components/QuestionList'
import AddQuestion from '@/components/AddQuestion'
import Welcome from '@/components/Welcome'
import QuestionEdit from '@/components/QuestionEdit'
import ReleaseSuccess from '@/components/ReleaseSuccess'

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
      path: '/AddDimensions/:u_id/:t_id',
      name: 'AddDimensions',
      component: AddDimensions
    },
    {
      path: '/CreateEvaluation',
      name: 'CreateEvaluation',
      component: CreateEvaluation
    },
    {
      path: '/QuestionList/:u_id/:t_id',
      name: 'QuestionList',
      component: QuestionList
    },
    {
      path: '/AddQuestion/:u_id/:t_id',
      name: 'AddQuestion',
      component: AddQuestion
    },
    {
      path: '/Welcome',
      name: 'Welcome',
      component: Welcome
    },
    {
      path: '/QuestionEdit/:u_id/:t_id/:q_id',
      name: 'QuestionEdit',
      component: QuestionEdit
    },
    {
      path: '/ReleaseSuccess',
      name: 'ReleaseSuccess',
      component: ReleaseSuccess
    }
  ]
})
