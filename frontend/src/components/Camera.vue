<template>
    <button @click="swtichCamera">Swtich</button>
    <h1>Open? {{ isOpen }}</h1>
    <div class="root">
        <video v-if="isOpen"
            :srcObject.prop="captureStream"
            id="video"
            autoplay
            playsinline
            muted></video>
        <button @click="testFrame">Frame</button>
        <canvas ref="outVideo"
            class="outVideo"
            width=1280
            height=720></canvas>
    </div>
</template>

<script lang="ts">
import { onBeforeUnmount, onMounted, defineComponent } from "vue";
import type { InputImage } from "@mediapipe/holistic";
import { is } from "@babel/types";




export default defineComponent({
    name: "CameraVue",


});




</script>


<script setup lang="ts">
import { ref, watch } from "vue";

const captureStream = ref<MediaStream | undefined>();
const isOpen = ref(false);
const webVideo = ref<HTMLVideoElement>()

const stopCamera = () => {

    const stream = captureStream.value
    const tracks = stream?.getTracks()

    tracks?.forEach((track) => {
        track.stop()
    })
}



const handleError = (error: Error) => {
    console.error(error.name, error.message);
};


const swtichCamera = () => {
    isOpen.value = !isOpen.value;

}

const startCamera = () => {
    const constraints = {
        audio: true,
        video: true,
    };

    const gotStream = (stream: MediaStream) => {
        captureStream.value = stream;
        console.log("STREMAING")
    };

    navigator.mediaDevices
        .getUserMedia(constraints)
        .then(gotStream)
        .catch(handleError);



}

const testFrame = () => {
    console.log(webVideo.value)
}

onMounted(() => {
    // startCamera();
})

watch(
    () => isOpen.value,
    () => {
        if (isOpen.value == true) {
            console.log("Setting up camera");
            startCamera();
        }
        else {
            stopCamera();
        }
    }
)

</script>


