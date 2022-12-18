<template>
    <title>"Welcome | Personal Trainer"</title>
    <div class="indexPage">

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
            <!-- <div class="login-form">
                <div class="login-des">
                    <h1>Welcome to Personal-Trainer-Beta</h1>
                    <p>Lorem ipsum dolor sist, amet consectetur adipisicing elit. Incidunt illo ab nobis quis facere
                        nostrum
                        quos mollitia earum aut temporibus fugiat ullam necessitatibus magni, cumque unde illum laborum
                        rem?
                        Corporis!</p>
                    <img src="@/assets/logo/index_logo.gif" />
                </div>
                <div class="login-card">
        </div>
    </div> -->


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