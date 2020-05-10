<template>
    <v-app-bar color="#263238" dense dark max-height="48px">
        <v-btn icon>
            <v-icon>{{ mdiLockOutline }}</v-icon>
        </v-btn>
        <v-toolbar-title>Authentification</v-toolbar-title>
        <v-spacer/>
        <v-btn dark outlined to="/auth/signin">Sign in</v-btn>
        <v-btn dark outlined to="/auth/signup">Sign up</v-btn>
    </v-app-bar>
</template>
<script>
  import {
    mdiLockOutline,
  } from '@mdi/js'

  export default {
    data() {
        return {
            mdiLockOutline,
        }
    },
  }
</script>