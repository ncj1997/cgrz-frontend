<!-- src/App.vue -->
<template>
  <v-container fluid class="pa-1">
    <v-row>
      <!-- Left Panel: Image Upload and Preview -->
      <v-col>
        <ImageUploadPanel height="85vh" @upload="uploadImages" />
      </v-col>

      <!-- Right Panel: Progress Updates -->
      <v-col>
        <ProgressPanel height="85vh" :currentStep="currentStep" :totalSteps=totalSteps
          :steps ="steps" :loading="loading" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

export default {
  data() {
    return {
      currentStep: 0,
      totalSteps: 5,
      steps: [],
      progressMessages: [],
      finalImageUrl: null,
      loading: false,

    };
  },
  methods: {
    async uploadImages(selectedImages) {
      this.loading = true;
      // this.currentStep = 0
      // this.steps = []
      this.progressMessages = [];
      this.finalImageUrl = null;

      const formData = new FormData();
      selectedImages.forEach((file) => formData.append('images', file));

      try {
        const response = await fetch('http://localhost:8080/gencam', {
          method: 'POST',
          headers: {
            'Content-Type': 'multipart/form-data'
          },
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

              const data = JSON.parse(progressMessage);

              // Push each new step to the reactive steps array
              this.steps.push({
                id: data.id,
                description: data.description,
                imageUrl: data.imageUrl,
                status: data.status
              });
              console.log(data.description)
              this.currentStep = data.id

              if (this.currentStep == this.totalSteps) {
                this.loading = false;
                return

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
