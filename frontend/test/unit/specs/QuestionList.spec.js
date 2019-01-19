import Vue from 'vue'
import QuestionList from '@/components/QuestionList'
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

describe('QuestionList.vue', () => {
  it('组件加载后，多个初始值为空', () => {
    const wrapper = mount(QuestionList, {
      mocks: {
        $route
      }
    })
    expect(wrapper.vm.questionId.length).to.equal(0)
    expect(wrapper.vm.questionName.length).to.equal(0)
    expect(wrapper.vm.questionData.length).to.equal(0)
  })

  it('点击返回按钮后, jumpBack函数被调用', () => {
    const wrapper = mount(QuestionList, {
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

  it('点击创建题目后, jumpToAddQuestion函数被调用', () => {
    const wrapper = mount(QuestionList, {
      mocks: {
        $route
      }
    })
    const clickMethodStub = sinon.stub()
    wrapper.setMethods({ jumpToAddQuestion: clickMethodStub })
    const submitButton = wrapper.find('#submitButton')
    submitButton.trigger('click')
    expect(clickMethodStub.called).to.equal(true)
  })
})
