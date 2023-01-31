<template>
    <Navbar />
    <div class="home">
        <div class="title">
            <h1>JUST DO IT!</h1>
        </div>
        <HelloWorld @count="chooseAnswer"
            @next="addFireStore" />
    </div>
    <p-Button label="Testing"
        @click="getFireStore"></p-Button>
    <Toast />
</template>

<script setup lang="ts">
// import CameraVue from '@/components/Camera.vue';

import { ref } from "vue";
import { useStore } from 'vuex'

import Toast from 'primevue/toast';
import { useToast } from "primevue/usetoast";

import Navbar from '@/components/NavBar.vue';
import HelloWorld from '@/components/HelloWorld.vue';

import getLastWeeksDate from "@/composables/time_utils";


import { useFirestore, useDocument, useCollection } from 'vuefire'
import {
    getFirestore,
    collection,
    // getCollecionts,
    doc,
    addDoc,
    deleteDoc,
    setDoc,
    getDoc,
    query,
    where,
    getDocs,
    documentId
} from 'firebase/firestore'
import { parseStringStyle } from "@vue/shared";

const store = useStore();
const db = getFirestore();
const toast = useToast();

const cnt = ref(0);
const toastMessage = ref({});

const chooseAnswer = (count: number) => {
    console.log(count)
    cnt.value += 1
}


const u_progess = useCollection(collection(db, 'u_progess'))


const past_data = ref([{}]);

const getFireStore = async () => {

    console.log("getFirestore")
    const weeks = getLastWeeksDate();

    const docRef = doc(db, "u_progess", store.state.user?.uid);
    const subcollection = await collection(
        docRef,
        "timeline"
    )



    const oneWeekAgo = new Date();
    oneWeekAgo.setDate(oneWeekAgo.getDate() - 7);
    console.log(oneWeekAgo.getTime())

    const __docs = await getDocs(subcollection);
    __docs.forEach((doc) => {

        if (parseInt(doc.id) >= oneWeekAgo.getTime()) {
            console.log(doc.data())
        }
        // past_data.value.push(tmp_data);
        // const tmp_date = new Date(parseInt(doc.id));

    })


    console.log(typeof weeks.at(0))

    // const past_stamp = past_data.value.filter(data => {
    //     const date = new Date(data.id);
    // })

    // const tmp = new Date(1673531983650);
    // console.log(tmp)

};

const addFireStore = () => {
    console.log("add fire store")
    const date = new Date()

    try {

        setDoc(doc(db, "u_progess", store.state.user?.uid), {
            lastUpdated: date.getTime(),
            displayName: store.state.user.displayName,
            uid:
                store.state.user?.uid
            ,
        })

        const timestamp = date.getTime().toString();

        setDoc(doc(db, `u_progess/${store.state.user?.uid}/timeline`, date.getTime().toString()), {
            timeCreated: date.getTime(),
            code: "e02",
            title: "squat",
            count: cnt.value,
        })
        cnt.value = 0

        toastMessage.value = { severity: 'success', summary: 'Data added', detail: 'Data has been added successfully.', life: 3000 };

    } catch (error: any) {
        toastMessage.value = { severity: 'error', summary: 'Info Message', detail: 'Message Content', life: 3000 };

        console.log(error)
    }
    toast.add(toastMessage.value);
}




</script>