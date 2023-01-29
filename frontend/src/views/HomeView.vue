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
        <Chart type="line"
          style="height: 100%;"
          :data="basicData"
          :options="basicOptions" />
        <!-- </div> -->
      </div>


      <div style="margin-top: 50px;">

        <!-- <TestFirebaseVue /> -->
        <h2>Leaderboard</h2>
        <TableVue :data="data"
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



const lastWeekLabels = ref();
const basicData = ref();

const columns = ref([
  { field: 'id', header: 'Code' },
  { field: 'name', header: 'Name' },
  { field: 'category', header: 'Category' },
  { field: 'quantity', header: 'Quantity' }
]);

const data = ref({
  "data": [
    { "id": "1000", "code": "f230fh0g3", "name": "Bamboo Watch", "description": "Product Description", "image": "bamboo-watch.jpg", "price": 65, "category": "Accessories", "quantity": 24, "inventoryStatus": "INSTOCK", "rating": 5 },
    { "id": "1001", "code": "nvklal433", "name": "Black Watch", "description": "Product Description", "image": "black-watch.jpg", "price": 72, "category": "Accessories", "quantity": 61, "inventoryStatus": "INSTOCK", "rating": 4 },
    { "id": "1002", "code": "zz21cz3c1", "name": "Blue Band", "description": "Product Description", "image": "blue-band.jpg", "price": 79, "category": "Fitness", "quantity": 2, "inventoryStatus": "LOWSTOCK", "rating": 3 },
    { "id": "1003", "code": "244wgerg2", "name": "Blue T-Shirt", "description": "Product Description", "image": "blue-t-shirt.jpg", "price": 29, "category": "Clothing", "quantity": 25, "inventoryStatus": "INSTOCK", "rating": 5 },
    { "id": "1004", "code": "h456wer53", "name": "Bracelet", "description": "Product Description", "image": "bracelet.jpg", "price": 15, "category": "Accessories", "quantity": 73, "inventoryStatus": "INSTOCK", "rating": 4 },
    { "id": "1005", "code": "av2231fwg", "name": "Brown Purse", "description": "Product Description", "image": "brown-purse.jpg", "price": 120, "category": "Accessories", "quantity": 0, "inventoryStatus": "OUTOFSTOCK", "rating": 4 },
    { "id": "1006", "code": "bib36pfvm", "name": "Chakra Bracelet", "description": "Product Description", "image": "chakra-bracelet.jpg", "price": 32, "category": "Accessories", "quantity": 5, "inventoryStatus": "LOWSTOCK", "rating": 3 },
    { "id": "1007", "code": "mbvjkgip5", "name": "Galaxy Earrings", "description": "Product Description", "image": "galaxy-earrings.jpg", "price": 34, "category": "Accessories", "quantity": 23, "inventoryStatus": "INSTOCK", "rating": 5 },
    { "id": "1008", "code": "vbb124btr", "name": "Game Controller", "description": "Product Description", "image": "game-controller.jpg", "price": 99, "category": "Electronics", "quantity": 2, "inventoryStatus": "LOWSTOCK", "rating": 4 },
    { "id": "1009", "code": "cm230f032", "name": "Gaming Set", "description": "Product Description", "image": "gaming-set.jpg", "price": 299, "category": "Electronics", "quantity": 63, "inventoryStatus": "INSTOCK", "rating": 3 }
  ]
})

const testGifs = ref([
  { fileName: "legs-and-abs-work-out-fitness" },
  { fileName: "../assets/excercise/legs-and-abs-work-out-fitness.gif" },
  { fileName: "../assets/excercise/legs-and-abs-work-out-fitness.gif" },
  { fileName: "../assets/excercise/legs-and-abs-work-out-fitness.gif" },
  { fileName: "../assets/excercise/legs-and-abs-work-out-fitness.gif" },
])

const cars = ref([
  { name: "adrian" },
  { name: "peter" },
  { name: "mark" },
  { name: "john" },
  { name: "sam" }
])

onMounted(async () => {
  lastWeekLabels.value = await getLastWeeksDate();
  // lastWeekLabels.value = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];

  basicData.value = ({
    // labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    labels: lastWeekLabels.value,

    datasets: [
      {
        label: 'My First dataset',
        borderColor: '#42A5F5',
        backgroundColor: '#42A5F515',
        fill: true,
        tension: .4,
        data: [65, 59, 80, 81, 56, 55, 40]
      },
      {
        label: 'My Second dataset',
        fill: true,
        borderColor: '#FFA726',
        backgroundColor: 'rgba(255,167,38,0.2)',
        tension: .4,
        data: [28, 48, 40, 19, 86, 27, 90]
      }
    ]
  })


})



const test = () => {
  const _time = getLastWeeksDate();
  console.log("time", _time)
}

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

// import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src


export default defineComponent({
  name: 'HomeView',
  components: {
    // HelloWorld,
    // TestFirebaseVue
  },
});
</script>
