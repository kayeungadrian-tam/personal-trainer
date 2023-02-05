<template>
  <NavBar />
  <div class="dashboard">
    <div class="title">
      <h1>
        Welcome back <span class="user-name">{{ store.state.user?.displayName || "empty" }}</span>
      </h1>
    </div>


    <!-- All EXs -->
    <div class="main">

      <div class="excercise-board">
        <ExcerciseCard msg="Push Up"
          :progress=25 />

        <ExcerciseCard msg="Jump Squat"
          :progress=25 />



      </div>

      <!-- <div> -->

      <!-- </div> -->
      <div class="mission-today">

        <!-- <Carousel :value="testGifs"
          :numVisible="1"
          :numScroll="1">
          <template #header>
            <h2>Custom Header</h2>
          </template>
          <template #item="slotProps">
            <img :src=slotProps.data.gif>
          </template>
          <template #footer>
            <p>Custom Footer</p>
          </template>
        </Carousel> -->

      </div>


      <div class="week-chart-container">
        <h2>Performance</h2>
        <!-- <div class="week-chart"> -->
        <Chart type="bar"
          style="height: 100%;"
          :data="basicData"
          :options="basicOptions" />
        <!-- </div> -->
      </div>


      <div style="margin-top: 50px;">

        <!-- <TestFirebaseVue /> -->
        <h2>Leaderboard</h2>
        <TableVue :data="data2"
          :columns="columns" />

      </div>

    </div>
  </div>


</template>



<style>
@import "@/assets/css/home.css";
</style>


<script setup lang="ts">
import { onMounted } from 'vue';
import { useStore } from 'vuex'


import getLastWeeksDate from "@/composables/time_utils";

import ExcerciseCard from '@/components/ExcerciseCard.vue'
import NavBar from "@/components/NavBar.vue";
import TableVue from '@/components/TableVue.vue';

import Chart from 'primevue/chart';
import Skeleton from 'primevue/skeleton';
import Carousel from 'primevue/carousel';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';
import Row from 'primevue/row'

import { useCollection, useDocument } from 'vuefire'
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

const db = getFirestore();

const lastWeekLabels = ref();
const basicData = ref();

const columns = ref([
  { field: 'id', header: 'Code' },
  { field: 'name', header: 'Name' },
  { field: 'coumt', header: 'Category' },
]);


const data2 = ref({ "data": [{}] })

interface DataObject {
  timestamp: number;
  count: number;
}


const today = new Date();

function counterSum(ary: number[]) {
  // acc: number
  return ary.reduce((acc, val) => {
    return acc + val;
  }, 0);
}


const getRecord = async () => {

  const subcollection = await collection(
    db,
    "u_record"
  )

  // const snapshot = await getDocs(query(subcollection, where("uid", "==", "UN8KIvDJh7WCk8Z3XLF2W7cX8Tn1")));

  // snapshot.forEach((doc) => {
  //   console.log("", doc.data())
  // })

  const __docs = await getDocs(subcollection);

  console.log(__docs);
  __docs.forEach((doc) => {

    data2.value.data.push({ id: doc.id, name: doc.data().displayName, count: doc.data().total, rating: doc.data().total / 10 })


    console.log(doc.id)
    if (doc.id == store.state.user?.uid) {
      console.log(doc.data())
    }

  })
  data2.value.data = data2.value.data.splice(1);
  console.log(data2.value.data)
}

const updateRecord = async () => {
  console.log(today.getDay());



  // if (today.getDay() !== 1) { return }

  const oneWeekAgo = new Date();

  for (let i = 0; i < 7; i++) {
    oneWeekAgo.setDate(oneWeekAgo.getDate() - 1);
  }

  const tmp = await getCountByDate();
  const _values = Object.values(tmp)


  const sum = counterSum(_values as number[]);


  setDoc(doc(db, "u_record", store.state.user?.uid), {
    lastUpdated: today.getTime(),
    displayName: store.state.user.displayName,
    total: sum,
    uid:
      store.state.user?.uid
    ,
  })

}


