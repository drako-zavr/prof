<template>
    <div class="row alert alert-warning">
        <div class="col-lg-4 col-md-6 col-sm-7">
            <img v-if="article?.photo" :src="article?.photo" style="border:1px solid #FFF; width:200px;">
        </div>
        <div class="col-lg-8 col-md-4 col-sm-4 alpha">
            <div>
                <p v-html="article?.title"></p>
                <br><br>
                <q-expansion-item v-model="expanded" label="Подробнее">
                    <q-card class="alert-warning">
                        <q-card-section>
                            <div>
                                <p v-html="article?.content"></p>
                                <div v-for="articledocument in article?.documents" :key="articledocument.id">
                                <p><a :href="articledocument.fileContent" target="_blank">{{articledocument.title}}</a></p>
                                </div>
                            </div>
                            <div class="row justify-center items-center">
                                <div v-for="articlephoto in article?.images" :key="articlephoto.id">
                                    <img @click="carousel = true; slide = articlephoto.order" v-if="articlephoto?.photo"
                                        :src="articlephoto?.photo" style="border:1px solid #FFF; width:150px;"
                                        class="col-4">
                                </div>
                            </div>
                            <q-dialog v-model="carousel">
                                <q-carousel transition-prev="slide-right" transition-next="slide-left" swipeable
                                    animated v-model="slide" control-color="black"
                                    navigation-icon="radio_button_unchecked" navigation arrows
                                    class="bg-white shadow-1 rounded-borders gallery" >
                                    <q-carousel-slide v-for="articlephoto in article?.images" :key="articlephoto.id"
                                        :name="articlephoto.order" class="column no-wrap flex-center">
                                        <img v-if="articlephoto?.photo" :src="articlephoto?.photo"
                                            class="gallery__image">
                                    </q-carousel-slide>
                                </q-carousel>
                            </q-dialog>
                        </q-card-section>
                    </q-card>
                </q-expansion-item>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { Article } from 'src/models/article';
import { PropType, ref } from 'vue';

defineProps({
    article: Object as PropType<Article>
});

const expanded = ref<boolean>(false)
const slide = ref<number>(0)
const carousel = ref<boolean>(false)

</script>