<template>

    <button @click="swtichCamera">Swtich</button>
    <h1>Open? {{ isOpen }}</h1>
    <div class="root">
        <video v-if="isOpen"
            :srcObject.prop="captureStream"
            id="video"
            ref="webVideo"
            autoplay
            playsinline
            width=1280
            height=720
            muted></video>
        <button @click="testFrame">Frame</button>
        <canvas v-if="isOpen"
            ref="outVideo"
            class="outVideo"
            width="1280"
            height="720"></canvas>
    </div>
</template>

<script lang="ts">
import { onBeforeUnmount, onMounted, defineComponent } from "vue";

import '@tensorflow/tfjs-backend-webgl';

export default defineComponent({
    name: "CameraVue",


});




</script>


<script setup lang="ts">

import { ref, watch } from "vue";
import { Holistic, Results, POSE_CONNECTIONS, FACEMESH_TESSELATION, HAND_CONNECTIONS, NormalizedLandmark } from '@mediapipe/holistic';
import { drawConnectors, drawLandmarks } from '@mediapipe/drawing_utils';
import type { InputImage } from "@mediapipe/holistic";
import * as tf from '@tensorflow/tfjs'
import * as posenet from '@tensorflow-models/posenet';
const captureStream = ref<MediaStream | undefined>();
const isOpen = ref(false);
const webVideo = ref<HTMLVideoElement>()
const outVideo = ref<HTMLCanvasElement>()
const ctx = ref()


const tmp = document.getElementById("video");


const interval = ref();


const onResults = (results: Results) => {
    ctx.value.save()
    ctx.value.clearRect(0, 0, 1280, 720)
    ctx.value.drawImage(results.image, 0, 0, 1280, 720)

    detectHolistic(results)
    ctx.value.restore()
}



const detectHolistic = (results: Results) => {
    if (results.poseLandmarks) {
        // console.log(results.poseLandmarks[11].x);
        // const x = results.poseLandmarks[386].x;
        const p0 = results.poseLandmarks[23];
        const p1 = results.poseLandmarks[11];
        const p2 = results.poseLandmarks[13];

        drawConnectors(ctx.value, results.poseLandmarks, POSE_CONNECTIONS, {
        });
        drawLandmarks(ctx.value, results.poseLandmarks,
            { color: '#FCAE1E', lineWidth: 2 });
        drawConnectors(ctx.value, results.faceLandmarks, FACEMESH_TESSELATION,
            { color: '#C0C0C070', lineWidth: 1 });
        drawConnectors(ctx.value, results.leftHandLandmarks, HAND_CONNECTIONS,
            { color: '#00FF00', lineWidth: 5 });
        drawLandmarks(ctx.value, results.leftHandLandmarks,
            { color: '#00FF00', lineWidth: 2 });
        drawConnectors(ctx.value, results.rightHandLandmarks, HAND_CONNECTIONS,
            { color: '#CC0000', lineWidth: 5 });
        drawLandmarks(ctx.value, results.rightHandLandmarks,
            { color: '#CC0000', lineWidth: 2 });
    }
    else {
        console.log("Not detected.")
    }
}


const stopCamera = () => {

    const stream = captureStream.value
    const tracks = stream?.getTracks()

    tracks?.forEach((track) => {
        track.stop()
    })
    clearInterval(interval.value)
}



const handleError = (error: Error) => {
    console.error(error.name, error.message);
};


const swtichCamera = () => {
    isOpen.value = !isOpen.value;

}


const imageScaleFactor = 0.50;
const flipHorizontal = false;
const outputStride = 16;


const startCamera = async () => {


    const constraints = {
        audio: true,
        video: true,
    };

    const gotStream = (stream: MediaStream) => {
        captureStream.value = stream;
        console.log("STREMAING");
    };

    navigator.mediaDevices
        .getUserMedia(constraints)
        .then(gotStream)
        .catch(handleError);


    interval.value = setInterval(async () => {
        // await console.log('calibrations');
        if (webVideo.value) {

            webVideo.value.width = 1280;
            webVideo.value.height = 720;
            console.log("OSENMTO")

            // const pose = await net.estimateSinglePose(tmp, 0.2, false, 16);
            // await holistic.send({ image: webVideo.value as unknown as InputImage });
        }
    }, 80)


}


const holistic = new Holistic({
    locateFile: (file) => {
        return `https://cdn.jsdelivr.net/npm/@mediapipe/holistic/${file}`;
    }
});
holistic.setOptions({
    modelComplexity: 1,
    smoothLandmarks: true,
    enableSegmentation: true,
    smoothSegmentation: true,
    refineFaceLandmarks: true,
    minDetectionConfidence: 0.5,
    minTrackingConfidence: 0.5
});

holistic.onResults(onResults)

const net = ref();

onMounted(async () => {
    // startCamera();
    net.value = await posenet.load();

    ctx.value = outVideo?.value?.getContext('2d')
})

const testFrame = async () => {
    console.log(webVideo.value)
    const pose = await net.value.estimateSinglePose(webVideo.value, 0.2, false, 16);
}





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


