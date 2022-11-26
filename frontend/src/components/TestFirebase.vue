<template>
    <div>
        <h1>Firebase Testing</h1>
        <ul>
            <li v-for="todo in todos"
                :key="todo.id">
                <span>{{ todo.id }}</span>
            </li>
        </ul>
    </div>

    <form @submit.prevent="signup"
        class="mt-4 flex flex-col">
        <h3 class="text-xl underline">Login</h3>

        <label for="email">Email:</label>
        <input class="border w-4/12"
            type="email"
            name="email"
            v-model="email"
            required>

        <label for="email">Password:</label>
        <input class="border w-4/12"
            type="password"
            name="password"
            v-model="password"
            required>

        <button class="w-max mt-4 px-4 py-2 text-center rounded-full bg-blue-500 text-white">Login</button>
        <div v-if="error">{{ error }}</div>



    </form>

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
        // error.value = err.message
        console.error(err)
    }
}

// return { handleSubmit, email, password, error }

</script>