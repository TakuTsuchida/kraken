<template>
    <v-row justify="center" align-content="center">
        <v-col>
            <v-card class="mx-auto" max-width="400px" >
                <v-img class="white--text align-end" height="300px" src="https://www.tabikobo.com/special/zekkei/images/main.jpg">
                    <v-card-title>Sign up</v-card-title>
                </v-img>
                <v-card-text>
                    <v-text-field label="Email address" v-model="email"/>
                    <v-text-field label="Password" v-model="password"/> 
                </v-card-text>
                <v-card-actions class="justify-center">
                    <v-btn color="#1565C0" dark large v-on:click="submit">Register</v-btn>
                </v-card-actions>
            </v-card>
        </v-col>
    </v-row>
</template>

<script>
import { mapActions } from 'vuex'
export default {
    data() {
        return {
            email: '',
            password: '',
        };
    },
    methods: {
        ...mapActions(
            'auth',
            ['signUp']),
        submit() {
            const credential = {email: this.email, password: this.password};
            this.signUp(credential);
        },
    },
}
</script>