<!-- src/components/ImageUploadPanel.vue -->
<template>
    <v-card>
      <v-card-title>Image Upload & Preview</v-card-title>
      <v-card-text>
        <v-file-input
          v-model="selectedImages"
          label="Upload Images"
          multiple
          show-size
          @change="previewImages"
        ></v-file-input>
  
        <div v-if="imagePreviews.length">
          <v-row>
            <v-col
              v-for="(img, index) in imagePreviews"
              :key="index"
              cols="6"
            >
              <v-img :src="img" max-width="150" class="mb-3" />
            </v-col>
          </v-row>
        </div>
      </v-card-text>
      <v-card-actions>
        <v-btn color="primary" @click="$emit('upload', selectedImages)">
          Upload
        </v-btn>
      </v-card-actions>
    </v-card>
  </template>
  
  <script>
  export default {
    data() {
      return {
        selectedImages: [],
        imagePreviews: [],
      };
    },
    methods: {
      previewImages() {
        this.imagePreviews = [];
        for (const file of this.selectedImages) {
          const reader = new FileReader();
          reader.onload = (e) => {
            this.imagePreviews.push(e.target.result);
          };
          reader.readAsDataURL(file);
        }
      },
    },
  };
  </script>
  