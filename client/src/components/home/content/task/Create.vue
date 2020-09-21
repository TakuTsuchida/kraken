<template>
  <v-row>
    <v-col>
      <v-card>
        <v-card-title class="headline">Task Registor</v-card-title>
        <v-card-text>
          <v-row>
            <v-col>
              <v-text-field
                v-model="title"
                :counter="30"
                label="Title"
                required/>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-textarea
                v-model="description"
                :counter="1000"
                label="Description"
                rows="4"
                required/>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-text-field
                v-model="deadline"
                label="Deadline"
                type="date"
                data-date-format="DD MMMM YYYY"
                required/>
            </v-col>
            <v-col>
              <v-slider
                v-model="importance"
                label="Importance"
                :max="10"
                :min="1"
                :color="color"
                track-color="grey"
                required/>
            </v-col>
          </v-row>
        </v-card-text>
        <v-card-actions class="justify-center">
            <v-btn color="#1565C0" dark large v-on:click="submit">REGISTOR</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import { mapActions } from 'vuex';
import importance from '@/modules/color';
export default {
  name: 'TaskCreate',
  computed: {
    color() {
      return importance(this.importance);
    },
    title: {
      get() { return this.$store.state.task.title },
      set(val) { return this.$store.commit('task/setTitle', val) },
    },
    description: {
      get() { return this.$store.state.task.description },
      set(val) { return this.$store.commit('task/setDescription', val) },
    },
    deadline: {
      get() { return this.$store.state.task.deadline },
      set(val) { return this.$store.commit('task/setDeadline', val) },
    },
    importance: {
      get() { return this.$store.state.task.importance },
      set(val) { return this.$store.commit('task/setImportance', val) },
    },
  },
  created() {
    this.deadline = this.today();
  },
  methods: {
    ...mapActions(
      'task',
      ['onPost']),
    today() {
      var dt = new Date();
      var y = dt.getFullYear();
      var m = ("00" + (dt.getMonth()+1)).slice(-2);
      var d = ("00" + dt.getDate()).slice(-2);
      return y + "-" + m + "-" + d;
    },
    submit() {
      this.onPost();
    },
  },
}
</script>