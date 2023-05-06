<template>
    <NavBar />
    <div class="profile-page">

        <div class="title">
            <h1>Profile</h1>
        </div>
        <div class="main">

            <div class="profile-inner">
                <div class="profile-card">

                    <Card>
                        <template #header>
                            <img alt="user header"
                                :src="store.state.user?.photoURL || ''">
                        </template>
                        <template #title>
                            {{ store.state.user?.displayName || 'empty' }}
                        </template>
                        <template #content>
                            <div class="user-rank">
                                @member
                            </div>

                        </template>
                        <template #footer>
                            <div class="profile-badges">
                                <BadgeView label="Last Month"
                                    :value=lastMonthCount />
                                <BadgeView label="Past 7 Days"
                                    :value=countSum />
                            </div>
                        </template>
                    </Card>
                </div>
            </div>

            <div>
                <h2>My progress</h2>
            </div>
            <div class="week-chart-container">
                <Chart type="line"
                    style="height: 100%; width: 100%"
                    :data="basicData"
                    :options="basicOptions" />
            </div>

            <input type="text"
                v-model="inputText" />
            <p-Button label="Add"
                @click="addFireStore"></p-Button>
            <h3>
                <br>
                <div v-for="(value, index) in u_progess"
                    :key="index">
                    {{ value }}
                    <p-Button class="p-button-danger"
                        @click="deleteDocument(value.id)">Del</p-Button>

                    <p-Button class="p-button-success"
                        @click="deleteDocument(value.id)">TMP</p-Button>

                </div>


                <hr>
                <div>



                </div>
            </h3>
        </div>
    </div>
    <p-Button label="Toast"
        @click="showToast"></p-Button>




    <Toast />
</template>

<style scoped>
@import "@/assets/css/profile.css";

h1,
h2,
h3 {
    color: antiquewhite;
}
</style>


<script setup lang="ts">
import { ref, onMounted, onBeforeMount } from "vue";

import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

import Card from 'primevue/card';
import ProgressBar from 'primevue/progressbar';
import Toast from 'primevue/toast';
import { useToast } from "primevue/usetoast";
import Chart from 'primevue/chart';

import NavBar from "@/components/NavBar.vue";
import ProgressCard from "@/components/ProgressCard.vue";
import BadgeView from "@/components/BadgeView.vue";


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



const store = useStore();

const testInt = ref(230);


const db = getFirestore();
const _collection = collection(db, "u_progess");
const u_progess = useCollection(collection(db, 'u_progess'))
// const time_line = useCollection(collection(db, `u_progess/${store.state.user?.uid || ""}`))

const countSum = ref(0);
const lastMonthCount = ref(0);
const basicData = ref();
const pushUps = ref([null]);

onBeforeMount(async () => {
    await getExcercises();
})




const inputText = ref("");

const toast = useToast();
const toast_message = ref({});
const emptyList = ref([{}]);



const basicOptions = ref({
    plugins: {
        legend: {
            labels: {
                color: '#495057'
            }
        }
    },
    responsive: true,
    maintainAspectRatio: false,
    scales: {
        x: {
            ticks: {
                color: 'whitesmoke'
            },
            grid: {
                color: '#495057'
            }
        },
        y: {
            ticks: {
                // color: '#495057'
            },
            grid: {
                // color: '#ebedef'
            }
        }
    }
})


const squats = ref({ count: [null], date: [""] });

const getTimeRanges = (weekOffset: number, monthOffset: number) => {
    const pastWeek = new Date();
    pastWeek.setDate(pastWeek.getDate() - weekOffset);

    const startOfMonth = new Date();
    startOfMonth.setMonth(startOfMonth.getMonth() - monthOffset);
    startOfMonth.setDate(1);
    startOfMonth.setHours(0, 0, 0, 0);

    const endOfMonth = new Date();
    endOfMonth.setDate(0);
    endOfMonth.setHours(23, 59, 59, 999);
    return { pastWeek, startOfMonth, endOfMonth };
}

const getExcercises = async () => {
    const { pastWeek, startOfMonth, endOfMonth } = getTimeRanges(7, 1);



    const docRef = doc(db, "u_progess", store.state.user?.uid);

    const subcollection = await collection(
        docRef,
        "timeline"
    )

    const __docs = await getDocs(subcollection);


    __docs.forEach((doc) => {
        if (doc.data().code == "e01") {
            pushUps.value.push(doc.data().count)
        } else if (doc.data().code == "e02") {
            squats.value.count.push(doc.data().count)
            const date = new Date(doc.data().timeCreated);
            const t_label = `${date.getMonth() + 1}/${date.getDate()} ${date.getHours()}:${date.getMinutes()}`;
            squats.value.date.push(t_label)


            if (date >= pastWeek && date <= new Date()) {
                countSum.value += doc.data().count;
            } else if (date >= startOfMonth && date <= endOfMonth) {
                lastMonthCount.value += doc.data().count;
            }

        }
    })



    basicData.value = ({
        labels: squats.value.date.slice(-5),
        // labels: Array.from(Array(pushUps.value.length).keys()),
        datasets: [
            //     {
            //         label: label,
            //         borderColor: '#42A5F5',
            //         backgroundColor: '#42A5F515',
            //         fill: true,
            //         tension: .4,
            //         data: pushUps.value
            //     },
            {
                label: 'Squats',
                fill: true,
                borderColor: '#FFA726',
                backgroundColor: 'rgba(255,167,38,0.2)',
                tension: .4,
                data: squats.value.count.slice(-5)
            }
        ]
    })

}


const showToast = async () => {
    toast.add({ severity: 'info', summary: 'Info Message', detail: 'Message Content', life: 3000 });

    // const snapshot = await getDocs(query(_collection, where("content", "==", "Adrian")));
    await getDocs(query(_collection, where(documentId(), "==", store.state.user?.uid))).then(snapshot => {
        snapshot.forEach(doc => {
            console.log(`${doc.id}: ${doc.data().uid}`);
        })
    })


    console.log(emptyList.value);   //
    // result.value = emptyList;

}


const deleteDocument = async (doc_id: string) => {
    const document = doc(db, "u_progess", doc_id);

    console.log(doc_id);
    await deleteDoc(document)



        ;
}

const addFireStore = (input: string) => {
    console.log("add fire store")
    const date = new Date();


    try {

        setDoc(doc(db, "u_progess", store.state.user?.uid), {
            lastUpdated: date.getTime(),
            displayName: store.state.user.displayName,
            uid:
                store.state.user?.uid
            ,
            content: inputText.value,
        });


        setDoc(doc(db, `u_progess/${store.state.user?.uid}/timeline`, date.getTime().toString()), {
            timeCreated: date.getTime(),
            // displayName: store.state.user.displayName,
            code: "e02",
            title: "squat",
            count: 10,
        });



        toast_message.value = {
            severity: 'success',
            summary: "Sucess!",
            detail: "Document added",
            life: 3000,
        };
    } catch (error: any) {
        toast_message.value = {
            severity: 'error',
            summary: "Firebase Error",
            detail: error.message,
            life: 3000,
        };
    }

    toast.add(
        toast_message.value
    )

    inputText.value = "";

}



</script>
