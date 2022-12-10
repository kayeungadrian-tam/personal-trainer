<template>
  <NavBar />
  <div class="home">
    <div class="title">
      <h1>
        Welcome back <span class="user-name">{{ store.state.user.displayName }}</span>
      </h1>
    </div>

    <!-- All EXs -->
    <div class="main">
      <h2>All Excercises</h2>
      <div class="excercise-board">
        <ExcerciseCard msg="Push Up"
          :progress=25 />

        <ExcerciseCard msg="Jump Squat"
          :progress=25 />


      </div>
    </div>
    <TestFirebaseVue />
  </div>


</template>



<style>
@import "@/assets/css/home.css";
</style>


<script setup lang="ts">

import Sidebar from 'primevue/sidebar';
import { useStore } from 'vuex'
import ExcerciseCard from '@/components/ExcerciseCard.vue'
import NavBar from "@/components/NavBar.vue";

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
