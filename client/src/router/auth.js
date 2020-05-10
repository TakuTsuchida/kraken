import Auth from '@/components/auth/Index.vue'
import Signin from '@/components/auth/pages/Signin.vue'
import Signup from '@/components/auth/pages/Signup.vue'

export default {
  path: '/auth',
  component: Auth,
  children: [
    {
      path: 'signin',
      component: Signin,
    },
    {
      path: 'signup',
      component: Signup,
    },
  ],
}