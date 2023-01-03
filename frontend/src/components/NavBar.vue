<template>
    <div class="toggle-menu">
        <i class="pi pi-align-justify"
            @click="visibleleft = true"
            style="font-size: 1.5rem; font-weight: 900; color:whitesmoke"></i>
    </div>
    <nav>
        <router-link to="/home">
            <span class="site-title">Personal Trainer</span>
        </router-link>
        <div class="profile"
            @click="router.push('/profile')">
            <Avatar :image="store.state.user?.photoURL || ''"
                shape="circle"
                size="xlarge" />

            <Knob v-model="value"
                :min="0"
                :max="100"
                valueColor="#5b7985" />
            <div class="trophies">
                <img src="https://cdn-icons-png.flaticon.com/128/9032/9032376.png"
                    width=40
                    height=40 />
                <img class="trophy-icon"
                    src="https://cdn-icons-png.flaticon.com/128/8888/8888935.png"
                    width=40
                    height=40 />
                <img class="trophy-icon"
                    src="https://cdn-icons-png.flaticon.com/128/7933/7933103.png"
                    width=40
                    height=40 />

            </div>
        </div>
        <Menu v-if="!hideMenu"
            ref="menu"
            :model="items"
            :popup="false" />

        <p-Button @click="logout"
            class="p-button-lg p-button-danger p-button-rounded ">
            <i class="pi pi-fw pi-power-off log-out-button"></i>
            Log out
        </p-Button>
    </nav>



    <Sidebar v-model:visible="visibleleft">
        <div class="sidebar">
            <div class="sidebar-profile">
                <Avatar :image="store.state.user?.photoURL || ''"
                    shape="circle"
                    size="xlarge" />
                <div class="display-name">

                    <h3>{{ store.state.user?.displayName }}</h3>
                    <p>Memeber</p>
                </div>
            </div>
            <div class="profile"
                @click="router.push('/profile')">
                <Knob v-model="value"
                    :min="0"
                    :max="100"
                    valueColor="#5b7985" />
                <div class="trophies">
                    <img src="https://cdn-icons-png.flaticon.com/128/9032/9032376.png"
                        width=40
                        height=40 />
                    <img class="trophy-icon"
                        src="https://cdn-icons-png.flaticon.com/128/8888/8888935.png"
                        width=40
                        height=40 />
                    <img class="trophy-icon"
                        src="https://cdn-icons-png.flaticon.com/128/7933/7933103.png"
                        width=40
                        height=40 />
                </div>
            </div>

            <div class="sidebar-items">
                <div class="sidebar-items-container"
                    v-for="(item, index) in items"
                    :key="index">
                    <span style="width:100%;"
                        @click="sidebarButton(item.to || '/')">
                        <i :class="item.icon" />
                        <span class="sidebar-item-label">
                            {{ item.label }}
                        </span>
                    </span>
                </div>
            </div>


            <div class="sidebar-logout-button">
                <p-Button @click="logout"
                    class="p-button-lg p-button-danger p-button-rounded ">
                    <i class="pi pi-fw pi-power-off log-out-button"></i>
                    Log out
                </p-Button>
            </div>
        </div>
    </Sidebar>

</template>

  
<script setup lang="ts">
import Avatar from 'primevue/avatar';
import Menu from 'primevue/menu';
import Sidebar from 'primevue/sidebar';
import Knob from 'primevue/knob';
import Breadcrumb from 'primevue/breadcrumb';


import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

import { defineEmits } from 'vue'

import stopCamera from "@/composables/camera_utils"

const emit = defineEmits(['inFocus', 'submit'])


const value = ref(20);

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

const sidebarButton = (path: string) => {
    console.log(path);
    router.push(path)
}

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
            label: "Memo",
            icon: 'pi-file-edit',
            to: "/memo"
        }

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