const getCountByDate = async () => {

  const docRef = doc(db, "u_progess", store.state.user?.uid || "UN8KIvDJh7WCk8Z3XLF2W7cX8Tn1");
  const subcollection = await collection(
    docRef,
    "timeline"
  )


  const past_data: DataObject[] = [];

  const __docs = await getDocs(subcollection);
  __docs.forEach((doc) => {
    past_data.push({ timestamp: parseInt(doc.id), count: doc.data().count });
  })


  const groupedData = past_data.reduce((grouped, data) => {
    const date = new Date(data.timestamp);
    const monthDate = `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;


    if (!grouped[monthDate]) {
      grouped[monthDate] = [];
    }

    grouped[monthDate].push({ ...data });
    return grouped;

  }, {} as { [key: string]: DataObject[] })


  const sums = Object.keys(groupedData).reduce((sums, monthDate) => {
    sums[monthDate] = groupedData[monthDate].reduce((total, object) => total + object.count, 0);
    return sums;
  }, {} as any);

  return sums;
}

onMounted(async () => {
  updateRecord();
  lastWeekLabels.value = await getLastWeeksDate();

  const tmp = await getCountByDate();


  basicData.value = ({
    labels: Object.keys(tmp),

    datasets: [

      {
        label: 'Squat',
        fill: true,
        borderColor: '#FFA726',
        backgroundColor: 'rgba(255,167,38,0.5)',
        tension: .4,
        data: Object.values(tmp)
      }
    ]
  })

  getRecord();

})



const test = () => {
  const _time = getLastWeeksDate();
  console.log("time", _time)
}

const basicOptions = ref({
  plugins: {
    legend: {
      labels: {
        color: '#ebedef'
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


const visibleLeft = ref(false)

const store = useStore()



const items = ref(
  [
    {
      label: 'File',
      icon: 'pi pi-fw pi-file',
      to: 'home',
      items: [
        {
          label: 'New',
          icon: 'pi pi-fw pi-plus',
          items: [
            {
              label: 'Bookmark',
              icon: 'pi pi-fw pi-bookmark'
            },
            {
              label: 'Video',
              icon: 'pi pi-fw pi-video'
            }
          ]
        },
        {
          label: 'Delete',
          icon: 'pi pi-fw pi-trash'
        },
        {
          separator: true
        },
        {
          label: 'Export',
          icon: 'pi pi-fw pi-external-link'
        }
      ]
    },
    {
      label: 'Edit',
      to: 'about',

      icon: 'pi pi-fw pi-pencil',
      items: [
        {
          label: 'Left',
          icon: 'pi pi-fw pi-align-left'
        },
        {
          label: 'Right',
          icon: 'pi pi-fw pi-align-right'
        },
        {
          label: 'Center',
          icon: 'pi pi-fw pi-align-center'
        },
        {
          label: 'Justify',
          icon: 'pi pi-fw pi-align-justify'
        }
      ]
    },
    {
      label: 'Users',
      to: 'about',

      icon: 'pi pi-fw pi-user',
      items: [
        {
          label: 'New',
          icon: 'pi pi-fw pi-user-plus',

        },
        {
          label: 'Delete',
          icon: 'pi pi-fw pi-user-minus',

        },
        {
          label: 'Search',
          icon: 'pi pi-fw pi-users',
          items: [
            {
              label: 'Filter',
              icon: 'pi pi-fw pi-filter',
              items: [
                {
                  label: 'Print',
                  icon: 'pi pi-fw pi-print'
                }
              ]
            },
            {
              icon: 'pi pi-fw pi-bars',
              label: 'List'
            }
          ]
        }
      ]
    },
    {
      label: 'Events',
      to: 'about',

      icon: 'pi pi-fw pi-calendar',
      items: [
        {
          label: 'Edit',
          icon: 'pi pi-fw pi-pencil',
          items: [
            {
              label: 'Save',
              icon: 'pi pi-fw pi-calendar-plus'
            },
            {
              label: 'Delete',
              icon: 'pi pi-fw pi-calendar-minus'
            }
          ]
        },
        {
          label: 'Archieve',
          to: 'about',

          icon: 'pi pi-fw pi-calendar-times',
          items: [
            {
              label: 'Remove',
              icon: 'pi pi-fw pi-calendar-minus'
            }
          ]
        }
      ]
    },
    {
      label: 'Quit',
      icon: 'pi pi-fw pi-power-off'
    }
  ]
)


</script>



<script lang="ts">

import { defineComponent, ref } from 'vue';
import TestFirebaseVue from '@/components/TestFirebase.vue';
import { RgbColorManager } from 'tsparticles-engine';

// import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src


export default defineComponent({
  name: 'HomeView',
  components: {
    // HelloWorld,
    // TestFirebaseVue
  },
});
</script>
