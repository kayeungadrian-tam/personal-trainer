<template>
    <div class="">
        <h4>
            {{ label }}
        </h4>
        <div class="tmp2">
            <Badge size="large"
                :value="value" />
        </div>
    </div>
</template>

<style>
/* @import "@/assets/css/progressbar.css"; */
</style>

<script setup lang="ts">
import Badge from 'primevue/badge';
import { defineProps, ref } from 'vue';


const props = defineProps({
    label: { type: String, required: true },
    value: { type: Number, reuqired: true }
})


const label = ref(props.label)
const value = ref(props.value)


</script>


<style scoped>
.p-badge {
    /* background-color: rgba(); */
    background: transparent;
    color: black;

    /* box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37); */
    /* backdrop-filter: blur(4px); */
}
</style>