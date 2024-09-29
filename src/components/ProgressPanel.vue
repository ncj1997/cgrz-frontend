<!-- src/components/ProgressPanel.vue -->
<template>
    <v-card>
      <v-card-title>Progress Updates</v-card-title>
      <v-card-text>
        <div v-if="loading">
          <v-progress-linear indeterminate color="primary"></v-progress-linear>
          <p>{{ progressMessages[0] }}</p>
        </div>
        <div v-else>
          <p v-for="(msg, index) in progressMessages" :key="index">{{ msg }}</p>
        </div>
  
        <div v-if="finalImageUrl">
          <v-img :src="finalImageUrl" max-width="300" class="mt-3" />
          <p>Final processed image is ready!</p>
        </div>
      </v-card-text>
    </v-card>
  </template>
  
  <script>
  export default {
    props: {
      progressMessages: Array,
      finalImageUrl: String,
      loading: Boolean,
    },
  };
  </script>
  