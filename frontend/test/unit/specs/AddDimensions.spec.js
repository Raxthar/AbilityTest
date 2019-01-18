import Vue from 'vue'
import AddDimensions from '@/components/AddDimensions'
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

describe('AddDimensions.vue', () => {
  it('点击添加维度按钮后, dimensions长度增加', () => {
    const wrapper = mount(AddDimensions, {
      mocks: {
        $route
      }
    })
    const addButton = wrapper.find('#addButton')
    const beforeLength = wrapper.vm.dimensionArray.dimensions.length
    addButton.trigger('click')
    const afterLength = wrapper.vm.dimensionArray.dimensions.length
    expect(afterLength).to.equal(beforeLength + 1)
  })

  it('点击删除维度按钮后, dimensions长度减少', () => {
    const wrapper = mount(AddDimensions, {
      mocks: {
        $route
      }
    })
    const addButton = wrapper.find('#delButton')
    const beforeLength = wrapper.vm.dimensionArray.dimensions.length
    addButton.trigger('click')
    const afterLength = wrapper.vm.dimensionArray.dimensions.length
    expect(afterLength).to.equal(beforeLength - 1)
  })

  it('点击提交后, updateDimensions函数被调用', () => {
    const wrapper = mount(AddDimensions, {
      mocks: {
        $route
      }
    })
    const clickMethodStub = sinon.stub()
    wrapper.setMethods({ updateDimensions: clickMethodStub })
    const updateButton = wrapper.find('#updateButton')
    updateButton.trigger('click')
    expect(clickMethodStub.called).to.equal(true)
  })
})
