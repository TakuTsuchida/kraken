<template>
  <v-container fluid>
    <task-create/>
  </v-container>
</template>

<script>
import TaskCreate from '@/components/home/content/task/Create.vue'

export default {
  name: 'TaskCreatePage',
  components: {
    TaskCreate,
  },
}
</script>