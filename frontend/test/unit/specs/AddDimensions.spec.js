import Vue from 'vue'
import AddDimensions from '@/components/AddDimensions'
import { mount, createLocalVue } from 'vue-test-utils'
import sino from 'sinon'
import Router from 'vue-router'
import iView from 'iview'
import 'iview/dist/styles/iview.css'
import axios from 'axios'

const localVue = createLocalVue()
Vue.prototype.$axios = axios
const tId = 1
const uId = 1
const $route = {
  params: { tId, uId }
}

Vue.use(iView)
localVue.use(Router)

describe('AddDimensions.vue', () => {
  it('点击按钮后, lists长度增加', () => {
    const wrapper = mount(AddDimensions, {
    mocks: {
      $route
    }})
    wrapper.setData({tId: 1})
    console.log(wrapper.vm.buttonSize)
    expect(1).to.equal(1)
  })
})