<template>
  <transition name="fade">
    <div id="naverh" v-show="scY > 300" @click="toTop">
      <p class="q-mb-none">Наверх</p>
    </div>
  </transition>
  <div class="footer">
    <div class="container">
      <h4 id="footer_text">© «Ростовский государственный экономический университет (РИНХ)»
        <a href="//www.liveinternet.ru/click" target="_blank"><img
            src="//counter.yadro.ru/hit?t44.6;r;s2880*1800*30;uhttp%3A//localhost%3A8080/otdih;0.3869637443048287"
            alt="" title="LiveInternet" border="0" width="31" height="31"></a>
      </h4>
    </div>
  </div>

</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';

var scTimer = ref<number>(0)
var scY = ref<number>(0)
onMounted(async () => {
  window.addEventListener('scroll', handleScroll);
})
/* Плавная прокрутка наверх */
function handleScroll() {
  if (scTimer.value) return
  scTimer.value = window.setTimeout(() => {
    scY.value = window.scrollY
    clearTimeout(scTimer.value)
    scTimer.value = 0
  }, 100)
}
function toTop() {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}
</script>