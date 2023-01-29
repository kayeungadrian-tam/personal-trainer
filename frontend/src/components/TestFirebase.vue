<template>
    <div>
        <h1>Leaderboard</h1>
        <ul>

        </ul>
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

const db = useFirestore();
const todos = useCollection(collection(db, 'todos'))



const email = ref('')
const password = ref('')
const error = ref(null)

const store = useStore()


const router = useRouter()


const login = async () => {
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
        // error.value = err.message
        console.error(err)
    }
}
// goolgeLogin
const LoginWithGoolge = async () => {
    try {
        await store.dispatch('goolgeLogin', {
        })
        router.push('/home')
    }
    catch (err) {
        // error.value = err.message
        console.error(err)
    }
}

// return { handleSubmit, email, password, error }

</script>
