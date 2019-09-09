import Vue from 'vue'
import Router from 'vue-router'
import signin from '@/components/Signin'
import register from '@/components/Register'
import news from '@/components/News'
import recommendation from '@/components/Recommendation'
import exhibition from '@/components/Exhibition'
import test from '@/components/test'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'signin',
      component: signin,
      //redirect: '/signin',
      meta: {
        login_require: false
      },
    },
    {
      path: '/signin',
      name: 'signin',
      component: signin,
      meta: {
        login_require: false
      },
    },
    {
      path: '/register',
      name: 'register',
      component: register,
      meta: {
        login_require: false
      },
    },
    {
      path: '/news',
      name: 'news',
      component: news,
      meta: {
        login_require: false
      },
    },
    {
      path: '/recommendation',
      name: 'recommendation',
      component: recommendation,
      meta: {
        login_require: false
      },
    },
    {
      path: '/exhibition',
      name: 'exhibition',
      component: exhibition,
      meta: {
        login_require: false
      },
    }
  ]
})

