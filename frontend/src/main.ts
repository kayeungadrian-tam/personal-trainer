import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/index'
import PrimeVue from 'primevue/config';
import Button from 'primevue/button';
import ToastService from 'primevue/toastservice';
import Particles from "vue3-particles";
import ConfirmationService from 'primevue/confirmationservice';
// import { tsParticles } from "https://cdn.jsdelivr.net/npm/tsparticles-engine/+esm";
// import { loadFull } from "https://cdn.jsdelivr.net/npm/tsparticles/+esm";


const app = createApp(App)
app
    .use(router)
    .use(store)
    .use(PrimeVue)
    .use(ToastService)
    .use(Particles)
    .use(ConfirmationService)
    ;

app
    .component('p-Button', Button)
    ;

app.mount('#app')