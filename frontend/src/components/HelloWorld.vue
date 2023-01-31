<template>

  <ConfirmDialog></ConfirmDialog>
  <div class="hello"
    style="color: white">
    <!-- <h1>{{ distance }}</h1> -->
    <!-- <h1>{{ delay }}</h1> -->
    <div class="button-container">


      <p-Button v-if="!start"
        class="animate__animated
      animate__flash 
      
      animate__infinite animate__slower

      p-button-raised p-button-rounded
      go-button
      "
        @click="startCamera">
        GO</p-Button>
      <div v-else>
        <span class="exercise-count">{{ counter }}</span>
      </div>
    </div>




    <Knob v-model="delay"
      :min="0"
      :max="30" />

    {{ videoDivice }}
    <div class="webcam">
      <video class="web_video"
        ref="webVideo"
        hidden></video>
      <canvas ref="outVideo"
        class="outVideo"
        style="    transform: scaleX(-1);"
        width=640
        height=480></canvas>
    </div>

  </div>
  <div class='square-box'>
    <div class="landmark-grid-container">
    </div>
  </div>
</template>

<script lang="ts">
import Knob from 'primevue/knob';
import { useConfirm } from "primevue/useconfirm";
import ConfirmDialog from 'primevue/confirmdialog';

import { Camera } from '@mediapipe/camera_utils';
import { Holistic, Results, POSE_CONNECTIONS, FACEMESH_TESSELATION, HAND_CONNECTIONS, NormalizedLandmark } from '@mediapipe/holistic';
import { ref, defineEmits, onBeforeUnmount, onMounted, onUnmounted, defineComponent } from "vue";
import type { InputImage } from "@mediapipe/holistic";
import { drawConnectors, drawLandmarks } from '@mediapipe/drawing_utils';

import { useRouter } from 'vue-router';


const UNSELECTED = "empty";

export default defineComponent({
  name: "HelloWorld",
  props: {
    msg: String,
  },

});
</script>

<script setup lang="ts">
const emit = defineEmits(['next', 'count'])

const router = useRouter();
const start = ref(false);

const videoDivice = ref(localStorage.getItem('videoDivice') || '')
const counter = ref(0);
const angle = ref(0);
const stage = ref("hello");
const haha = ref(0)

const webVideo = ref<HTMLVideoElement>()
const outVideo = ref<HTMLCanvasElement>()
const camera = ref<Camera>()
const ctx = ref()

const MAX_HIEGHT = ref(480);

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

const countSquats = (shoulderY: number) => {
  if (shoulderY > 240) {
    stage.value = "up"
  } else if (shoulderY <= 400) {
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



const confirm = useConfirm();

const showConfirm = () => {

  confirm.require({
    message: 'Are you sure you want to proceed?',
    header: 'Confirmation',
    icon: 'pi pi-exclamation-triangle',
    accept: () => {
      //callback to execute when user confirms the action
    },
    reject: () => {
      //callback to execute when user rejects the action
    },
    onHide: () => {
      //callback to execute when dialog is hidden
    }
  });
}

const startCamera = () => {
  holistic.onResults(onResults)

  if (webVideo.value) {
    camera.value = new Camera(webVideo.value, {
      onFrame: async () => {
        await holistic.send({ image: webVideo.value as InputImage });
      },
      width: 640,
      height: 480
    });
    camera.value.start();
  }
  start.value = !start.value;


}



const onResults = (results: Results) => {
  ctx.value.save()
  ctx.value.clearRect(0, 0, 640, 480)
  ctx.value.drawImage(results.image, 0, 0, 640, 480)

  detectHolistic(results)
  ctx.value.restore()
}


const getDistance = (x1: number, y1: number, x2: number, y2: number) => {
  let y = x2 - x1;
  let x = y2 - y1;
  return Math.sqrt(x * x + y * y);
}

const distance = ref(0);
const delay = ref(0);

const detectHolistic = (results: Results) => {
  if (results.poseLandmarks) {
    const p0 = results.poseLandmarks[23];
    const p1 = results.poseLandmarks[11];
    const p2 = results.poseLandmarks[13];


    const left_shoulder = results.poseLandmarks[11];
    const right_shoulder = results.poseLandmarks[12];

    haha.value = (left_shoulder.y + right_shoulder.y) / 2;

    const right_hand_points = [17, 19, 21];

    const right_average = [0, 0];

    right_hand_points.forEach((landmarks_idx, i) => {
      right_average[0] += results.poseLandmarks[landmarks_idx].x;
      right_average[1] += results.poseLandmarks[landmarks_idx].y;
    })


    distance.value = getDistance(right_average[0] / 3, right_average[1] / 3, p1.x, p1.y)
    if (distance.value < 0.1) {
      if (delay.value <= 30) {
        delay.value += 1;
      } else {
        emit("next", true)
        counter.value = 0;
        delay.value = 0;
      }
    }
    // console.log(distance);

    const tmp = finaAngle(p0, p1, p2);
    // console.log(tmp);
    angle.value = tmp;
    // countPushUps(tmp);
    countSquats(haha.value * MAX_HIEGHT.value);

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
    // drawConnectors(ctx.value, results.rightHandLandmarks, HAND_CONNECTIONS,
    // { color: '#CC0000', lineWidth: 5 });
    // drawLandmarks(ctx.value, results.rightHandLandmarks,
    // { color: '#CC0000', lineWidth: 2 });
  }
  else {
    console.log("Not detected.")
  }

}


function stopBothVideoAndAudio(stream: any) {
  stream.getTracks().forEach(function (track: any) {
    if (track.readyState == 'live') {
      track.stop();
    }
  });
}


const stopCamera = () => {




  if (!webVideo.value?.srcObject) {
    return
  }
  const stream = webVideo.value.srcObject as MediaStream
  stopBothVideoAndAudio(stream);
  // const tracks = stream.getTracks()
  // tracks.forEach((track) => {
  // track.stop();
  // })
  webVideo.value.srcObject = null
  ctx.value.clearRect(0, 0, 1280, 720)
  camera.value?.stop()
}


onMounted(() => {
  // startCamera();
  ctx.value = outVideo?.value?.getContext('2d')
})

onUnmounted(() => {
  // stopCamera();
  console.log("Unmounted");
})

onBeforeUnmount(() => {
  stopCamera()
  console.log("BeforeUnmounted");

})

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import 'animate.css';

.outVideo {
  /* visibility: hidden; */
  /* opacity: 0.5; */
  border-radius: 50px;
  filter: brightness(50%)
}

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

.exercise-count {
  color: antiquewhite;
  font-size: 5rem
}

.button-container {
  width: 400px;
  height: 400px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1;
}

.go-button {
  font-size: 5rem;
  --animate-duration: 2.5s;
}

.go-button:hover {
  cursor: pointer;
  /* --animate-duration: 0s; */

}
</style>
