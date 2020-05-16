<template>
    <v-row justify="center" align-content="center">
        <v-col>
            <v-card class="mx-auto" max-width="400px" >
                <v-img class="white--text align-end" height="300px" src="https://cdn.vuetifyjs.com/images/cards/docks.jpg">
                    <v-card-title>Sign in</v-card-title>
                </v-img>
                <v-card-text>
                    <v-text-field label="Email address" v-model="email"/>
                    <v-text-field label="Password" v-model="password"/> 
                </v-card-text>
                <v-card-actions class="justify-center">
                    <v-btn color="#1565C0" dark large v-on:click="submit">LOG IN</v-btn>
                </v-card-actions>
            </v-card>
        </v-col>
    </v-row>
</template>
<script>
import { mapActions } from 'vuex';
export default {
    data() {
        return {
            email: '',
            password: '',
        }
    },
    methods: {
        ...mapActions(
            'auth',
            ['signIn']),
        submit() {
            const credential = {email: this.email, password: this.password};
            this.signIn(credential);
        },
    },
}
</script>