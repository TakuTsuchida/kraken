<template>
  <v-container fluid>
    <task-list/>
  </v-container>
</template>

<script>
import TaskList from '@/components/home/content/task/List.vue';

export default {
  name: 'TaskListPage',
  components: {
    TaskList,
  },
}
</script>