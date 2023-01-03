<template>
    <div class="profile-progess-card">
        <div class="tmp">
            <ProgressBar mode="determinate"
                :showValue="false"
                :value="20" />
        </div>
        <div class="tmp2">
            <ProgressBar mode="determinate"
                :showValue="false"
                :value="20" />
            <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Expedita error voluptas, eos dicta id
                consectetur alias veritatis. Dicta officiis veritatis rem, necessitatibus, accusamus eaque quis
                tempore omnis tenetur, natus debitis.</p>
        </div>
    </div>
</template>

<style>
@import "@/assets/css/progressbar.css";
</style>

<script setup lang="ts">
import ProgressBar from 'primevue/progressbar';
</script>