<!-- <template>
  <v-app>
    <v-main>
      <router-view />
    </v-main>

    <AppFooter />
  </v-app>
</template>

<script setup>
  //
</script> -->
<template>
  <!-- Use v-app as the root container -->
  <v-app>
    <!-- App Bar -->
    <v-app-bar color="white" density="compact" >
      <!-- <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon> -->

      <v-toolbar-title> Adaptive Camouflage Pattern Generator</v-toolbar-title>

      <v-spacer></v-spacer>
    </v-app-bar>

    <!-- Navigation Drawer -->
    <v-navigation-drawer
        expand-on-hover
        rail
      >
        <!-- User Info -->
        <v-list>
          <v-list-item
            prepend-avatar="https://randomuser.me/api/portraits/lego/7.jpg" 
            subtitle="team@intelilab.click"
            title="Team Intelilabs"
          ></v-list-item>
        </v-list>

        <v-divider></v-divider>

        <!-- Navigation List -->
        <v-list density="compact" nav>
          <!-- Camouflage Generator -->
          <v-list-item
            prepend-icon="mdi-home"
            title="Camouflage Generator"
            value="generator"
            to="/"
            exact
          ></v-list-item>
          
          <!-- Apply Camouflage -->
          <v-list-item
            prepend-icon="mdi-brush"
            title="Apply Camouflage"
            value="apply"
            to="/apply-pattern"
            exact
          ></v-list-item>
        </v-list>
      </v-navigation-drawer>

    <!-- Main Content Area -->
    <v-main >
      <v-container fluid class="pa-2" >
        <router-view />
      </v-container>
    </v-main>

    <!-- Footer -->
    <AppFooter />
  </v-app>
</template>
<script>
export default {
  data: () => ({
    drawer: false,
    group: null,
    items: [
      {
        title: 'Pattern Generator',
        value: 'foo',
      },
      {
        title: 'Apply to Objects',
        value: 'bar',
      },
    ],
  }),

  watch: {
    group() {
      this.drawer = false
    },
  },
}
</script>

<style>

</style>