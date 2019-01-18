import Vue from 'vue'
import Router from 'vue-router'
import Welcome from '@/components/Welcome'
import AddEvaluationTitle from '@/components/AddEvaluationTitle'
import AddDimensions from '@/components/AddDimensions'
import CreateEvaluation from '@/components/CreateEvaluation'
import QuestionList from '@/components/QuestionList'
import AddQuestion from '@/components/AddQuestion'
import QuestionEdit from '@/components/QuestionEdit'
import ReleaseSuccess from '@/components/ReleaseSuccess'
import EvaluationEdit from '@/components/EvaluationEdit'
import DimensionsEdit from '@/components/DimensionsEdit'
import EvaluationStat from '@/components/EvaluationStat'
import AddJudge from '@/components/AddJudge'

Vue.use(Router)

export default new Router({
  model: 'hash',
  routes: [
    {
      path: '/',
      name: 'Welcome',
      component: Welcome
    },
    {
      path: '/AddEvaluationTitle/:uId',
      name: 'AddEvaluationTitle',
      component: AddEvaluationTitle
    },
    {
      path: '/AddDimensions/:uId/:tId',
      name: 'AddDimensions',
      component: AddDimensions
    },
    {
      path: '/CreateEvaluation',
      name: 'CreateEvaluation',
      component: CreateEvaluation
    },
    {
      path: '/QuestionList/:uId/:tId',
      name: 'QuestionList',
      component: QuestionList
    },
    {
      path: '/AddQuestion/:uId/:tId',
      name: 'AddQuestion',
      component: AddQuestion
    },
    {
      path: '/QuestionEdit/:uId/:tId/:qId',
      name: 'QuestionEdit',
      component: QuestionEdit
    },
    {
      path: '/ReleaseSuccess',
      name: 'ReleaseSuccess',
      component: ReleaseSuccess
    },
    {
      path: '/EvaluationEdit/:uId/:tId',
      name: 'EvaluationEdit',
      component: EvaluationEdit
    },
    {
      path: '/DimensionsEdit/:uId/:tId',
      name: 'DimensionsEdit',
      component: DimensionsEdit
    },
    {
      path: '/EvaluationStat/:tId',
      name: 'EvaluationStat',
      component: EvaluationStat
    },
    {
      path: '/AddJudge/:tId',
      name: 'AddJudge',
      component: AddJudge
    }
  ]
})
