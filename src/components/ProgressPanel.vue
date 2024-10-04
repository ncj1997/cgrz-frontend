<template>
  <v-card v-if="currentStepIndex > 0" elevation="5" class="progress-card">
    <v-progress-linear v-if="loading" color="cyan" striped height="8" indeterminate="">
    </v-progress-linear>
    <v-card-title class="bg-blue-lighten-5 mb-2">Progress Updates</v-card-title>

    <!-- Display Current Step Image and Description -->
    <v-card-text class="text-center pt-4">
      <span>
        {{ steps[currentStepIndex - 1]["description"] }}
      </span>
      <v-container>
        <v-row class="d-flex justify-center align-center">
          <v-col class=" text-center">
            <v-img :aspect-ratio="1" class="bg-white mx-auto mt-4" :src="steps[currentStepIndex - 1]['imageUrl']"
              width="500" cover>

              <template v-slot:placeholder>
                <div class="d-flex align-center justify-center fill-height grey-lighten-4"
                  style="background-color: #FAFAFA;">
                  <v-progress-circular color="grey-lighten-4" indeterminate></v-progress-circular>
                </div>
              </template>

            </v-img>
          </v-col>
        </v-row>
        <v-row>
          <v-btn variant="outlined" class="mx-auto" :loading="loading_download"
            @click="loading_download = !loading_download">
            Download the image

            <template v-slot:loader>
              <v-progress-linear indeterminate></v-progress-linear>
            </template>
          </v-btn>
        </v-row>
      </v-container>
    </v-card-text>

    <!-- Navigation Buttons -->
    <v-btn variant="flat" color="#bbDDDD" icon="mdi-chevron-left" @click="goPrevious" class="mx-1 prev-btn"
      :disabled="(currentStepIndex === 1) || loading">

    </v-btn>
    <v-btn ariant="flat" color="#bbDDDD" icon="mdi-chevron-right" @click="goNext" class="mx-1 next-btn"
      :disabled="(currentStepIndex === totalSteps) || loading">

    </v-btn>
    <v-progress-linear v-if="loading" color="cyan" height="15" :model-value="progressPercentage">
      <p>Step {{ currentStepIndex }}/{{ totalSteps }}</p>
    </v-progress-linear>

  </v-card>

  <v-card v-else elevation="5" class="progress-card">
    <v-progress-linear v-if="loading && currentStepIndex == 0" color="cyan" striped height="8" indeterminate="">
    </v-progress-linear>
    <v-card-title class="bg-blue-lighten-5" :class="{ 'pt-4': !loading }">Progress Updates</v-card-title>
    <v-card-text class="d-flex justify-center align-center">

      <v-container v-if="loading">
        <v-row class="text-center">
          <v-col class="text-center">
            <!-- Using v-img to display the GIF -->
            <v-img class="mx-auto" src="../../public/static/computer.gif" alt="Sample GIF" width="150" height="150"
              contain></v-img>
            <span>
              Selected Images are being Uploading
            </span>
          </v-col>
        </v-row>
      </v-container>

      <v-container v-else>
        <v-row class="text-center">
          <v-col class="text-center">
            <!-- Using v-img to display the GIF -->
            <v-img class="mx-auto" src="../../public/static/pictures.png" width="120" height="120" contain></v-img>
            <span>
              Upload Image to Continue
            </span>
          </v-col>
        </v-row>
      </v-container>

    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    steps: Object,
    currentStep: Number,
    totalSteps: Number,
    loading: Boolean,

  },
  data() {
    return {
      loading_download: false,
      currentStepIndex: this.currentStep  // Initialize based on the passed prop
    };
  },
  computed: {
    progressPercentage() {
      return ((this.currentStepIndex) / this.totalSteps) * 100;
    },
    currentStepObj() {
      return this.steps[this.currentStepIndex];
    },
  },
  methods: {
    goNext() {
      // if (this.currentStepIndex < this.totalSteps - 1) {
      this.currentStepIndex++;
      // }
    },
    goPrevious() {
      if (this.currentStepIndex > 0) {
        this.currentStepIndex--;
      }
    },
  },
  watch: {
    // In case the parent passes a new step via props, update the currentStepIndex
    currentStep(newStep) {
      this.currentStepIndex = newStep;
    },
  },
};
</script>

<style scoped>
.progress-card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
  position: relative;
  /* Relative positioning to contain the buttons */
}

.step-description {
  font-size: 18px;
  text-align: center;
  margin: 20px;
}

/* Position Previous Button on the Left */
.prev-btn {
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
}

/* Position Next Button on the Right */
.next-btn {
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
}
</style>
