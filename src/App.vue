<template>
  <HomePage />
</template>

<script>
import HomePage from './components/Home.vue';

export default {
  name: 'App',
  components: {
    HomePage,
  }
}
</script>

<style>
*{
    margin: 0px;
    padding: 0px;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center;
  color: #2c3e50;
  margin-top: 60px; */
}
</style>
