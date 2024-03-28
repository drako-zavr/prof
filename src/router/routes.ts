import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
    {
        path: '/',
        component: () => import('layouts/MainLayout.vue'),
        children: [
          {
            path: '',
            name: 'IndexPage',
            component: () => import('pages/IndexPage.vue'),
          },
        ],
      },
      {
        path: '/profact',
        component: () => import('layouts/MainLayout.vue'),
        children: [
          {
            path: '',
            name: 'ProfactPage',
            component: () => import('components/AppProfact.vue'),
          },
        ],
      },
    {
        path: '/history',
        component: () => import('layouts/MainLayout.vue'),
        children: [
          {
            path: '',
            name: 'HistoryPage',
            component: () => import('components/AppHistory.vue'),
          },
        ],
      },
      {
        path: '/normdoc',
        component: () => import('layouts/MainLayout.vue'),
        children: [
          {
            path: '',
            name: 'NormDoc',
            component: () => import('components/AppNormDoc.vue'),
          },
        ],
      },
      {
        path: '/ohrana',
        component: () => import('layouts/MainLayout.vue'),
        children: [
          {
            path: '',
            name: 'Ohrana',
            component: () => import('components/AppOhrana.vue'),
          },
        ],
      },
      {
        path: '/dogovor',
        component: () => import('layouts/MainLayout.vue'),
        children: [
          {
            path: '',
            name: 'Dogovor',
            component: () => import('components/AppDogovor.vue'),
          },
        ],
      },
      {
        path: '/otdih',
        component: () => import('layouts/MainLayout.vue'),
        children: [
          {
            path: '',
            name: 'Otdih',
            component: () => import('components/AppOtdih.vue'),
          },
        ],
      },
      {
        path: '/culture',
        component: () => import('layouts/MainLayout.vue'),
        children: [
          {
            path: '',
            name: 'Culture',
            component: () => import('components/AppCulture.vue'),
          },
        ],
      },
      {
        path: '/memory',
        component: () => import('layouts/MainLayout.vue'),
        children: [
          {
            path: '',
            name: 'Memory',
            component: () => import('components/AppMemory.vue'),
          },
        ],
      },
      {
        path: '/smi',
        component: () => import('layouts/MainLayout.vue'),
        children: [
          {
            path: '',
            name: 'Smi',
            component: () => import('components/AppSmi.vue'),
          },
        ],
      },
      {
        path: '/mat-pom',
        component: () => import('layouts/MainLayout.vue'),
        children: [
          {
            path: '',
            name: 'MatPom',
            component: () => import('components/AppMatPom.vue'),
          },
        ],
      },
      {
        path: '/help',
        component: () => import('layouts/MainLayout.vue'),
        children: [
          {
            path: '',
            name: 'Help',
            component: () => import('components/AppHelp.vue'),
          },
        ],
      },
      {
        path: '/report',
        component: () => import('layouts/MainLayout.vue'),
        children: [
          {
            path: '',
            name: 'Report',
            component: () => import('components/AppReport.vue'),
          },
        ],
      },
      {
        path: '/contact',
        component: () => import('layouts/MainLayout.vue'),
        children: [
          {
            path: '',
            name: 'Contact',
            component: () => import('components/AppContact.vue'),
          },
        ],
      },
      {
        path: '/archive',
        component: () => import('layouts/MainLayout.vue'),
        children: [
          {
            path: '',
            name: 'Archive',
            component: () => import('components/AppArchive.vue'),
          },
        ],
      },
    // Always leave this as last one,
    // but you can also remove it
    {
        path: '/:catchAll(.*)*',
        component: () => import('pages/ErrorNotFound.vue'),
    },
];

export default routes;
