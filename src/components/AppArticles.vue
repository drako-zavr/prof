<template>
  <div class="centr">
    <div class="container">
      <div class="col-lg-3">
        <SideBar />
      </div>
      <div class="col-lg-9">
        <div id="content">

          <div class="col-lg-4 alert alert-success text-center">
            <h3><a href="src/assets/doc/zayavlenie.docx">Заявление в профсоюз РГЭУ (РИНХ)</a></h3>
          </div>
          <div class="col-lg-4">&nbsp;</div>
          <div class="col-lg-4 alert alert-success text-center"><a href="mailto:gordeev.se@mail.ru">ПОЧТОВЫЙ ЯЩИК ДЛЯ
              ОБРАЩЕНИЙ И ПРЕДЛОЖЕНИЙ<br><br>
              <img src="../assets/images/mail.png"></a></div>

          <br>
          <h3 align="center">НОВОСТИ</h3>
          <br>

          <div id="myTabContent" class="tab-content">
            <div class="tab-pane fade in active" id="2016">
              <div v-for="article in sortedArray.slice(-5).reverse()" :key="article.id">
                <AppArticle :article="article" />
              </div>
            </div>
          </div>
          <button type="button" class="btn btn-default" @click="$router.push({ name: 'Archive' })">Архив <q-icon name="east" /></button>
        </div>
      </div>
    </div>
  </div>

</template>
<script setup lang="ts">
import SideBar from 'src/layouts/SideBar.vue';
import AppArticle from 'src/components/AppArticle.vue';
import { useArticles } from 'src/composables/useArticles';
import { Article } from 'src/models/article';
import { onMounted, ref } from 'vue';

const { fetchArticles } = useArticles();
const articlesList = ref<Article[]>([]);
const sortedArray = ref<Article[]>([]);
const isLoading = ref<boolean>(true);

onMounted(async () => {
  articlesList.value = await fetchArticles();
  isLoading.value = false;
  sortedArray.value = articlesList.value.sort((a, b) => a.id - b.id);
});

</script>