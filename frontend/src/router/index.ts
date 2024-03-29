import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue';
import IndexView from '../views/IndexView.vue';
import ProfileView from '../views/ProfileView.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'index',
    component: IndexView
  },
  {
    path: '/logout',
    name: 'logout',
    component: IndexView
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/webcam',
    name: 'webcam',
    component: () => import(/* webpackChunkName: "about" */ '../views/WebCamView.vue')
  },
  {
    path: '/memo',
    name: 'memo',
    component: () => import(/* webpackChunkName: "about" */ '../views/MemoView.vue')
  },
  {
    path: '/exercise',
    name: 'exercise',
    component: () => import(/* webpackChunkName: "about" */ '../views/ExerciseView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
