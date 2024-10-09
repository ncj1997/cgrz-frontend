<template>
  <v-card elevation="5" class="processed-image-card">
    <v-card-title class="bg-blue-lighten-5 mb-2">Processed Output Image</v-card-title>

    <v-card-text class="text-center">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" class="text-center">
            <!-- Loading Indicator -->
            <v-container v-if="loading">
              <v-row class="text-center">
                <v-col>
                  <v-img
                    class="mx-auto"
                    src="../../static/pictures.png"
                    width="150"
                    height="150"
                    contain
                  />
                  <p>Processing images, please wait...</p>
                </v-col>
              </v-row>
            </v-container>

            <!-- Display the processed image or placeholder -->
            <v-img
              v-else-if="imageUrl"
              :src="imageUrl"
              max-width="100%"
              contain
            />
            <v-img
              v-else
              src="../assets/add-image.png"
              max-width="30%"
              contain
            />

            <!-- Display the detection result if available -->
            <p v-if="detectionResult && !loading" class="mt-2">{{ detectionResult }}</p>
          </v-col>
        </v-row>
      </v-container>
    </v-card-text>

    <v-card-actions>
      <v-btn
        variant="outlined"
        class="mx-auto"
        @click="downloadImage"
        :disabled="!imageUrl"
      >
        Download Image
      </v-btn>
    </v-card-actions>
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
