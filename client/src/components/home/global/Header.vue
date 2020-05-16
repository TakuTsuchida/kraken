<template>
    <v-app-bar color="#263238" dense dark max-height="48px">
        <v-btn icon>
            <v-icon>{{ mdiHomeOutline }}</v-icon>
        </v-btn>
        <v-toolbar-title>Home</v-toolbar-title>
        <v-spacer/>
        <v-btn dark outlined v-on:click="submit">Logout</v-btn>
    </v-app-bar>
</template>
<script>
import { mdiHomeOutline } from '@mdi/js'
import { mapActions} from 'vuex'

export default {
  data() {
      return {
          mdiHomeOutline,
      };
  },
  methods: {
      ...mapActions(
          'auth',
          ['logout'],
      ),
      submit() {
          this.logout();
      },
  },
}
</script>