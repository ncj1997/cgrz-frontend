<!-- src/App.vue -->
<template>
  <v-container class="mx-auto">
    <v-row class="mx-0">
      <!-- Left Panel: Image Upload and Preview -->
      <v-col cols="6">
        <ImageUploadPanel @upload="uploadImages" />
      </v-col>

      <!-- Right Panel: Progress Updates -->
      <v-col cols="6">
        <ProgressPanel :currentStep="currentStep" :totalSteps=totalSteps :progressMessages="progressMessages"
          :finalImageUrl="finalImageUrl" :loading="loading" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

export default {
  data() {
    return {
      currentStep: 1,
      totalSteps: 5,
      progressMessages: [],
      finalImageUrl: null,
      loading: false,
    };
  },
  methods: {
    async uploadImages(selectedImages) {
      this.loading = true;
      this.progressMessages = [];
      this.finalImageUrl = null;

      const formData = new FormData();
      selectedImages.forEach((file) => formData.append('images', file));

      try {
        const response = await fetch('https://backend.intelilab.click/progress', {
          method: 'POST',
          body: formData,
        });

        if (!response.ok) {
          throw new Error('Error uploading images');
        }

        const reader = response.body.getReader();
        const decoder = new TextDecoder('utf-8');

        let loading = true;

        while (loading) {
          const { done, value } = await reader.read();
          if (done) break;

          const chunk = decoder.decode(value, { stream: true });
          const messages = chunk.split('\n\n');

          for (const message of messages) {
            if (message.startsWith('data:')) {
              const progressMessage = message.replace('data: ', '').trim();

              this.progressMessages = [progressMessage];

              // Extract the step number from the message
              const stepMatch = message.match(/Step (\d+):/);
              if (stepMatch && stepMatch[1]) {
                this.currentStep = parseInt(stepMatch[1], 10); // Convert step number to integer
              }

              if (progressMessage.includes('Image processed')) {
                this.loading = false;

                const urlMatch = progressMessage.match(/View at (.*)/);
                if (urlMatch && urlMatch[1]) {
                  this.finalImageUrl = urlMatch[1];
                  console.log(this.finalImageUrl)
                }

                loading = false;
                break;
              }
            }
          }
        }
      } catch (error) {
        console.error('Error uploading images:', error);
        this.loading = false;
        this.progressMessages.push('Error occurred while uploading images.');
      }
    },
  },
};
</script>

<style scoped>
v-container {
  padding: 1px;
}
</style>
