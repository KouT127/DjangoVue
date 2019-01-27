<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <v-toolbar-title >Django&Vue</v-toolbar-title>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        flat

        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
      >
        <span>{{ users }}</span>
        <span class="mr-2">Latest Release</span>
      </v-btn>
    </v-toolbar>

    <v-content>
      <HelloWorld/>
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld'

export default {
  name: 'App',
  created() {
    this.getUsers()
  },
  components: {
    HelloWorld
  },
  computed: {
    users() {
      return this.$store.getters.users
    }
  },
  methods: {
    getUsers(){
      this.$store.dispatch('getUsersAction')
    }
  }
}
</script>
