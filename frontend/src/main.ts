import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/index'
import PrimeVue from 'primevue/config';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';

const app = createApp(App)
app
    .use(router)
    .use(store)
    .use(PrimeVue)

app.component('p-Button', Button);

app.mount('#app')