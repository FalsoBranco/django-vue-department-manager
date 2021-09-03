import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/Home.vue';
import Employee from '@/views/Employee.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/employee',
    name: 'Employee',
    component: Employee,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
