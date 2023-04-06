<script>
	import { onMount } from 'svelte';

	// functions
	async function loadData() {
		const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
		const json = await response.json();

		return json;
	}

	onMount(async () => {
		dataPromise = await loadData();
	});

	// variables
	let dataPromise = loadData();
</script>

<div class="m-4">
	{#await dataPromise}
		<p>Loading...</p>
	{:then data}
		<ul>
			{#each Object.keys(data) as key}
				<li>{key}: {data[key]}</li>
			{/each}
		</ul>
	{:catch error}
		<p>Error: {error.message}</p>
	{/await}

	<button
		on:click={loadData}
		type="button"
		class="inline-flex justify-center items-center space-x-2 border font-semibold rounded-lg px-4 py-2 leading-6 border-blue-700 bg-blue-700 text-white hover:text-white hover:bg-blue-600 hover:border-blue-600 focus:ring focus:ring-blue-400 focus:ring-opacity-50 active:bg-blue-700 active:border-blue-700 dark:focus:ring-blue-400 dark:focus:ring-opacity-90"
		>Load Data</button
	>
</div>
