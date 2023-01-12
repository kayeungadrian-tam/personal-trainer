<template>
    <NavBar />

    <div class="memo-page">
        <div class="title">
            <h2>
                Memo
            </h2>
        </div>
        <div class="todos-list">
            <div v-for="(todo, i) in todos"
                :key="i"
                style="margin-top:20px">
                <Card>
                    <template #title>
                        {{ todo.author }}
                    </template>
                    <template #content>
                        {{ todo.content }}
                    </template>
                    <template #footer>
                        {{ todo.timeCreated }}
                    </template>
                </Card>
            </div>

        </div>


        <Dialog v-model:visible="display">
            <template #header>
                <h4>Add memo</h4>
            </template>
            <h2>Title</h2>
            <InputText type="text"
                style="width:100%"
                v-model="memoAuthor" />
            <h2>Memo</h2>
            <Textarea style="width:100%"
                v-model="memoContent"
                rows="5"
                cols="30" />
            <template #footer>
                <p-Button label="Cancel"
                    icon="pi pi-times"
                    class="p-button-text p-button-secondary" />
                <p-Button @click="addMemo"
                    label="Add"
                    icon="pi pi-check"
                    class="p-button-secondary"
                    autofocus />
            </template>
        </Dialog>
        <div class="memo-add-button">
            <p-Button @click="showPopup"
                class="p-button-lg p-button-warning p-button-rounded ">
                <i class="pi pi-fw pi-plus log-out-button"></i>
                Add
            </p-Button>
            <Toast />

        </div>
    </div>

</template>


<script setup lang="ts">
import { ref, onMounted } from 'vue';

import Textarea from 'primevue/textarea';
import InputText from 'primevue/inputtext';
import Dialog from 'primevue/dialog';
import Card from 'primevue/card';

import { useFirestore } from 'vuefire'
import { useCollection } from 'vuefire'
import { collection, addDoc } from 'firebase/firestore'

import NavBar from "@/components/NavBar.vue";

const db = useFirestore();
const todos = useCollection(collection(db, 'todos'))


const display = ref(false)



const memoAuthor = ref();
const memoContent = ref();

const memos = ref([
    {
        id: "1",
        content: "Create memo CRUD",
        author: "Adrian",
        status: "To-do",
    },
    {
        id: "2",
        content: "test",
        author: "Author",
        status: "Completed",
    }

])

const showPopup = () => {
    display.value = true;
}

const addMemo = () => {
    const date = new Date();

    addDoc(collection(db, 'todos'), {
        id: date.getTime(),
        author: memoAuthor.value,
        content: memoContent.value,
        timeCreated: date.getTime()
    });
    display.value = false;
    memoAuthor.value = "";
    memoContent.value = "";
}



</script>


<style scoped>
@import "@/assets/css/memoPage.css";
</style>