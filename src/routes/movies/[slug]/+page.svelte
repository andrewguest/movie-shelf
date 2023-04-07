<script>
	export let data;
	import { onMount } from 'svelte';

	// variables
	let temp_all_movies = []; // temp array for all movies
	let movies_in_genre = []; // list of movies filtered by genre

	// functions
	async function loadMovieData() {
		const response = await fetch('http://localhost:8000/movies/');
		const json_data = await response.json();

		// save the response object to sessionStorage
		sessionStorage.setItem('movieObjects', JSON.stringify(json_data));

		return json_data;
	}

	onMount(async () => {
		let stored_movies_data = JSON.parse(sessionStorage.getItem('movieObjects'));

		// if there are movies in sessionStorage
		if (stored_movies_data !== null) {
			temp_all_movies = stored_movies_data;
		} else {
			temp_all_movies = await loadMovieData();
		}

		// only keep the movies with the current genre
		for (let i = 0; i < temp_all_movies.length; i++) {
			if (temp_all_movies[i].genres.includes(data.genre)) {
				console.log(temp_all_movies[i]);
				movies_in_genre.push(temp_all_movies[i]);
			}
		}
	});
</script>

<!-- Page Heading with Actions and Breadcrumb -->
<div
	class="text-center sm:text-left sm:flex sm:items-center sm:justify-between sm:border-b-2 sm:border-gray-200 mb-4 m-4 lg:mb-8"
>
	<div class="py-3 space-y-1">
		<h2 class="text-2xl font-bold">Movie genre: <u>{data.genre}</u></h2>
	</div>

	<!-- Actions -->
	<div
		class="flex items-center justify-between sm:justify-end space-x-2 py-3 bg-gray-50 rounded sm:bg-transparent px-2 sm:px-0"
	>
		<a
			type="button"
			class="inline-flex justify-center items-center space-x-2 border font-semibold focus:outline-none px-3 py-2 leading-6 rounded border-transparent text-blue-600 hover:text-blue-400 focus:ring focus:ring-blue-500 focus:ring-opacity-50 active:text-blue-600"
			href="/movies"
		>
			<svg
				class="hi-solid hi-arrow-left inline-block w-5 h-5 opacity-75 transform rotate-45"
				fill="currentColor"
				viewBox="0 0 20 20"
				xmlns="http://www.w3.org/2000/svg"
				><path
					fill-rule="evenodd"
					d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z"
					clip-rule="evenodd"
				/></svg
			>
			<span>Go Back</span>
		</a>
	</div>
	<!-- END Actions -->
</div>
<!-- END Page Heading with Actions -->

{#each movies_in_genre as m}
	<p>{m.title}</p>
{/each}

<div class="p-6">
	<!-- Cards in Grid: Movies -->
	<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-6 gap-4 lg:gap-8 m-4">
		{#each movies_in_genre as movie}
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
				</div>
			</div>
			<!-- END Movie Card -->
		{/each}
	</div>
	<!-- END Cards in Grid: Movies -->
</div>
