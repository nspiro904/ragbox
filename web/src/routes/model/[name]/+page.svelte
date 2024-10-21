<script lang="ts">
	import { page } from '$app/stores';
	export let data;

	const name = $page.params.name;
	let { system, details } = data;
</script>

<form method="POST">
	<h1>Manage Model: {name}</h1>
	<div>
		<label for="base">Base Model</label>
		<input type="text" name="base" bind:value={details.parent_model} />
	</div>

	<div>
		<label for="systemPrompt">System Prompt</label>
		<textarea name="systemPrompt" bind:value={system} rows="7" cols="35"></textarea>
	</div>

	<button type="submit">Save</button>
</form>

<style lang="scss">
	form {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		height: 50vh;
		gap: 2em;

		> div {
			display: flex;
			gap: 2em;
			width: 20vw;
			justify-content: space-between;
			> label {
				align-self: center;
			}
		}
	}
</style>
