<template>

  <body>

    <ParticlesVue v-if="store.state.user" />
    <router-view />
  </body>
</template>

<script setup lang="ts">
// import NavBar from "@/components/NavBar.vue";
import { useStore } from 'vuex'
import { onMounted } from "vue";

import ParticlesVue from "@/components/ParticlesVue.vue";

const store = useStore()


onMounted(async () => {
  store.state.user = null;
})



</script>

<style>
@import "primevue/resources/themes/saga-blue/theme.css";
@import "primevue/resources/primevue.min.css";
@import "primeicons/primeicons.css";

@import "@/assets/css/base.css";
</style>
