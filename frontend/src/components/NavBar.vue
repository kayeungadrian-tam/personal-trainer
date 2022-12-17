<template>
    <div class="toggle-menu">
        <i class="pi pi-align-justify"
            @click="visibleleft = true"
            style="font-size: 1.5rem; font-weight: 900;"></i>
    </div>
    <nav>
        <router-link to="/home">
            <span class="site-title">Personal Trainer</span>
            <!-- <img class="site-logo" -->
            <!-- v-if="!hideMenu" -->
            <!-- src="https://w7.pngwing.com/pngs/82/587/png-transparent-man-with-muscle-illustration-muscular-system-skeletal-muscle-human-body-human-skeleton-human-body-miscellaneous-physical-fitness-biology.png" -->
            <!-- width=100 -->
            <!-- height=50 /> -->
        </router-link>

        <Menu v-if="!hideMenu"
            ref="menu"
            :model="items"
            :popup="false" />

        <p-Button @click="test_emit">sa</p-Button>
        <p-Button @click="logout"
            class="p-button-lg p-button-danger p-button-rounded ">
            <i class="pi pi-fw pi-power-off log-out-button"></i>

            Log out
        </p-Button>
    </nav>



    <Sidebar v-model:visible="visibleleft">
        Content
    </Sidebar>

</template>

  
<script setup lang="ts">
import Sidebar from 'primevue/sidebar';
import Menu from 'primevue/menu';
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

import { defineEmits } from 'vue';
const emit = defineEmits(['inFocus', 'submit'])

const test_emit = () => {
    emit("submit", 1)
}

const router = useRouter()
const store = useStore();
const hideMenu = ref(false)

const visibleleft = ref(false)


const logout = async () => {
    try {
        await store.dispatch('logout', {
            // password: password.value
        })
        router.push("/")
    }
    catch (err) {
        // error.value = err.message
        console.error(err)
    }
}



const menu = ref();

const _toggle = (event: any) => {
    console.log("saegini")
    hideMenu.value = !hideMenu.value
    menu.value?.toggle(event);
};



const items = ref(
    [
        {
            label: 'Home',
            icon: 'pi pi-home',
            to: "/home"
        },
        {
            label: 'About',
            icon: 'pi pi-info',
            to: "/about"

        },
        {
            label: 'Mediapipe',
            icon: 'pi pi-camera',
            to: "/webcam"
            // url: 'https://vuejs.org/'
        },
        {
            label: 'Roadmap',
            icon: 'pi pi-map',
            // to: '/home',
            url: "https://adrian-tam.notion.site/Personal-Trainer-fa1afe46158548da8a8239762d3d7669",
            target: "blank"
        },

        // {
        //     label: 'Options',
        //     items: [{ label: 'New', icon: 'pi pi-fw pi-plus', command: () => { console.log("TESTES") } },
        //     { label: 'Delete', icon: 'pi pi-fw pi-trash', url: 'https://www.primetek.com.tr' }]
        // },
        // {
        //     label: 'Account',
        //     items: [{ label: 'Options', icon: 'pi pi-fw pi-cog', to: '/options' },
        //     { label: 'Sign Out', icon: 'pi pi-fw pi-power-off', to: '/logout' }]
        // }
    ]
)

onMounted(() => { window.addEventListener("resize", myEventHandler) })

const myEventHandler = (e: any) => {
    if (window.innerWidth < 800) {
        hideMenu.value = true;
    } else {
        hideMenu.value = false;
    }
}
</script>
  
  
  
<script lang="ts">
import { defineComponent, ref, onMounted, onUnmounted } from 'vue';
import { async } from '@firebase/util';
</script>
  


<style>
@import "@/assets/css/nav.css";
</style>