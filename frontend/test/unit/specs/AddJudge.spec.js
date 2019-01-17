import Vue from 'vue'
import AddJudge from '@/components/AddJudge'
import { mount } from 'vue-test-utils'
import sino from 'sinon'
import Router from 'vue-router'
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
      }})
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
})