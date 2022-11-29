<template>
    <title>"Welcome | Personal Trainer"</title>
    <div class="indexPage">
        <div class="index-inner">
            <div class="login-form">
                <div class="login-des">
                    <h1>Welcome to Personal-Trainer-Beta</h1>
                    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Incidunt illo ab nobis quis facere
                        nostrum
                        quos mollitia earum aut temporibus fugiat ullam necessitatibus magni, cumque unde illum laborum
                        rem?
                        Corporis!</p>
                    <img src="@/assets/logo/index_logo.gif" />
                </div>
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