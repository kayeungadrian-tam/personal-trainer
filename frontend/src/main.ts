import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { firebaseApp } from './firebase'
import { VueFire, VueFireAuth } from 'vuefire'

// createApp(App).use(router).mount('#app')

const app = createApp(App)
app
    .use(VueFire, {
        // imported above but could also just be created here
        firebaseApp,
        modules: [
            // we will see other modules later on
            VueFireAuth(),
        ],
    })
    .use(router)

app.mount('#app')