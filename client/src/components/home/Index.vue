<template>
  <!-- App.vue -->
  <v-app>
    <!-- header -->
    <Header/>
    <!-- nav -->
    <Navigation/>
    <!-- content -->
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>
<script>
import { mapState, mapMutations } from 'vuex'
import router from '@/router/index'

import Header from '@/components/home/global/Header.vue'
import Navigation from '@/components/home/global/Navigation.vue'

export default {
  name: 'Home',
  components: {
    Header,
    Navigation,
  },
  methods: {
    ...mapMutations(
      'error',
      ['clearMessage']
    ),
  },
  computed: {
    ...mapState(
      'auth',
      ['token']
    ),
  },
  created() {
    if (!this.token) router.push('/auth/signin');
    this.clearMessage();
  },
}
</script>
