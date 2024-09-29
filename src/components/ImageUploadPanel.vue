<template>
  <v-card class="upload-card" height="90vh">
    <v-card-title>Image Upload & Preview</v-card-title>
    <v-card-text class="upload-content">
      <!-- Clickable Drag and Drop Area -->
      <div class="drop-area" @dragover.prevent @drop.prevent="handleDrop" @dragenter.prevent="dragging = true"
        @dragleave.prevent="dragging = false" @click="openFilePicker"
        :class="{ 'dragging': dragging, 'with-images': imagePreviews.length > 0 }">
        <div v-if="imagePreviews.length === 0" class="my-10">
          <img src="../assets/add-image.png" alt="placeholder" class="placeholder-image" />
          <p class="mb5">Drag and drop your images here, or click to select files</p>

        </div>

        <p v-if="!dragging && imagePreviews.length > 0">Click to add more images</p>

      </div>


      <!-- Hidden File Input -->
      <v-file-input ref="fileInput" v-model="selectedImages" multiple show-size hide-details
        accept="image/jpeg, image/png" style="display: none;" @change="previewImages"></v-file-input>

      <!-- Image Previews -->
      <div v-if="imagePreviews.length" class="preview-container">
        <v-row>
          <v-col v-for="(img, index) in imagePreviews" :key="index" cols="4" class="image-preview">
            <div class="image-container">
              <v-img :src="img.src" max-width="100%" height="100px" class="preview-image"
                :alt="'Preview ' + (index + 1)" contain />
              <v-btn icon class="delete-btn" @click="deleteImage(index)">
                <v-icon>mdi-delete</v-icon>
              </v-btn>
            </div>
          </v-col>
        </v-row>
      </div>
    </v-card-text>
    <v-card-actions>
      <v-btn color="primary" @click="uploadImages">
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
      dragging: false,
    };
  },
  methods: {
    // Open the file picker when the drag-and-drop area is clicked
    openFilePicker() {
      this.$refs.fileInput.click();
    },
    handleDrop(event) {
      this.dragging = false;
      const files = event.dataTransfer.files;
      this.validateAndAddFiles(files);
    },
    validateAndAddFiles(files) {
      const validTypes = ["image/jpeg", "image/png"];
      const maxSize = 5 * 1024 * 1024;

      for (const file of files) {
        if (!validTypes.includes(file.type)) {
          alert(`${file.name} is not a valid image type.`);
          continue;
        }
        if (file.size > maxSize) {
          alert(`${file.name} exceeds the 5MB size limit.`);
          continue;
        }

        this.selectedImages.push(file);
        this.previewImages();
      }
    },
    previewImages() {
      // Append new images to the existing previews
      this.selectedImages.forEach((file) => {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.imagePreviews.push({ src: e.target.result });
        };
        reader.readAsDataURL(file);
      });
    },
    deleteImage(index) {
      this.imagePreviews.splice(index, 1); // Remove image at the specific index
    },
    uploadImages() {
      if (this.selectedImages.length === 0) {
        alert("No images to upload");
        return;
      }
      this.$emit("upload", this.selectedImages);
    },
  },
};
</script>

<style scoped>
.upload-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}

.upload-content {
  flex: 1;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.drop-area {
  border: 2px dashed #aaa;
  padding: 20px;
  text-align: center;
  cursor: pointer;
  /* flex-grow: 1; */
  display: flex;
  justify-content: center;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
  height: 200px;
  transition: height 0.3s ease;
}

.drop-area.with-images {
  height: 50px;
}

.drop-area.dragging {
  background-color: #e0e0e0;
}

.preview-container {
  min-height: 60vh;
  max-height: 60vh;
  overflow-y: auto;
  overflow-x: hidden;
}

.image-preview {
  text-align: center;
  padding: 5px;
  position: relative;
}

.preview-image {
  object-fit: cover;
  max-width: 100%;
  height: 100px;
  border-radius: 4px;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
}

.image-container {
  position: relative;
}

.delete-btn {
  position: absolute;
  top: 5px;
  right: 5px;
  display: none;
}

.image-container:hover .delete-btn {
  display: block;
}

.placeholder-image {
  max-width: 100px;
  margin-bottom: 10px;
  margin-top: 20px
}
</style>
