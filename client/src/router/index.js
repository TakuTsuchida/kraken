import Vue from 'vue';
import Router from 'vue-router';

import Auth from '@/router/auth'
// import Home from '@/components/pages/Home'

Vue.use(Router)

export default new Router({
  routes: [
    {...Auth},
  ]
})
