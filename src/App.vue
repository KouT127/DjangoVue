<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <v-toolbar-title>
          <v-btn flat>Django & Vue</v-btn>
        </v-toolbar-title>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        flat

        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
      >
        <span class="mr-2">Latest Release</span>
      </v-btn>
    </v-toolbar>

    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  computed: {
  }
}
</script>
