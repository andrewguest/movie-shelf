<script>
	import { onMount } from 'svelte';
	import GenreBadge from './genre_badge.svelte';

	// variables
	let movies_data = [];

	// functions
	async function loadMovieData() {
		const response = await fetch('http://localhost:8000/movies/');
		const json = await response.json();

		return json;
	}

	onMount(async () => {
		movies_data = await loadMovieData();
	});
</script>

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
						<GenreBadge {genre} />
					{/each}
				</div>
			</div>
			<!-- END Movie Card -->
		{/each}
	</div>
	<!-- END Cards in Grid: Movies -->
</div>
