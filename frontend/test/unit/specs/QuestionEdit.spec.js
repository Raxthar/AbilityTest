import Vue from 'vue'
import QuestionEdit from '@/components/QuestionEdit'
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

describe('QuestionEdit.vue', () => {
  it('组件加载后，多个初始值为空', () => {
    const wrapper = mount(QuestionEdit, {
      mocks: {
        $route
      }
    })
    expect(wrapper.vm.oldOptionData.length).to.equal(0)
    expect(wrapper.vm.dimensionsData.length).to.equal(0)
    expect(wrapper.vm.dimensionId.length).to.equal(0)
    expect(wrapper.vm.dimensionName.length).to.equal(0)
    expect(wrapper.vm.questionData.newOptionData.length).to.equal(0)
  })

  it('点击导出后, editQuestion函数被调用', () => {
    const wrapper = mount(QuestionEdit, {
      mocks: {
        $route
      }
    })
    const clickMethodStub = sinon.stub()
    wrapper.setMethods({ editQuestion: clickMethodStub })
    const submitButton = wrapper.find('#submitButton')
    submitButton.trigger('click')
    expect(clickMethodStub.called).to.equal(true)
  })

  it('组件加载后，多个字符串为空', () => {
    const wrapper = mount(QuestionEdit, {
      mocks: {
        $route
      }
    })
    const emptyStr = ''
    expect(wrapper.vm.oldQuestionName).to.equal(emptyStr)
    expect(wrapper.vm.questionData.newQuestionName).to.equal(emptyStr)
  })

  it('点击返回按钮后, jumpBack函数被调用', () => {
    const wrapper = mount(QuestionEdit, {
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
