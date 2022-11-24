<template>
    <div>
        <h1>Firebase Testing</h1>
        <ul>
            <li v-for="todo in todos"
                :key="todo.id">
                <span>{{ todo.id }}</span>
            </li>
        </ul>
        <button @click="add">ADD</button>
    </div>
</template>

<script setup lang="ts">
import { useCollection, useFirestore } from 'vuefire'
import { collection } from 'firebase/firestore'
import axios from 'axios';

const db = useFirestore()
const todos = useCollection(collection(db, 'todos'))

const add = async () => {
    console.log("Adding");

    const data = { message: "hello" }

    const res = await axios.post("https://personal-trainer-beta-default-rtdb.asia-southeast1.firebasedatabase.app/test.json", data)

    console.log(res)
    // await axios.post("https://personal-trainer-beta-default-rtdb.asia-southeast1.firebasedatabase.app", data)
}

</script>