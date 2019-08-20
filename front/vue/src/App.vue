<template>
  <div id="app">
    <ogi-header/>
    <router-view/>
  </div>
</template>

<script>
import OgiHeader from '@/components/OgiHeader'
import OgiFooter from '@/components/OgiFooter'

export default {
  name: 'App',
  components: {
    OgiHeader,
    OgiFooter
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
