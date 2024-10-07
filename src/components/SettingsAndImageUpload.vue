<template>
  <v-card elevation="5" class="upload-card">
    <v-card-title class="bg-blue-lighten-5 mb-2 pt-4">Settings & Image Upload</v-card-title>
    <v-card-text class="upload-content">
      <v-form ref="form">
        <v-row>
          <!-- Object Type Selection -->
          <v-col>
            <v-select v-model="selectedObjectType" :items="objectTypes" label="Select Object Type" outlined required />
          </v-col>
        </v-row>

        <v-row>
          <!-- Environment Image Upload -->
          <v-col>
            <div class="drop-area" @dragover.prevent @drop.prevent="handleDrop" @click="openFilePicker">
              <div v-if="!environmentImagePreview" class="my-10">
                <p>Drag and drop Environment Image here, or click to select files</p>
              </div>
              <img v-if="environmentImagePreview" :src="environmentImagePreview" class="preview-image" />
            </div>
            <v-file-input ref="environmentFileInput" @change="previewEnvironmentImage" accept="image/jpeg, image/png" style="display: none" />
            <v-btn @click="openEnvironmentFilePicker">Upload Environment Image</v-btn>
          </v-col>

          <!-- Camouflage Image Upload -->
          <v-col>
            <div class="drop-area" @dragover.prevent @drop.prevent="handleDropCamouflage" @click="openCamouflageFilePicker">
              <div v-if="!camouflageImagePreview" class="my-10">
                <p>Drag and drop Camouflage Image here, or click to select files</p>
              </div>
              <img v-if="camouflageImagePreview" :src="camouflageImagePreview" class="preview-image" />
            </div>
            <v-file-input ref="camouflageFileInput" @change="previewCamouflageImage" accept="image/jpeg, image/png" style="display: none" />
            <v-btn @click="openCamouflageFilePicker">Upload Camouflage Image</v-btn>
          </v-col>
        </v-row>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-btn color="primary" @click="uploadImages">Process Images</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      selectedObjectType: null,
      objectTypes: ['Humans', 'Vehicles'],
      environmentImage: null,  // Correct binding for environment image
      camouflageImage: null,   // Correct binding for camouflage image
      environmentImagePreview: '',
      camouflageImagePreview: '',
    };
  },
  methods: {
    openEnvironmentFilePicker() {
      this.$refs.environmentFileInput.click();  // Trigger file input click for environment
    },
    openCamouflageFilePicker() {
      this.$refs.camouflageFileInput.click();  // Trigger file input click for camouflage
    },
    handleDrop(event) {
      const files = event.dataTransfer.files;
      this.validateAndAddFiles(files, 'environment');
    },
    handleDropCamouflage(event) {
      const files = event.dataTransfer.files;
      this.validateAndAddFiles(files, 'camouflage');
    },
    validateAndAddFiles(files, type) {
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

        if (type === 'environment') {
          this.environmentImage = file;  // Correctly assign environment image
          this.previewEnvironmentImage({ target: { files: [file] } }); // Trigger the preview
        } else if (type === 'camouflage') {
          this.camouflageImage = file;  // Correctly assign camouflage image
          this.previewCamouflageImage({ target: { files: [file] } }); // Trigger the preview
        }
      }
    },
    previewEnvironmentImage(event) {
      const file = event.target.files ? event.target.files[0] : this.environmentImage;
      if (!file) return;

      this.environmentImage = file;  // Assign the selected file
      const reader = new FileReader();
      reader.onload = (e) => {
        this.environmentImagePreview = e.target.result;  // Update preview
      };
      reader.readAsDataURL(file);
    },
    previewCamouflageImage(event) {
      const file = event.target.files ? event.target.files[0] : this.camouflageImage;
      if (!file) return;

      this.camouflageImage = file;  // Assign the selected file
      const reader = new FileReader();
      reader.onload = (e) => {
        this.camouflageImagePreview = e.target.result;  // Update preview
      };
      reader.readAsDataURL(file);
    },
    uploadImages() {
      // Debugging: Check if images are assigned
      console.log("Selected object type:", this.selectedObjectType);
      console.log("Environment image:", this.environmentImage);
      console.log("Camouflage image:", this.camouflageImage);

      if (!this.environmentImage || !this.camouflageImage || !this.selectedObjectType) {
        alert("Please select images and an object type.");
        return;
      }

      // Emit upload event
      this.$emit('upload', {
        environmentImage: this.environmentImage,
        camouflageImage: this.camouflageImage,
        objectType: this.selectedObjectType.toLowerCase(),
      });
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
  width: 100%;
}

.drop-area {
  padding: 20px;
  text-align: center;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
  height: 200px;
  transition: height 0.3s ease;
}

.preview-image {
  max-width: 100%;
  height: 100px;
}
</style>
