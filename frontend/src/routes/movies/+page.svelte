<script>
  import { onMount } from 'svelte';
  import GenreBadge from './genre_badge.svelte';

  // variables
  let movies_data = []; // list of movies that may be changed
  let untouched_movies_data = []; // original, unchanged, list of movies
  let release_years_list = []; // list of release years from the API
  let selected_release_year = null; // currently selected release year
  let sort_field = 'title_asc'; // current movie property to sort by

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

  async function sortAllMoviesByField(sort_field) {
    if (sort_field !== null) {
      if (sort_field === 'title_asc') {
        movies_data = movies_data.sort((a, b) => (a.title > b.title ? 1 : -1));
      } else if (sort_field === 'title_desc') {
        movies_data = movies_data.sort((a, b) => (a.title < b.title ? 1 : -1));
      } else if (sort_field === 'release_year_asc') {
        movies_data = movies_data.sort((a, b) =>
          a.release_year > b.release_year ? 1 : -1
        );
      } else if (sort_field === 'release_year_desc') {
        movies_data = movies_data.sort((a, b) =>
          a.release_year < b.release_year ? 1 : -1
        );
      }
    }

    return movies_data;
  }

  // lifecycle hooks
  onMount(async () => {
    movies_data = await loadMovieData();
    movies_data = await sortAllMoviesByField(sort_field);
    untouched_movies_data = movies_data;
    release_years_list = await getAllReleaseYears();
  });
</script>

<div>
  <div class="p-6">
    <!-- START sort and filter button grid -->
    <div id="sort-and-filter-grid" class="grid grid-cols-8 gap-6">
      <!-- START "Release Year" filter select box -->
      <form onsubmit="return false;" class="space-y-6 mb-10">
        <div class="space-y-1">
          <label class="font-medium" for="release_year_select"
            >Release Year</label
          >
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
      <!-- END "Release Year" filter select box -->
      <!-- START "Sort by" select box -->
      <form onsubmit="return false;" class="space-y-6 mb-10">
        <div class="space-y-1">
          <label class="font-medium" for="sort_by_select">Sort movies by</label>
          <select
            class="w-full block border bg-white border-gray-200 rounded px-3 py-2 focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
            id="sort_by_select"
            name="sort_by_select"
            bind:value={sort_field}
            on:change={sortAllMoviesByField(sort_field)}
          >
            <option value="title_asc">Title (Ascending)</option>
            <option value="title_desc">Title (Descending)</option>
            <option value="release_year_asc">Release Year (Ascending)</option>
            <option value="release_year_desc">Release Year (Descending)</option>
          </select>
        </div>
      </form>
      <!-- END "Sort by" select box -->
      <!-- START download button -->
      <div class="col-end-8 flex justify-center">
        <a class="" href="/movie_import_template.csv" download>
          <button
            type="buttton"
            class="h-1/2 my-2 px-2 text-space-blue-100 bg-transparent ring-2 ring-space-blue-100 font-semibold rounded hover:ring-4 hover:ring-space-blue-200 focus:ring-2 focus:ring-space-blue-200 focus:ring-opacity-50 active:border-space-blue-300"
            ><svg
              class="bi bi-download inline-block w-5 h-5 mr-4"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 16 16"
              aria-hidden="true"
              ><path
                d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z"
              /><path
                d="M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3z"
              /></svg
            >CSV template</button
          >
        </a>
      </div>
      <!-- END download button -->
      <!-- START import button -->
      <button
        type="submit"
        class="col-end-9 h-1/2 my-2 bg-space-blue-100 text-white font-semibold rounded hover:text-white hover:bg-space-blue-200 hover:border-space-blue-200 focus:ring focus:ring-blue-400 focus:ring-opacity-50 active:bg-space-blue-300 active:border-space-blue-300"
        ><svg
          class="bi bi-upload inline-block w-5 h-5 mr-4"
          xmlns="http://www.w3.org/2000/svg"
          fill="currentColor"
          viewBox="0 0 16 16"
          aria-hidden="true"
          ><path
            d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z"
          /><path
            d="M7.646 1.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 2.707V11.5a.5.5 0 0 1-1 0V2.707L5.354 4.854a.5.5 0 1 1-.708-.708l3-3z"
          /></svg
        >Import from CSV</button
      >
      <!-- END import button -->
    </div>
    <!-- END sort and filter button grid -->

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
