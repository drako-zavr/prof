<template>
    <div class="centr">
        <div class="container">
            <div class="col-lg-3">
                <SideBar />
            </div>
            <div class="col-lg-9">
                <div id="content">

                    <h3 v-for="report in reportList"
                            :key="report.id"><a :href="report.fileContent"
                            target="_blank">{{report.title}}</a> <a v-if="report.presentationContent" :href="report.presentationContent"
                            target="_blank">(Смотреть презентацию)</a></h3>

                    <br><br>
                    <p align="center">&nbsp;</p>
                    <p align="center"><strong>&nbsp;</strong></p>
                    <p align="center">&nbsp;</p>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup lang="ts">
import SideBar from 'src/layouts/SideBar.vue';
import { useReport } from 'src/composables/useReports';
import { onMounted, ref } from 'vue';
import { Report } from 'src/models/report';

const { fetchReport } = useReport();
const reportList = ref<Report[]>([]);
const isLoading = ref<boolean>(true);

onMounted(async () => {
    reportList.value = await fetchReport();
    isLoading.value = false;
    console.log(reportList.value)
});
</script>