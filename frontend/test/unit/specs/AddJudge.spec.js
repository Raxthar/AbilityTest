import Vue from 'vue'
import AddJudge from '@/components/AddJudge'
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

describe('AddJudge.vue', () => {
  it('页面内组件数量由数据长度决定', () => {
    const wrapper = mount(AddJudge, {
      mocks: {
        $route
      }
    })
    wrapper.setData({
      judges: {
        dimensionId: [1, 2],
        dimensionName: ['内向', '外向'],
        judge: ['你很内向', '你很外向'],
        due: '2019-01-01',
        tId: 1
      }
    })
    const pArray = wrapper.find('p')
    const inputArray = wrapper.find('input')
    const pLength = Object.keys(pArray).length
    const inputLength = Object.keys(inputArray).length
    expect(pLength).to.equal(5)
    expect(inputLength).to.equal(5)
  })

  it('点击提交后, editJudge函数被调用', () => {
    const wrapper = mount(AddJudge, {
      mocks: {
        $route
      }
    })
    const clickMethodStub = sinon.stub()
    wrapper.setMethods({ editJudge: clickMethodStub })
    const submitButton = wrapper.find('#submitButton')
    submitButton.trigger('click')
    expect(clickMethodStub.called).to.equal(true)
  })

  it('组件加载后, 数组dimensionId和dimensionName为空', () => {
    const wrapper = mount(AddJudge, {
      mocks: {
        $route
      }
    })
    expect(wrapper.vm.judges.dimensionId.length).to.equal(0)
    expect(wrapper.vm.judges.dimensionName.length).to.equal(0)
  })

  it('点击返回按钮后, jumpBack函数被调用', () => {
    const wrapper = mount(AddJudge, {
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
