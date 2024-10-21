<script lang="ts">
	export let data;

	console.log(data);

	let search: string = '';

	// async function submit() {
	// try {
	// const response = await fetch("")
	// }
	// }
</script>

<h1>Search for model</h1>

<form on:submit|preventDefault={submit}>
	<input type="text" bind:value={search} />
	<button>Search</button>
</form>

<style lang="scss">
	form {
		display: flex;
		justify-content: center;
	}
</style>
