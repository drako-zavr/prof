<template>
    <q-layout view="lHh Lpr lFf">
        <AppHeader/>
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
