import Vue from 'vue'
// import Bootstrapvue from 'bootstrap-vue'
import Router from 'vue-router'

import OgiStories from '@/components/OgiStories'
import TankaList from '@/components/TankaList'
import Tanka from '@/components/Tanka'

// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'OgiStories',
      component: OgiStories
    },
    {
      path: '/tanka/:id',
      name: 'Tanka',
      component: Tanka
    },
    {
      path: '/tanka',
      name: 'TankaList',
      component: TankaList
    }
  ],
  scrollBehavior (to, from, savedPosition) {
    // if (savedPosition) { return savedPosition }
    return { x: 0, y: 0 }
  }
})
