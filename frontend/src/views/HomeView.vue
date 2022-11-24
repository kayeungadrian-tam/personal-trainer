<template>
  <div class="home">

    <!-- <HelloWorld msg="Welcome to Your Vue.js + TypeScript App"/> -->

    <TestFirebaseVue />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import TestFirebaseVue from '@/components/TestFirebase.vue';

// import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src

export default defineComponent({
  name: 'HomeView',
  components: {
    // HelloWorld,
    TestFirebaseVue
  },
});
</script>
