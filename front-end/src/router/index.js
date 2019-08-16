import Vue from 'vue'
import Router from 'vue-router'
import signin from '@/components/Signin'
import register from '@/components/Register'

Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name: 'signin',
      component: signin
    },
    {
      path: '/signin',
      name: 'signin',
      component: signin
    },
    {
      path: '/register',
      name: 'register',
      component: register
    }
  ]
})
