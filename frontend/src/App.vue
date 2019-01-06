<template>
  <div>
    <Breadcrumb>
      <BreadcrumbItem to="/HelloWorld">Home</BreadcrumbItem>
      <BreadcrumbItem to="/AddEvaluationTitle">AddEvaluationTitle</BreadcrumbItem>
      <BreadcrumbItem to="/AddDimensions">AddDimensions</BreadcrumbItem>
      <BreadcrumbItem to="/CreateEvaluation">CreateEvaluation</BreadcrumbItem>
    </Breadcrumb>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
  methods: {
    gotest () {
      this.$router.push('/')
    }
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
  margin-top: 60px;
}
</style>
