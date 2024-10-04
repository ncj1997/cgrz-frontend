<template>
    <div style="margin-top: 10vh;">
        <h1>Apply Adaptive Camouflage</h1>
        <p>
            Welcome to the Adaptive Camouflage Application Interface. Use this tool to segment objects and apply the
            generated camouflage patterns using YOLOv8 technology.
        </p>
        
        <h3>Instructions:</h3>
        <v-list>
            <v-list-item>
                <template v-slot:prepend>
                    <v-icon color="primary">mdi-upload</v-icon>
                </template>
                <v-list-item-title><strong>Upload an Image:</strong></v-list-item-title>
                <v-list-item-subtitle>Select the image of the object or environment where the camouflage will be applied.</v-list-item-subtitle>
            </v-list-item>

            <v-list-item>
                <template v-slot:prepend>
                    <v-icon color="primary">mdi-image-filter-center-focus</v-icon>
                </template>
                <v-list-item-title><strong>Segment the Object:</strong></v-list-item-title>
                <v-list-item-subtitle>YOLOv8 will automatically detect and segment the objects in the image.</v-list-item-subtitle>
            </v-list-item>

            <v-list-item>
                <template v-slot:prepend>
                    <v-icon color="primary">mdi-palette</v-icon>
                </template>
                <v-list-item-title><strong>Apply Camouflage:</strong></v-list-item-title>
                <v-list-item-subtitle>The adaptive camouflage pattern will be applied based on the segmentation results.</v-list-item-subtitle>
            </v-list-item>

            <v-list-item>
                <template v-slot:prepend>
                    <v-icon color="primary">mdi-eye-check</v-icon>
                </template>
                <v-list-item-title><strong>Preview & Download:</strong></v-list-item-title>
                <v-list-item-subtitle>Preview the camouflaged object and download the final result.</v-list-item-subtitle>
            </v-list-item>
        </v-list>

        <p>
            This process uses advanced computer vision techniques to blend objects into their environments, providing
            seamless camouflage.
        </p>

    </div>
</template>