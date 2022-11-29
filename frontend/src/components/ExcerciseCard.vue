<template>
    <div class="excercise-card">

        <Card>

            <template #header>
                <img v-if="(msg == 'Push up')"
                    src="../assets/excercise/push_up.gif"
                    alt="Image Text" />
                <img v-else
                    src="../assets/excercise/jump_squat.gif">
            </template>
            <template #title>
                {{ msg }}<br>
                <Tag value="New"></Tag>
            </template>
            <template #content>

            </template>
            <template #footer>


                <Knob v-model="value"
                    :size="60"
                    :disabled="true"
                    valueColor="red"
                    :min="0"
                    :max="100" />

                <p-Button icon="pi pi-chevron-right"
                    label="GO!"
                    class="p-button-success"
                    style="margin-left: .5em" />
            </template>
        </Card>


    </div>

</template>

<style>
@import "@/assets/css/excerciseCard.css";
</style>

<script lang="ts">

</script>

<script setup lang="ts">

import Card from 'primevue/card';
import Tag from 'primevue/tag';
import Image from 'primevue/image';
import Knob from 'primevue/knob';
import { ref, defineComponent, PropType, defineProps } from 'vue';


const props = defineProps({
    msg: {
        type: String,
        required: true
    },
    progress: {
        type: Number
    },
})

const value = ref(props.progress)


const getThumbnail = (name: string) => {
    if (name == "Push up") {
        return "../assets/excercise/push_up.gif"
    } else {
        return "ADRIAN"
    }
}

const img_thumbnail = ref(getThumbnail(props.msg))


const items = ref([

    {
        title: "title",
        tag: "tag",
    },

    {
        title: "title",
        tag: "tag",
    },
    {
        title: "title",
        tag: "tag",
    },
    {
        title: "title",
        tag: "tag",
    },
    {
        title: "title",
        tag: "tag",
    },
    {
        title: "title",
        tag: "tag",
    },
])

</script>