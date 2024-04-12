<template>
  <transition name="fade">
    <div id="naverh" v-show="scY > 300" @click="toTop">
      <p class="q-mb-none">Наверх</p>
    </div>
  </transition>
  <div class="footer">
    <div class="container">
      <h4 id="footer_text">© «Ростовский государственный экономический университет (РИНХ)»
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