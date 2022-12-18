<template>
    <div class="login-card">
        <Card>
            <template #title>
                <h2>
                    Welcome back
                </h2>
            </template>
            <template #content>
                <p class="welcome-message">Welcome back! Login or sign-up!</p>
                <div class="input">
                    <div class="p-inputgroup">
                        <span class="p-inputgroup-addon">
                            <i class="pi pi-user"></i>
                        </span>
                        <InputText v-model="email"
                            placeholder="Username or Email" />
                    </div>
                </div>

                <div class="input">
                    <div class="p-inputgroup">
                        <span class="p-inputgroup-addon">
                            <i class="pi pi-lock"></i>
                        </span>
                        <Password :toggleMask="true"
                            :feedback="false"
                            placeholder="Password"
                            v-model="password" />

                    </div>
                </div>




                <div class="social-login">
                    <div class="sign-in-button">
                        <p-Button @click="login"
                            label="Sign in" />
                    </div>
                    <div class="google-button">
                        <p-Button @click="LoginWithGoolge"
                            icon="pi pi-google"
                            label="Google" />

                    </div>
                </div>
            </template>
            <template #footer>
                <div class="login-card-footer">
                    Don't have an account? <span class="register">Register</span>
                </div>
            </template>
        </Card>

    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

import { database } from "@/firebase/config";

import { useFirestore } from 'vuefire'
import { useCollection } from 'vuefire'
import { collection } from 'firebase/firestore'

import Card from 'primevue/card';
import InputText from 'primevue/inputtext';
import Divider from 'primevue/divider';
import Password from 'primevue/password';

const db = useFirestore();
const todos = useCollection(collection(db, 'todos'))



const email = ref('')
const password = ref('')
const error = ref(null)

const store = useStore()


const router = useRouter()


const login = () => {
    store.state.user = "empty";
    router.push('/home')

}

const handleSubmit = async () => {
    try {
        await store.dispatch('login', {
            email: email.value,
            password: password.value
        })
        router.push('/')
    }
    catch (err) {
        // error.value = err.message
        console.error(err)
    }
}

const signup = async () => {
    try {
        await store.dispatch('signup', {
            email: email.value,
            password: password.value
        })
        router.push('/')
    }
    catch (err) {
        console.error(err)
    }
}
const LoginWithGoolge = async () => {
    try {
        await store.dispatch('goolgeLogin', {
        })
        router.push('/home')
    }
    catch (err) {
        console.error(err)
    }
}


</script>
