// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import axios from 'axios'
import '../node_modules/element-ui/lib/theme-chalk/index.css'

Vue.config.productionTip = false
/* eslint-disable no-new */
Vue.use(ElementUI)
Vue.prototype.$http = axios;

const NotFound = { template: '<p>Page not found</p>' }
const Home = { template: '<p>home page</p>' }
const About = { template: '<p>about page</p>' }

const routes = {
  '/': Home,
  '/about': About
}

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
