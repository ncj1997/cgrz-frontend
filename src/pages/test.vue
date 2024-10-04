<template>
    <v-select v-model="selectedEnvironment" :items="environments" item-title="textenv" :item-props="true"
        label="Select Environment" outlined>
        <!-- Custom rendering of each item -->
        <template #item="{ item, on, props }">
            <v-list-item v-bind="props" v-on="on" :title="item.textenv" :prepend-icon="props.icon">
                <v-list-item-content>
                    <v-list-item-title>{{ props.textenv }}</v-list-item-title>
                    <v-list-item-subtitle>{{ props.description }}</v-list-item-subtitle>
                </v-list-item-content>
            </v-list-item>
        </template>
    </v-select>
</template>

<script>
export default {
    data() {
        return {
            selectedEnvironment: null,
            environments: [
                {
                    textenv: "Desert",
                    value: "desert",
                    description: "Sandy desert environment.",
                    icon: "mdi-weather-sunny",
                },
                {
                    textenv: "Forest",
                    value: "forest",
                    description: "Lush forest environment.",
                    icon: "mdi-tree",
                },
                {
                    textenv: "Snowy",
                    value: "snowy",
                    description: "Icy snowy environment.",
                    icon: "mdi-snowflake",
                },
                {
                    textenv: "Urban",
                    value: "urban",
                    description: "Busy urban environment.",
                    icon: "mdi-city",
                },
            ],
        };
    },
};
</script>