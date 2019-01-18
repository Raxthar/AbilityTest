import Vue from 'vue'
import EvaluationEdit from '@/components/EvaluationEdit'
import { mount } from 'vue-test-utils'
import iView from 'iview'
import 'iview/dist/styles/iview.css'
import axios from 'axios'

Vue.prototype.$axios = axios
const tId = 1
const uId = 1
const $route = {
  params: { tId, uId }
}

Vue.use(iView)

describe('EvaluationEdit.vue', () => {
  it('组件加载后，多个字符串为空', () => {
    const wrapper = mount(EvaluationEdit, {
      mocks: {
        $route
      }
    })
    const emptyStr = ''
    expect(wrapper.vm.evaluationData.evaluationName).to.equal(emptyStr)
    expect(wrapper.vm.evaluationData.evaluationDescribe).to.equal(emptyStr)
  })

  it('点击提交后, editEvaluation函数被调用', () => {
    const wrapper = mount(EvaluationEdit, {
      mocks: {
        $route
      }
    })
    const clickMethodStub = sinon.stub()
    wrapper.setMethods({ editEvaluation: clickMethodStub })
    const submitButton = wrapper.find('#submitButton')
    submitButton.trigger('click')
    expect(clickMethodStub.called).to.equal(true)
  })

  it('点击返回按钮后, jumpBack函数被调用', () => {
    const wrapper = mount(EvaluationEdit, {
      mocks: {
        $route
      }
    })
    const clickMethodStub = sinon.stub()
    wrapper.setMethods({ jumpBack: clickMethodStub })
    const submitButton = wrapper.find('#backButton')
    submitButton.trigger('click')
    expect(clickMethodStub.called).to.equal(true)
  })
})
