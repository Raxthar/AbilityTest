import Vue from 'vue'
import DimensionsEdit from '@/components/DimensionsEdit'
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

describe('DimensionsEdit.vue', () => {
    it('点击添加维度按钮，数组长度加1', () => {
      const wrapper = mount(DimensionsEdit, {
      mocks: {
        $route
      }})
      wrapper.setData({
        buttonSize: 'large',
        uId: 1,
        dimensions: {
            dimensionId: [],
            dimensionName: [],
            tId: 1
        }
      })
      const addButton = wrapper.find('#addButton')
      const dimensionArrayBefore = wrapper.vm.dimensions.dimensionName
      const beforeLength = dimensionArrayBefore.length
      addButton.trigger('click')
      const dimensionArrayAfter = wrapper.vm.dimensions.dimensionName
      const afterLength = dimensionArrayAfter.length
      expect(afterLength).to.equal(beforeLength + 1)
    })

    it('点击删除维度按钮，数组长度减1', () => {
        const wrapper = mount(DimensionsEdit, {
        mocks: {
          $route
        }})
        wrapper.setData({
          buttonSize: 'large',
          uId: 1,
          dimensions: {
              dimensionId: [],
              dimensionName: [{index: ''}],
              tId: 1
          }
        })
        const addButton = wrapper.find('#delButton')
        const dimensionArrayBefore = wrapper.vm.dimensions.dimensionName
        const beforeLength = dimensionArrayBefore.length
        addButton.trigger('click')
        const dimensionArrayAfter = wrapper.vm.dimensions.dimensionName
        const afterLength = dimensionArrayAfter.length
        expect(afterLength).to.equal(beforeLength - 1)
      })

      it('点击添加维度按钮，组件数量增加', () => {
        const wrapper = mount(DimensionsEdit, {
        mocks: {
          $route
        }})
        wrapper.setData({
          buttonSize: 'large',
          uId: 1,
          dimensions: {
              dimensionId: [],
              dimensionName: [],
              tId: 1
          }
        })
        const addButton = wrapper.find('#addButton')
        const inputObj = wrapper.find('Input')
        const objLength = Object.keys(inputObj).length
        addButton.trigger('click')
        const inputObjAfter = wrapper.find('Input')
        const objLengthAfter = Object.keys(inputObjAfter).length
        expect(objLengthAfter).to.equal(objLength + 4)
      })

      it('点击删除维度按钮，组件数量减少', () => {
        const wrapper = mount(DimensionsEdit, {
        mocks: {
          $route
        }})
        wrapper.setData({
          buttonSize: 'large',
          uId: 1,
          dimensions: {
              dimensionId: [],
              dimensionName: [{index: ''}],
              tId: 1
          }
        })
        const addButton = wrapper.find('#delButton')
        const inputObj = wrapper.find('Input')
        const objLength = Object.keys(inputObj).length
        addButton.trigger('click')
        const inputObjAfter = wrapper.find('Input')
        const objLengthAfter = Object.keys(inputObjAfter).length
        expect(objLengthAfter).to.equal(objLength - 4)
      })
})