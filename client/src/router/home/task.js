import TaskListPage from '@/components/home/pages/task/List.vue';
import TaskCreatePage from '@/components/home/pages/task/Create.vue';

const Task = [
    {
       path: 'task',
       component: TaskListPage,
    },
    {
       path: 'task/create',
       component: TaskCreatePage,
    },
]

export default Task;