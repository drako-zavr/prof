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
          <h3 align="center">АРХИВ</h3>
          <br>

          <div id="myTabContent" class="tab-content">
            <div v-for="article in paginatedArray.slice()" :key="article.id">
              <AppArticle :article="article" />
            </div>
          </div>
          <center>
            <ul id="myTab" class="pagination">
              <li v-bind:class="{ 'disabled': pageNumber == 0, '': pageNumber > 0 }" @click="prevPage"><a
                  data-toggle="tab">&laquo;</a></li>
              <template v-for="a in arrayLength" :key="a">
                <li v-bind:class="{ 'active': pageNumber == a - 1, '': pageNumber != a - 1 }"><a class="col"
                    @click="selectPage(a - 1)" data-toggle="tab">{{ a }}</a></li>
              </template>
              <li v-bind:class="{ 'disabled': pageNumber >= arrayLength - 1, '': pageNumber < arrayLength - 1 }" @click="nextPage"><a
                  data-toggle="tab">&raquo;</a></li>
            </ul>
          </center>
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

// пагинация
const paginatedArray = ref<Article[]>([]);
var pageNumber = ref<number>(0)
const size = ref<number>(15)
let arrayLength = ref<number>(0);

onMounted(async () => {
  articlesList.value = await fetchArticles();
  isLoading.value = false
  sortedArray.value = articlesList.value.sort((a, b) =>b.id- a.id )
  arrayLength.value =  Math.ceil(sortedArray.value.length / size.value)

  paginatedData()
});

function paginatedData() {
  const start = pageNumber.value * size.value,
    end = start + size.value;
  paginatedArray.value = sortedArray.value
    .slice(start, end)
}

function nextPage() {
  if (pageNumber.value != arrayLength.value - 1) {
    pageNumber.value++;
  }
  paginatedData()
}
function prevPage() {
  if (pageNumber.value != 0) {
    pageNumber.value--;
  }
  paginatedData()
}
function selectPage(page: number) {
  pageNumber.value = page;
  paginatedData()
}
</script>