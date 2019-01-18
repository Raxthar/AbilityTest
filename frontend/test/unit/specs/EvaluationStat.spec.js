import Vue from 'vue'
import EvaluationStat from '@/components/EvaluationStat'
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

describe('EvaluationStat.vue', () => {
  it('组件加载后，多个初始值为空', () => {
    const wrapper = mount(EvaluationStat, {
      mocks: {
        $route
      }
    })
    expect(wrapper.vm.resultId.length).to.equal(0)
    expect(wrapper.vm.resultName.length).to.equal(0)
    expect(wrapper.vm.csvData.length).to.equal(0)
    expect(wrapper.vm.pNumber.length).to.equal(0)
    expect(wrapper.vm.dName.length).to.equal(0)
    expect(wrapper.vm.tableData.length).to.equal(0)
  })

  it('点击导出后, exportCsv函数被调用', () => {
    const wrapper = mount(EvaluationStat, {
      mocks: {
        $route
      }
    })
    const clickMethodStub = sinon.stub()
    wrapper.setMethods({ exportCsv: clickMethodStub })
    const submitButton = wrapper.find('#exportButton')
    submitButton.trigger('click')
    expect(clickMethodStub.called).to.equal(true)
  })

  it('组件加载后，table需要使用的columns数组长度为2', () => {
    const wrapper = mount(EvaluationStat, {
      mocks: {
        $route
      }
    })
    expect(wrapper.vm.columns.length).to.equal(2)
  })

  it('点击返回按钮后, jumpBack函数被调用', () => {
    const wrapper = mount(EvaluationStat, {
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
