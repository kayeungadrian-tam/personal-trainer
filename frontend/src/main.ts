import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/index'
import PrimeVue from 'primevue/config';
import Dialog from 'primevue/dialog';

const app = createApp(App)
app
    .use(router)
    .use(store)
    .use(PrimeVue)

// app.component('Dialog', Dialog);

app.mount('#app')