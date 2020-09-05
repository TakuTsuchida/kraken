import Home from '@/components/home/Index'
import Task from '@/components/home/pages/Task'
// import  from '@/components/organisums/account/Task'

export default {
  path: '/home',
  component: Home,
  children: [
    {
      path: 'task',
      component: Task,
    },
  ],
}