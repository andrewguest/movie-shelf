<script>
  import { onMount } from 'svelte';
  import GenreBadge from './genre_badge.svelte';

  // variables
  let movies_data = []; // list of movies that may be changed
  let untouched_movies_data = []; // original, unchanged, list of movies
  let release_years_list = []; // list of release years from the API
  let selected_release_year = null; // currently selected release year

  // get all movies from the API
  async function loadMovieData() {
    const response = await fetch('/api/movies');
    const json_data = await response.json();

    return json_data;
  }

  // get the list of `Release Years` from the API to populate the select box
  async function getAllReleaseYears() {
    const response = await fetch('/api/movies/release_years');
    const json_data = await response.json();

    return json_data;
  }

  // if the `Release Year` select box is used, then filter the `movies_data` array to
  //  only show the movies from that year
  async function filterAllMoviesByReleaseYear(filter_year) {
    movies_data = untouched_movies_data;

    if (filter_year === null || filter_year == '') {
      return movies_data;
    } else {
      movies_data = movies_data.filter((movie_object) => {
        return movie_object.release_year == filter_year;
      });
    }
  }

  // lifecycle hooks
  onMount(async () => {
    movies_data = await loadMovieData();
    untouched_movies_data = movies_data;
    release_years_list = await getAllReleaseYears();
  });
</script>

<div>
  <div class="p-6">
    <!-- Start sort and filter button grid -->
    <div id="sort-and-filter-grid" class="grid grid-cols-8 gap-4">
      <!-- Start "Release Year" filter select box -->
      <form onsubmit="return false;" class="space-y-6 mb-10">
        <div class="space-y-1">
          <label class="font-medium" for="select">Release Year</label>
          <select
            class="w-full block border bg-white border-gray-200 rounded px-3 py-2 focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
            id="release_year_select"
            name="release_year_select"
            bind:value={selected_release_year}
            on:change={filterAllMoviesByReleaseYear(selected_release_year)}
          >
            <option />
            {#each release_years_list as year}
              <option>{year}</option>
            {/each}
          </select>
        </div>
      </form>
      <!-- End "Release Year" filter select box -->
    </div>
    <!-- End sort and filter button grid -->

    <!-- Cards in Grid: Movies -->
    <div
      class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols:4 lg:grid-cols-6 gap-4 lg:gap-8 m-4"
    >
      {#each movies_data as movie}
        <!-- Movie Card -->
        <div
          class="flex flex-col rounded-lg shadow-sm bg-white overflow-hidden"
        >
          <div class="p-5 lg:p-6 grow w-full text-center">
            <div class="rounded-md -mx-2.5 -mt-2.5 mb-5 overflow-hidden">
              <a
                href={movie.poster_url}
                target="_blank"
                class="block transition ease-out duration-200 hover:scale-110 active:opacity-50"
              >
                <img src={movie.poster_url} alt="poster" />
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
