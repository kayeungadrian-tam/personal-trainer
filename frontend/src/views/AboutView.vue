<template>
  <NavBar />
  <div class="home">
    <div class="title">
      <h1>Quiz</h1>
    </div>
    <!-- <CameraVue /> -->

    <p-Button @click="checked[2] = true">SET</p-Button>

    <p-Button @click="get_quiz">Quiz</p-Button>
    <div class="quiz-area">
      <div class="quiz-card"
        v-for="(problem, i) in problems"
        :key="i">

        <Fieldset>
          <template #legend>
            <div class="quiz-header">
              #{{ i + 1 }} - {{ problem.category }}
            </div>
          </template>
          <div class="quiz-question">
            <h3>{{ problem.question }}</h3>
          </div>
          <div class="quiz-answers">
            <div class="quiz-indvidual-answer"
              v-for="(answer, i ) in problem.incorrectAnswers"
              :key="i">
              <ToggleButton :disabled="true"
                :onLabel="`[${answerConditions[i]}]  ${answer}`"
                :offLabel="`[${answerConditions[i]}] ${answer}`"
                v-model="checked[i]"
                offIcon="pi pi-circle"
                onIcon="pi pi-check-circle" />
            </div>

            <ToggleButton :disabled="true"
              :onLabel="`[${answerConditions[3]}]  ${problem.correctAnswer}`"
              :offLabel="`[${answerConditions[3]}]  ${problem.correctAnswer}`"
              v-model="checked[3]"
              offIcon="pi pi-circle"
              onIcon="pi pi-check-circle" />

          </div>
        </Fieldset>

        {{ choices }}
      </div>
    </div>
    <HelloWorld @count="chooseAnswer"
      @next="get_quiz" />
  </div>
</template>

<style>
@import "@/assets/css/quizview.css";
</style>


<script setup lang="ts">
import HelloWorld from '@/components/HelloWorld.vue';
import Fieldset from 'primevue/fieldset';
import CameraVue from '@/components/Camera.vue';
import NavBar from '@/components/NavBar.vue';
import ToggleButton from 'primevue/togglebutton';

// import get_quiz from '@/composables/quiz';
import { ref } from 'vue';
import axios from 'axios';

const answerConditions = ref([2, 4, 6, 7])
const currentCounter = ref(0);

const chooseAnswer = (count: number) => {
  console.log(count)
  answerConditions.value.forEach((number, index) => {
    if (count === number) {
      console.log("YES!")
      checked.value = [false, false, false, false]
      checked.value[index] = true

    }
  })
  const i = count % 2;
}

const problems = ref()
const checked = ref([false, false, false, false])
const choices = ref()

const get_quiz = async () => {
  answerConditions.value.forEach((number, index) => {
    answerConditions.value[index] = Math.floor(Math.random() * 10) + 1
  })
  const choices = []
  const url = "https://the-trivia-api.com/api/questions?limit=1"

  const respone = await axios.get(url);
  checked.value = [false, false, false, false]

  problems.value = respone.data;

  for (var data of respone.data) {
    console.log(data.correctAnswer);
    for (var answer of data.incorrectAnswers) {
      choices.push({ label: answer, correc: false })
    }
    // answers.value.push({ "answer": answer, "correct": 0 })
  }

  const correctAnswer = respone.data.correctAnswer;
  // answers.value = respone.data.incorrectAnswers;
  // answers.value.push(respone.data.correctAnswer);
  console.log(choices);

  // return respone
};




// const quiz_result = async () => {
//   const response = get_quiz();
//   problem.value = response;
// }

</script>