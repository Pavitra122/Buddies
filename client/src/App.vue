<template>
	<div id="app">
		<img src="./assets/logo.png">
		<HelloWorld/>
	</div>
</template>

<script>
import Main from "./components/Main.vue";
import Second from "./components/Second.vue";

export default {
	name: 'App',
	components: {
		
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
