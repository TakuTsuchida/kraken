<template>
  <v-container fluid>
    <task-form/>
    <task-list/>
  </v-container>
</template>

<script>
import TaskList from '@/components/home/content/TaskList.vue'
import TaskForm from '@/components/home/content/TaskForm.vue'

export default {
  name: 'Task',
  components: {
    TaskList,
    TaskForm,
  },
}
</script>