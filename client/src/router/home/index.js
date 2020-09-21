import Home from '@/components/home/Index.vue';
import Task from '@/router/home/task.js';
// import  from '@/components/organisums/account/Task'

export default {
  path: '/home',
  component: Home,
  children: [
    ...Task,
  ],
}