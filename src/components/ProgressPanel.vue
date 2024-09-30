<template>
  <v-card elevation="5" class="progress-card" >
    <v-card-title>Progress Updates</v-card-title>

    <!-- Initial Description State (Before Upload) -->
    <v-card-text v-if="!loading && !finalImageUrl">
      <p class="initial-state-text">
        Upload multiple images of an environment, and a camouflage pattern will be generated for the images.
      </p>
    </v-card-text>

    <!-- Progress State -->
    <v-card-text v-if="loading" class="progress-content">
      <v-progress-linear v-if="loading" stream striped :model-value="progressPercentage" height="10" color="primary"
        class="progress-bar"></v-progress-linear>

      <!-- Step Image with Transition -->
      <transition name="fade" mode="out-in">
        <img v-if="currentStep > 0 && currentStep <= totalSteps" :src="`/static/step${currentStep}.png`"
          :alt="`Step ${currentStep}`" class="step-image" key="step-image" />
      </transition>

      <!-- Progress Messages -->
      <transition-group name="fade" mode="out-in">
        <p v-for="(msg, index) in progressMessages" :key="index" class="progress-text">
          {{ msg }}
        </p>
      </transition-group>
    </v-card-text>

    <!-- Final Image Display -->
    <v-card-text v-if="finalImageUrl">
      <p class="final-text">Camouflage generated successfully!</p>
      <v-img :src="finalImageUrl" max-width="50vw" max-height="65vh" />

      <!-- Download Button -->
      <v-btn class="mt-5 mx-auto" variant="outlined" color="primary" @click="downloadImage">
        Download Image
      </v-btn>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    progressMessages: Array,
    currentStep: Number,
    totalSteps: Number,
    loading: Boolean,
    finalImageUrl: String, // New prop to hold the final processed image URL
  },
  computed: {
    progressPercentage() {
      return (this.currentStep / this.totalSteps) * 100;
    },
  },
  methods: {
    downloadImage() {
      const filename = this.finalImageUrl.split('/').pop(); 
      console.log(filename)// Extract the filename from the URL
      const downloadUrl = `https://backend.intelilab.click/download-image/${filename}`; // Point to the Flask download route

      // Make a GET request to trigger the download
      fetch(downloadUrl)
        .then(response => response.blob())
        .then(blob => {
          const link = document.createElement('a');
          const objectURL = URL.createObjectURL(blob); // Create an object URL for the blob
          link.href = objectURL;
          link.setAttribute('download', filename); // Set the file name for download
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link); // Clean up
          URL.revokeObjectURL(objectURL); // Revoke the object URL to free up memory
        })
        .catch(error => {
          console.error('Error downloading image:', error);
        });
    },
  },
};
</script>

<style scoped>
.progress-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}

.progress-content {
  flex: 1;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.progress-bar {
  margin-bottom: 20px;
}

.step-image {
  max-width: 150px;
  margin-bottom: 20px;
  transition: opacity 0.5s ease;
}

.progress-text {
  font-size: 18px;
  text-align: center;
}

.initial-state-text {
  font-size: 18px;
  text-align: center;
  margin: 20px;
}

.final-text {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 15px;
}

.final-image {
  margin-bottom: 20px;
}



.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
