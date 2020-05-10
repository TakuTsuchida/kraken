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
import Header from '@/components/organisms/share/Header.vue'
import Navigation from '@/components/organisms/share/Navigation.vue'

export default {
  name: 'Home',
  components: {
    Header,
    Navigation,
  },
  created() {
    this.$store.commit('home/initMenuListFlg');
  },
}
</script>
