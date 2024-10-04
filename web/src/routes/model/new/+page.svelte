<script lang="ts">
	export let form;
</script>

<form method="POST">
	<h1>Create Model</h1>
	<div>
		<label for="name">Name:</label>
		<input type="text" name="name" />
	</div>

	<div>
		<label for="base">Base Model</label>
		<input type="text" name="base" />
	</div>

	<div>
		<label for="systemPrompt">System Prompt: </label>
		<textarea name="systemPrompt" rows="7" cols="35"></textarea>
	</div>

	<button type="submit">Create</button>
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
