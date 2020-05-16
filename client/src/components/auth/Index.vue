<template>
    <v-app>
        <Header/>
        <v-content>
            <router-view/>
        </v-content>
    </v-app>
</template>

<script>
import Header from '@/components/auth/global/Header.vue'
export default {
    components: {
        Header,
    }
}
</script>