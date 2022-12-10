<template>
    <Nav />
    <div class="home">
        <div class="title">
            <h1>About</h1>
        </div>
        <h1>This is an about page</h1>
        <CameraVue />
    </div>
</template>
  
  
<script setup lang="ts">
import CameraVue from '@/components/Camera.vue';
import Nav from '@/components/NavBar.vue';

</script>