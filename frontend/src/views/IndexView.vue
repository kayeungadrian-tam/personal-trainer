<template>
    <title>"Welcome | Personal Trainer"</title>
    <div class="index-page">

        <div class="index-inner">
            <div class="welcom-side">
                <div class="main-slogan">
                    <h1>Personal Trainer</h1>
                    <p>If you are working on something that you really care about, you don’t have to be pushed. The
                        vision pulls you.</p>
                </div>
            </div>
            <div class="login-side">
                <div class="login-card">
                    <LoginCard />
                </div>
            </div>
        </div>
    </div>
</template>

<style>
@import "@/assets/css/index.css";
</style>



<script lang="ts">
document.title = 'Welcom | Personal Trainer Beta';

import { onMounted, defineComponent } from 'vue';
import LoginCard from '@/components/LoginCard.vue';

export default defineComponent({
    name: 'indexView',
    components: {
        // HelloWorld,
        LoginCard
    },
});
</script>