import Vue from 'vue'
import App from './index'
const app = new Vue(App)
app.$mount()
export default {
  'usingComponents': {
    'i-button': '/node_modules/iview-weapp/dist/button/index',
    'i-modal': '../../../node_modules/iview-weapp/dist/modal/index',
    'i-row': '../../../node_modules/iview-weapp/dist/row/index',
    'i-col': '../../../node_modules/iview-weapp/dist/col/index',
    'i-action-sheet': '../../../static/iview/action-sheet/index',
    'i-message': '../../../static/iview/message/index'
  }
}
