<template>
  <ul class="nav nav-pills nav-stacked" id="menu">
    <li ><a @click=" $router.push({ name: 'IndexPage' })">ГЛАВНАЯ</a></li> 
    <li><a @click=" $router.push({ name: 'ProfactPage' })">ПРОФАКТИВ</a></li>
    <li><a @click=" $router.push({ name: 'HistoryPage' })">ИСТОРИЯ</a></li>
    <li><a @click=" $router.push({ name: 'NormDoc' })">НОРМАТИВНЫЕ ДОКУМЕНТЫ</a></li>
    <li><a @click=" $router.push({ name: 'Ohrana' })">ОХРАНА ТРУДА</a></li>
    <li><a @click=" $router.push({ name: 'Otdih' })">ОТДЫХ И ЗДОРОВЬЕ</a></li>
    <li><a @click=" $router.push({ name: 'Dogovor' })">КОЛЛЕКТИВНЫЙ ДОГОВОР</a></li>
    <li><a @click=" $router.push({ name: 'Culture' })">КУЛЬТУРНО-ПРОСВЕТИТЕЛЬСКАЯ ДЕЯТЕЛЬНОСТЬ</a></li>
    <li><a @click=" $router.push({ name: 'Memory' })">МЫ ПОМНИМ ВСЕХ ВАС ПОИМЕННО</a></li>
    <li><a @click=" $router.push({ name: 'Smi' })">ИЗДАНИЯ СМИ</a></li>
    <li><a @click=" $router.push({ name: 'MatPom' })">МАТЕРИАЛЬНАЯ ПОМОЩЬ</a></li>
    <li><a @click=" $router.push({ name: 'Report' })">ПУБЛИЧНЫЙ ОТЧЕТ</a></li>
    <li><a @click=" $router.push({ name: 'Help' })">ЭКСПЕРТНО-ПРАВОВАЯ ПОМОЩЬ</a></li>
    <li><a @click=" $router.push({ name: 'Contact' })">КОНТАКТЫ</a></li>
  </ul>
  <br><br>
  <AppMail />
</template>
<script setup lang="ts">
import AppMail from 'src/components/AppMail.vue';
</script>
