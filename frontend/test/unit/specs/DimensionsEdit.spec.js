import Vue from 'vue'
import DimensionsEdit from '@/components/DimensionsEdit'
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

describe('DimensionsEdit.vue', () => {
  it('点击提交后, editDimension函数被调用', () => {
    const wrapper = mount(DimensionsEdit, {
      mocks: {
        $route
      }
    })
    const clickMethodStub = sinon.stub()
    wrapper.setMethods({ editDimension: clickMethodStub })
    const submitButton = wrapper.find('#submitButton')
    submitButton.trigger('click')
    expect(clickMethodStub.called).to.equal(true)
  })

  it('点击返回按钮后, jumpBack函数被调用', () => {
    const wrapper = mount(DimensionsEdit, {
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

  it('组件加载后，多个初始对象数组为空', () => {
    const wrapper = mount(DimensionsEdit, {
      mocks: {
        $route
      }
    })
    expect(wrapper.vm.dimensions.dimensionId.length).to.equal(0)
    expect(wrapper.vm.dimensions.dimensionName.length).to.equal(0)
  })
})
