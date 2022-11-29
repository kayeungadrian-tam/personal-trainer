<template>
    <nav>
        <router-link to="/home">
            <img class="site-logo"
                v-if="!hideMenu"
                src="https://w7.pngwing.com/pngs/82/587/png-transparent-man-with-muscle-illustration-muscular-system-skeletal-muscle-human-body-human-skeleton-human-body-miscellaneous-physical-fitness-biology.png"
                width=100
                height=50 />
        </router-link>
        <div v-if="hideMenu"
            class="toggle-bar">
            <p-Button @click="_toggle"><i class="pi pi-align-justify"></i></p-Button>
            <p-Button @click="logout"><i class="pi pi-power-off"></i></p-Button>
        </div>
        <Menu ref="menu"
            :model="items"
            :popup="hideMenu" />

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
    menu.value?.toggle(event);
};



const items = ref(
    [
        {
            label: 'Update',
            icon: 'pi pi-refresh',
        },
        {
            label: 'Delete',
            icon: 'pi pi-times',

        },
        {
            label: 'Vue Website',
            icon: 'pi pi-external-link',
            to: "/webcam"
            // url: 'https://vuejs.org/'
        },
        {
            label: 'Router',
            icon: 'pi pi-upload',
            to: '/home'
        },
        {
            label: 'Options',
            items: [{ label: 'New', icon: 'pi pi-fw pi-plus', command: () => { console.log("TESTES") } },
            { label: 'Delete', icon: 'pi pi-fw pi-trash', url: 'https://www.primetek.com.tr' }]
        },
        {
            label: 'Account',
            items: [{ label: 'Options', icon: 'pi pi-fw pi-cog', to: '/options' },
            { label: 'Sign Out', icon: 'pi pi-fw pi-power-off', to: '/logout' }]
        }
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