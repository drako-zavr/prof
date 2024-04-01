<template>
    <div class="centr">
        <div class="container">
            <div class="col-lg-3">
                <SideBar />
            </div>
            <div class="col-lg-9">
                <div id="content">
                    <h3 align="center">МЫ ПОМНИМ ВСЕХ ВАС ПОИМЕННО</h3>
                    <br><br>
                    <div class="row">
                        <div class="col-lg-6 col-md-6 col-sm-6" v-for="memory in memoryList"
                            :key="memory.id">
                            <div align="center"><img v-if="memory?.photo" :src="memory?.photo"
                                    style="border:1px solid #FFF"></div>
                            <p align="center"><strong>{{ memory.lastname }} {{ memory.firstname }} {{ memory.midname }}
                                </strong><br></p>
                            <p align="center" v-html="memory?.description"></p>
                            <p align="center">  
                                <a v-if="memory.fileContent != null" :href="memory.fileContent">Подробнее >>></a>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup lang="ts">
import SideBar from 'src/layouts/SideBar.vue';
import { useMemory } from 'src/composables/useMemory';
import { onMounted, ref } from 'vue';
import { Memory } from 'src/models/memory';

const { fetchMemory } = useMemory();
const memoryList = ref<Memory[]>([]);
const isLoading = ref<boolean>(true);

onMounted(async () => {
    memoryList.value = await fetchMemory();
    isLoading.value = false;
    console.log(memoryList.value)
});
</script>