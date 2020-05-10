import Account from '@/components/templates/Account'
import  from '@/components/organisums/account/Index'
import  from '@/components/organisums/account/Task'

export default {
  path: '/account',
  component: Account,
  children: [
    {
      path: '',
      component: Index,
    },
    {
      path: 'signup',
      component: Signup,
    },
  ],
}