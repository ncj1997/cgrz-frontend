<template>
  <v-container fluid class="pa-1">
    <v-row>
      <!-- Left Panel: Settings and Image Upload -->
      <v-col>
        <SettingsAndImageUpload @upload="processImages" />
      </v-col>

      <!-- Right Panel: Processed YOLO Image -->
      <v-col>
        <ProcessedYoloImage
          :imageUrl="processedImageUrl"
          :detectionResult="detectionResult"
          :loading="loading"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import SettingsAndImageUpload from '@/components/SettingsAndImageUpload.vue';
import ProcessedYoloImage from '@/components/ProcessedYoloImage.vue';

export default {
  components: {
    SettingsAndImageUpload,
    ProcessedYoloImage,
  },
  data() {
    return {
      processedImageUrl: null, // Holds the URL of the processed image returned from the API
      detectionResult: '',     // Holds the detection result (message or status) from the API
      loading: false,          // Loading indicator for the API call
    };
  },
  methods: {
    // Function to handle the image processing
    async processImages({environmentImage, camouflageImage, objectType}) {
      const formData = new FormData();
      formData.append('environment_image', environmentImage);
      formData.append('camouflage_image', camouflageImage);
      formData.append('object_type', objectType);

      try {
        this.loading = true; // Start loading spinner
        const response = await fetch('http://backend.intelilab.click/apply_camouflage', {
          method: 'POST',
          body: formData,
        });

        // Check if the response was successful
        if (!response.ok) {
          throw new Error('Error processing images');
        }

        // Parse the response from the backend
        const data = await response.json();

        // Set the processed image URL and detection result
        this.processedImageUrl = data.image_url;
        this.detectionResult = data.detection_result;
      } catch (error) {
        console.error('Error processing images:', error);
      } finally {
        this.loading = false; // Stop loading spinner
      }
    },
  },
};
</script>

<style scoped>
.v-container {
  padding: 1px;
}
</style>
