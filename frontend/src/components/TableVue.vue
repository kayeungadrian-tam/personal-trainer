<template>
    <div class="table">
        <DataTable :value="data.data"
            responsiveLayout="scroll"
            :sortOrder="-1">
            <Column field="rank"
                header="Ranking"></Column>
            <Column field="name"
                header="Name">
            </Column>
            <Column field="count"
                header="Count"
                :sortable="true">
            </Column>
            <Column field="rating"
                header="Reviews">
                <template #body="slotProps">
                    <Rating :modelValue="slotProps.data.rating"
                        :readonly="true"
                        :cancel="false">
                        <template #onicon>
                            <img src="@/assets/icon/fire_on.png"
                                height="24"
                                width="24">
                        </template>
                        <template #officon>
                            <img src="@/assets/icon/fire_off.png"
                                height="24"
                                width="24">
                        </template>
                    </Rating>
                </template>
            </Column>

        </DataTable>
    </div>
</template>


<script setup lang="ts">
import { defineProps, ref } from 'vue';



import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';
import Row from 'primevue/row';

import Rating from 'primevue/rating';


const props = defineProps({
    data: { type: Object, required: true },
    columns: { type: Array, reuqired: true }
})


const data = ref(props.data)
const columns = ref(props.columns)


</script>


<style scoped>
@import "@/assets/css/table.css";
</style>