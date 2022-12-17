<template>
  <div class="hello">
    <h1>{{ angle }}</h1>
    <h1>{{ counter }}</h1>
    <h1>{{ stage }}</h1>


    {{ videoDivice }}
    <div class="webcam">
      <video class="web_video"
        ref="webVideo"
        hidden></video>
      <canvas ref="outVideo"
        class="outVideo"
        width=640
        height=480></canvas>
    </div>
    <p-Button @click="startCamera">Start</p-Button>
    <p-Button @click="stopCamera">Stop</p-Button>
  </div>
  <div class='square-box'>
    Box below
    <div class="landmark-grid-container">
    </div>
  </div>
</template>

<script lang="ts">

import { Camera } from '@mediapipe/camera_utils';
import { Holistic, Results, POSE_CONNECTIONS, FACEMESH_TESSELATION, HAND_CONNECTIONS, NormalizedLandmark } from '@mediapipe/holistic';
import { ref, defineEmits, onBeforeUnmount, onMounted, defineComponent } from "vue";
import type { InputImage } from "@mediapipe/holistic";
import { drawConnectors, drawLandmarks } from '@mediapipe/drawing_utils';


const UNSELECTED = "empty";

export default defineComponent({
  name: "HelloWorld",
  props: {
    msg: String,
  },

});
</script>

<script setup lang="ts">

const emit = defineEmits(['inFocus', 'count'])

const videoDivice = ref(localStorage.getItem('videoDivice') || '')
const counter = ref(0);
const angle = ref(0);
const stage = ref("hello");


const webVideo = ref<HTMLVideoElement>()
const outVideo = ref<HTMLCanvasElement>()
const camera = ref<Camera>()
const ctx = ref()


const finaAngle = (p0: NormalizedLandmark, p1: NormalizedLandmark, p2: NormalizedLandmark) => {
  const a = Math.pow(p1.x - p0.x, 2) + Math.pow(p1.y - p0.y, 2);
  const b = Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2);
  const c = Math.pow(p2.x - p0.x, 2) + Math.pow(p2.y - p0.y, 2);
  const radians = Math.acos((a + b - c) / Math.sqrt(4 * a * b));
  return radians * (180 / Math.PI);
};



const countPushUps = (angle: number) => {
  if (angle > 45) {
    stage.value = "up"
  } else if (angle <= 20) {
    if (stage.value === "up") {
      stage.value = "down"
      counter.value += 1
      emit("count", counter.value)
    }
  }

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



const startCamera = () => {
  holistic.onResults(onResults)

  if (webVideo.value) {
    camera.value = new Camera(webVideo.value, {
      onFrame: async () => {
        console.log("onFrame")
        await holistic.send({ image: webVideo.value as InputImage });
      },
      width: 640,
      height: 480
    });
    camera.value.start();
  }
}



const onResults = (results: Results) => {
  ctx.value.save()
  ctx.value.clearRect(0, 0, 640, 480)
  ctx.value.drawImage(results.image, 0, 0, 640, 480)

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

    const tmp = finaAngle(p0, p1, p2);
    // console.log(tmp);
    angle.value = tmp;
    countPushUps(tmp);

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


  console.log(typeof webVideo.value)
  console.log(typeof webVideo.value)
  console.log(typeof ctx.value)

  if (!webVideo.value?.srcObject) {
    return
  }
  const stream = webVideo.value.srcObject as MediaStream
  const tracks = stream.getTracks()
  tracks.forEach((track) => {
    track.stop()
  })
  webVideo.value.srcObject = null
  ctx.value.clearRect(0, 0, 1280, 720)
  camera.value?.stop()
}


onMounted(() => {
  // startCamera();
  ctx.value = outVideo?.value?.getContext('2d')
})



onBeforeUnmount(async () => {
  // stopCamera()
})

// const devicesList = ref<string[]>([UNSELECTED]); // videoリスト
// navigator.mediaDevices
//   .getUserMedia({ audio: false, video: true })
//   .then((stream) => {
//     navigator.mediaDevices
//       .enumerateDevices()
//       .then((devices) => {
//         devices.forEach((device) => {
//           if (device.kind === "videoinput")
//             devicesList.value.push(device.label);
//         });
//       })
//       .catch((err) => {
//         console.error(err);
//       });
//   })
//   .catch((err) => {
//     console.error(err);
//   });
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
