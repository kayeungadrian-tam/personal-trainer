<template>
    <NavBar />
    <div class="profile-page">

        <div class="title">
            <h1>Profile</h1>
        </div>


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
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error
                        repudiandae numquam deserunt
                        quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse,
                        cupiditate neque quas!
                    </template>
                    <template #footer>
                        <Button icon="pi pi-check"
                            label="Save" />
                        <Button icon="pi pi-times"
                            label="Cancel"
                            class="p-button-secondary"
                            style="margin-left: .5em" />
                    </template>
                </Card>
            </div>

            <div class="profile-progress">
                <ProgressCard />
            </div>


        </div>
        <div>
            <h1>Test Firebase</h1>
            <h2> ID:
                {{ store.state.user?.uid || "uu1234" }}
            </h2>

            <Chart type="line"
                style="height: 100%; width: 100%"
                :data="basicData"
                :options="basicOptions" />

            <p-Button label="Get"
                class="p-button-secondary"
                style="margin-left:"
                @click="getExcercises" />
            <br>
            <input type="text"
                v-model="inputText" />
            <p-Button label="Add"
                @click="addFireStore"></p-Button>
        </div>
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
                {{ tmpData }}



            </div>
            EOF
        </h3>

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
import { ref, onMounted } from "vue";

import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

import Card from 'primevue/card';
import ProgressBar from 'primevue/progressbar';
import Toast from 'primevue/toast';
import { useToast } from "primevue/usetoast";
import Chart from 'primevue/chart';

import NavBar from "@/components/NavBar.vue";
import ProgressCard from "@/components/ProgressCard.vue";

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



const router = useRouter()
const store = useStore();


const db = getFirestore();
const _collection = collection(db, "u_progess");
const u_progess = useCollection(collection(db, 'u_progess'))
// const time_line = useCollection(collection(db, `u_progess/${store.state.user?.uid || ""}`))


const basicData = ref();
const pushUps = ref([] as any);

onMounted(async () => {
    //   lastWeekLabels.value = await getLastWeeksDate();
    // lastWeekLabels.value = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];


    // await getExcercises();

})


const result = ref();


const inputText = ref("");

const tmpData = ref();
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



const getExcercises = async () => {


    const docRef = doc(db, "u_progess", store.state.user?.uid);

    const subcollection = await collection(
        // query(_collection, where(documentId(), "==", "test"))
        docRef,
        "timeline"
    )
        ;



    tmpData.value = useCollection(subcollection);

    tmpData.value.data.forEach(
        (doc: any) => pushUps.value.push(doc.count)
    )


    basicData.value = ({
        // labels: ['January', 'February', 'March'],
        // labels: lastWeekLabels.value,

        labels: Array.from(Array(pushUps.value.length).keys()),

        datasets: [
            {
                label: 'My First dataset',
                borderColor: '#42A5F5',
                backgroundColor: '#42A5F515',
                fill: true,
                tension: .4,
                data: pushUps.value
            },
            // {
            //     label: 'My Second dataset',
            //     fill: true,
            //     borderColor: '#FFA726',
            //     backgroundColor: 'rgba(255,167,38,0.2)',
            //     tension: .4,
            //     data: [28, 48, 40]
            // }
        ]
    })


    // const ssss = collection(subcollection, "timeline");
    // console.table(subcollection.data);


    // console.log(excerciseData.collection());
    // excerciseData.docs.forEach(doc => {
    // console.log(doc)
    // });

    // await getDocs(query(_collection, where(documentId(), "==", store.state.user?.uid))).then(snapshot => {
    //     snapshot.forEach(doc => {
    //         console.log(`${doc.id}: ${doc.data().uid}`);
    //     })
    // })
    // const snapshot = await getDocs(query(_collection, where(documentId(), "==", store.state.user?.uid)));
    // snapshot.forEach(doc => {
    //     console.log(`${doc.id}: ${doc.data().uid}`);
    // });

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
            code: "e01",
            title: "push_up",
            count: 16,
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
