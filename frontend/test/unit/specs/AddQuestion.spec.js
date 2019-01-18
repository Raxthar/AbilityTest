import Vue from 'vue'
import AddQuestion from '@/components/AddQuestion'
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

describe('AddQuestion.vue', () => {
  it('点击添加选项按钮，lists数据长度变长，组件数量增加', () => {
    const wrapper = mount(AddQuestion, {
      mocks: {
        $route
      }
    })
    wrapper.setData({
      dimensionsData: [{dName: '内向', dId: '1'}, {dName: '外向', dId: '2'}],
      dimensionId: [1, 2],
      dimensionName: ['内向', '外向'],
      questionData: {
        tId: 1,
        qName: '你是否惧怕上台讲话？',
        oName: {1: '怕', 2: '不怕'},
        dId: {1: '1', 2: '2'},
        score: {1: '100', 2: '100'}
      }
    })
    const addButton = wrapper.find('#addButton')
    const listsLength = wrapper.vm.lists.length
    addButton.trigger('click')
    const afterInputObj = wrapper.find('Input')
    const inputLengthAfter = Object.keys(afterInputObj).length
    const listsLengthAfter = wrapper.vm.lists.length
    expect(listsLengthAfter).to.equal(listsLength + 1)
    expect(inputLengthAfter).to.equal(5)
  })

  it('点击删除选项按钮，lists数据长度变短，组件数量减少', () => {
    const wrapper = mount(AddQuestion, {
      mocks: {
        $route
      }
    })
    wrapper.setData({
      dimensionsData: [{dName: '内向', dId: '1'}, {dName: '外向', dId: '2'}],
      dimensionId: [1, 2],
      dimensionName: ['内向', '外向'],
      questionData: {
        tId: 1,
        qName: '你是否惧怕上台讲话？',
        oName: {1: '怕', 2: '不怕'},
        dId: {1: '1', 2: '2'},
        score: {1: '100', 2: '100'}
      }
    })
    const delButton = wrapper.find('#delButton')
    const listsLength = wrapper.vm.lists.length
    delButton.trigger('click')
    const afterInputObj = wrapper.find('Input')
    const inputLengthAfter = Object.keys(afterInputObj).length
    const listsLengthAfter = wrapper.vm.lists.length
    expect(listsLengthAfter).to.equal(listsLength - 1)
    expect(inputLengthAfter).to.equal(5)
  })

  it('点击提交后, setQuestion函数被调用', () => {
    const wrapper = mount(AddQuestion, {
      mocks: {
        $route
      }
    })
    const clickMethodStub = sinon.stub()
    wrapper.setMethods({ setQuestion: clickMethodStub })
    const submitButton = wrapper.find('#submitButton')
    submitButton.trigger('click')
    expect(clickMethodStub.called).to.equal(true)
  })
})
