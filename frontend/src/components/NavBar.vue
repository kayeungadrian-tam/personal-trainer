<template>
    <nav>
        <router-link to="/home">
            <img class="site-logo"
                v-if="!hideMenu"
                src="https://w7.pngwing.com/pngs/82/587/png-transparent-man-with-muscle-illustration-muscular-system-skeletal-muscle-human-body-human-skeleton-human-body-miscellaneous-physical-fitness-biology.png"
                width=100
                height=50 />
        </router-link>
        <div v-if="true"
            class="toggle-bar">
            <div @click="_toggle"><i class="pi pi-align-justify"></i></div>
            <!-- <p-Button @click="logout"><i class="pi pi-power-off"></i></p-Button> -->
        </div>
        <Menu v-if="!hideMenu"
            ref="menu"
            :model="items"
            :popup="false" />

    </nav>

</template>
<scripts setup lang="ts">

</scripts>
  
<script setup lang="ts">

import Menu from 'primevue/menu';
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'



const router = useRouter()
const store = useStore();
const hideMenu = ref(false)

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
        {
            label: 'Sign Out',
            icon: 'pi pi-fw pi-power-off',
            // to: '/logout',
            command: () => { logout(); }
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