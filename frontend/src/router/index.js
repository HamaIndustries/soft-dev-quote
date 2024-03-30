import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/fuel',
      name: 'fuel',
      component: () => import('../views/FuelQuote.vue')
    },

    {
      path: '/login',
      name: 'login',
      component: () => import('../views/Login.vue')
    },

    {
      path: '/register',
      name: 'register',
      component: () => import('../views/register.vue')
    },

    {
      path: '/profileManage',
      name: 'profilemanage',
      component: () => import('../views/profileManage.vue')
    },

    // {
    //   path: '/profile',
    //   name: 'profile',
    //   component: () => import('../views/profileView.vue')
    // },

    {
      path: '/quotehistory',
      name: 'quotehistory',
      component: () => import('../views/QuoteHistory.vue')
    }
  ]
})

export default router
