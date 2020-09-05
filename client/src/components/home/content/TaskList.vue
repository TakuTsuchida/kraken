<template>
  <v-row>
    <v-col>
      <v-card>
        <v-card-title class="headline">Task List</v-card-title>
        <v-list two-line>
          <v-list-item-group>
            <template v-for="(item, index) in tasks">
              <v-list-item :key="item.title">
                <v-list-item-content>
                  <v-list-item-title v-text="item.title"></v-list-item-title>
                  <v-list-item-subtitle v-html="viewDescription(item.description)"></v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-action>
                  <v-list-item-action-text v-text="item.deadline"></v-list-item-action-text>
                  <v-icon :color="color(item.importance)">
                    {{star}}
                  </v-icon>
                  <v-btn icon v-on:click="onDelete(item.id)">
                    <v-icon>{{deleteIcon}}</v-icon>
                  </v-btn>
                </v-list-item-action>
              </v-list-item>
              <v-divider
                v-if="index + 1 < tasks.length"
                :key="index"
              ></v-divider>
            </template>
          </v-list-item-group>
        </v-list>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import { mdiStar, mdiDelete } from '@mdi/js'
import { mapActions } from 'vuex'
export default {
  data () {
    return {
      star: mdiStar,
      deleteIcon: mdiDelete,
    };
  },
  computed: {
    tasks: {
      get() { return this.$store.state.task.tasks},
    },
  },
  methods: {
    ...mapActions(
      'task',
      ['onGetAll', 'onDelete']
    ),
    color(importance) {
      if (importance < 3) return 'indigo';
      if (importance < 5) return 'teal';
      if (importance < 7) return 'green';
      if (importance < 9) return 'orange';
      return 'red';
    },
    viewDescription(desc) {
      const splited = desc.split('\n');
      if (splited.length > 2) {
        splited.splice(2);
        splited.push('...');
      }
      return splited.join('<br>');
    },
  },
  created() {
    this.onGetAll();
  }
}
</script>