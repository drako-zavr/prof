<template>
    <div class="centr">
        <div class="container">
            <div class="col-lg-3">
                <SideBar />
            </div>
            <div class="col-lg-9">
                <div id="content">
                    <h3 align="center">ОТДЫХ И ЗДОРОВЬЕ</h3>
                    <br />
                    <div class="col-lg-6">&nbsp;</div>
                    <div class="col-lg-6 alert alert-success text-center"><a
                            href="src/assets/doc/otdih/zayavlenie.doc">Завление на
                            санаторно-оздоровительный отдых</a></div>
                    <br><br>
                    <ul>
                        <li><a href="src/assets/doc/otdih/polisOMS.pdf" target="_blank"><strong>КАК БЕСПЛАТНО ОФОРМИТЬ
                                    ИЛИ ВОССТАНОВИТЬ
                                    ПОЛИС ОМС</strong></a></li>
                        <li><strong><a href="src/assets/doc/otdih/straxovanie.doc">ПРОГРАММА СТРАХОВАНИЯ ОТ НЕСЧАСТНЫХ
                                    СЛУЧАЕВ</a></strong></li>
                        <!--<li><strong><a href="doc/otdih/DMS.doc">ПРОГРАММА  ДОБРОВОЛЬНОГО МЕДИЦИНСКОГО СТРАХОВАНИЯ</a></strong></li>-->
                        <li><strong><a href="src/assets/doc/otdih/medosmotri.doc">МЕДИЦИНСКИЕ ОСМОТРЫ</a></strong></li>
                        <li><strong><a @click="dialog = true">СПОРТИВНЫЕ СЕКЦИИ</a></strong></li>
                    </ul>
                    <p align="center"><strong>&nbsp;</strong></p>
                    <p align="center"><strong>ЛЕЧЕБНО-ОЗДОРОВИТЕЛЬНЫЕ КОМПЛЕКСЫ*:</strong></p>
                    <p align="center"><strong>&nbsp;</strong></p>
                    <ul>
                        <!-- <li><strong><u><a data-toggle="modal" data-target="#arhiz" href="#">«СОСНОВЫЙ БЕРЕГ»  (п. Архыз)</a></u></strong></li><br />
                      <li><strong><u><a data-toggle="modal" data-target="#ivushka" href="#">«ИВУШКА»  (г. Таганрог)</a></u></strong></li><br />-->

                        <li><a href="src/assets/doc/otdih/Правила участия в программе РАН_2022.pdf"
                                target="_blank"><strong>Программа
                                    оздоровления РАН</strong></a></li><br>
                        <li><strong><a href="src/assets/doc/otdih/ЭКСКУРСИИ ВЫХОДНОГО ДНЯ.docx">ЭКСКУРСИИ ВЫХОДНОГО
                                    ДНЯ</a></strong>
                        </li><br>
                        <li><strong><a href="src/assets/doc/otdih/КОМПЕНСАЦИЯ ПУТЁВКИ.docx">КОМПЕНСАЦИЯ
                                    ПУТЁВКИ</a></strong></li>
                        <br>
                        <!--<p><strong>ТРК "Правый берег Дона"</strong></p>
                      <ul>
                      <li><a href="doc/otdih/ТРК Дон тур.docx">Информационное письмо</a></li>
                      <li><a href="doc/otdih/Тарифы ДТ 2018.pdf">Тарифы</a></li>
                      </ul>
                      </li><br />-->
                    </ul>
                    <p><strong><u>САНАТОРНО-ОЗДОРОВИТЕЛЬНОЕ ЛЕЧЕНИЕ </u></strong></p>
                    <ul>
                        <li><a href="http://www.obkomprof.ru/pages/ozdorov/ozdstart.htm">Программа
                                санаторно-оздоровительного лечения Ростовской областной организации Профсоюза работников
                                народного образования и науки РФ</a></li>
                    </ul>
                    <p><strong></strong></p>
                    <p><strong>*</strong><strong>оздоровление работников осуществляется только во время отпуска, в
                            выходные
                            и праздничные дни по предварительной заявке</strong><strong> </strong></p>
                    <q-dialog v-model="dialog" ref="dialogRef">
                        <q-card class="modal-otdih">
                            <OtdihModal v-on:close-dialog="closeDialog" />
                        </q-card>
                    </q-dialog>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup lang="ts">
import SideBar from 'src/layouts/SideBar.vue';
import OtdihModal from 'src/components/OtdihModal.vue';
import { ref } from 'vue';

var dialog = ref<boolean>(false);
function closeDialog() {
    dialog.value = false
}
</script>
