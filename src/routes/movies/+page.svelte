<script>
	import { onMount } from 'svelte';
	import GenreBadge from './genre_badge.svelte';

	// variables
	let movies_data = [];
	let search_query = '';
	let search_results = [];

	// functions
	async function loadMovieData() {
		const response = await fetch('http://localhost:8000/movies/');
		const json_data = await response.json();

		// save the response object to sessionStorage
		sessionStorage.setItem('movieObjects', JSON.stringify(json_data));

		return json_data;
	}

	const search = async () => {
		try {
			const response = await fetch(`https://api.example.com/search?q=${search_query}`);
			search_results = response.data;
		} catch (error) {
			console.error(error);
		}
	};

	onMount(async () => {
		let stored_movies_data = JSON.parse(sessionStorage.getItem('movieObjects'));

		// if there are movies in sessionStorage
		if (stored_movies_data !== null) {
			movies_data = stored_movies_data;
		} else {
			movies_data = await loadMovieData();
		}
	});
</script>

<div>
	<div class="grid grid-cols-3 gap-2 mb-8">
		<div class="col-span-1 col-start-2 row-start-6 flex items-center justify-center">
			<form class="flex items-center justify-center mt-4">
				<input
					type="text"
					class="w-full p-4 rounded shadow-md"
					placeholder="Search for movie"
					bind:value={search_query}
				/>
				<button
					type="submit"
					class="bg-blue-500 text-white font-semibold mx-4 px-4 py-4 rounded hover:text-white hover:bg-blue-600 hover:border-blue-600 focus:ring focus:ring-blue-400 focus:ring-opacity-50 active:bg-blue-700 active:border-blue-700"
					on:click={search}>Search</button
				>
			</form>
		</div>
	</div>

	<div class="p-6">
		<!-- Cards in Grid: Movies -->
		<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-6 gap-4 lg:gap-8 m-4">
			{#each movies_data as movie}
				<!-- Movie Card -->
				<div class="flex flex-col rounded-lg shadow-sm bg-white overflow-hidden">
					<div class="p-5 lg:p-6 grow w-full text-center">
						<div class="rounded-md -mx-2.5 -mt-2.5 mb-5 overflow-hidden">
							<a
								href={movie.artwork_url}
								target="_blank"
								class="block transition ease-out duration-200 hover:scale-110 active:opacity-50"
							>
								<img src={movie.artwork_url} alt="poster" />
							</a>
						</div>
						<h3 class="text-lg font-semibold mb-1">{movie.title}</h3>
						<h3 class="font-semibold my-3">({movie.release_year})</h3>
						<h3 class="flex items-center my-2 mb-4">
							<span aria-hidden="true" class="grow bg-gray-300 rounded h-0.5" />
						</h3>
						<!-- Create a badge for each genre -->
						{#each movie.genres as genre}
							<a href="/movies/{genre}">
								<GenreBadge {genre} />
							</a>
						{/each}
					</div>
				</div>
				<!-- END Movie Card -->
			{/each}
		</div>
		<!-- END Cards in Grid: Movies -->
	</div>
</div>
