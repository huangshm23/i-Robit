import Vue from 'vue'
import Router from 'vue-router'
import signin from '@/components/Signin'
import register from '@/components/Register'
import questionaire from '@/components/Questionaire'
import news from '@/components/News'
import recommendation from '@/components/Recommendation'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'signin',
      component: signin,
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
      path: '/questionaire',
      name: 'questionaire',
      component: questionaire
    },
    {
      path: '/news',
      name: 'news',
      component: news,
      meta: {
        login_require: true
      },
    },
    {
      path: '/recommendation',
      name: 'recommendation',
      component: recommendation,
      meta: {
        login_require: true
      },
    }
  ]
})

