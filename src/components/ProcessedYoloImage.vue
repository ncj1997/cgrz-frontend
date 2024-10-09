<template>
  <v-card elevation="5" class="processed-image-card">
    <v-card-title class="bg-blue-lighten-5 mb-2">Processed Output Image</v-card-title>

    <v-card-text class="d-flex justify-center align-center">
      <v-container>
        <v-row>
          <v-col>
            <!-- Loading Indicator -->
            <v-container class="d-flex justify-center align-center" v-if="loading">
              <v-row class="text-center">
                <v-col class="text-center">
                  <!-- Using v-img to display the GIF -->
                  <v-img class="mx-auto" src="../../public/static/computer.gif" alt="Sample GIF" width="150"
                    height="150" contain></v-img>
                  <span>
                    Selected Images are being Uploading
                  </span>
                </v-col>
              </v-row>
            </v-container>
            <v-container v-else-if="imageUrl">
              <v-row>
                <!-- <v-img class="mx-auto" :src="imageUrl" max-width="60%" contain /> -->
                <v-img class="mx-auto" :src="imageUrl"  max-width="400">
                  <template v-slot:placeholder>
                    <v-progress-circular class="mx-auto" indeterminate color="primary"></v-progress-circular>
                  </template>
                </v-img>
              </v-row>
              <v-row>
                <v-chip variant="outlined" label color="success" class="mx-auto mt-4"
                  v-if="detectionResult && !loading">{{
                    detectionResult }}</v-chip>
              </v-row>
              <v-row>
                <v-btn variant="outlined" color="primary" class="mx-auto mt-4" @click="downloadImage"
                  :disabled="!imageUrl">
                  Download Image
                </v-btn>
              </v-row>
            </v-container>
            <v-container class="d-flex justify-center align-center" v-else>

              <v-row class="text-center">
                <v-col>
                  <v-img class="mx-auto" src="../assets/add-image.png" max-width="8vw" contain />
                  <v-chip class="mt-4 mx-auto" label>Please Upload Images to the left panel to see the processed
                    output</v-chip>
                </v-col>
              </v-row>
            </v-container>


            <!-- Display the processed image or placeholder -->



            <!-- Display the detection result if available -->

          </v-col>
        </v-row>
      </v-container>
    </v-card-text>


  </v-card>
</template>

<script>
export default {
  props: {
    imageUrl: {
      type: String,
      default: null,
    },
    detectionResult: {
      type: String,
      default: 'No detection results available.',
    },
    loading: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    downloadImage() {
      if (this.imageUrl) {
        const link = document.createElement('a');
        link.href = this.imageUrl;
        link.download = 'processed_image.png'; // Default name for the downloaded file
        link.click();
      }
    },
  },
};
</script>

<style scoped>
.processed-image-card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
  position: relative;
}

.text-center {
  text-align: center;
}
</style>
