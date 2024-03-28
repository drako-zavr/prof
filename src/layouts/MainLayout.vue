<template>
    <q-layout view="lHh Lpr lFf">
        <!-- <q-header elevated>
            <q-toolbar>
                <q-toolbar-title> RSUE </q-toolbar-title>
            </q-toolbar>
        </q-header> -->
        <AppHeader/>
        <!-- <SideBar/> -->

        <q-page-container>
            <router-view />
        </q-page-container>
        <AppFooter/>
    </q-layout>
</template>

<script setup lang="ts">
import AppHeader from './AppHeader.vue';
import AppFooter from './AppFooter.vue';
</script>
