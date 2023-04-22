<script>
  import { onMount } from 'svelte';
  import GenreBadge from './genre_badge.svelte';

  // variables
  let movies_data = []; // list of movies that may be changed
  let untouched_movies_data = []; // original, unchanged, list of movies
  let release_years_list = []; // list of release years from the API
  let selected_release_year = null; // currently selected release year
  let sort_field = 'title_asc'; // current movie property to sort by
  let show_settings_modal = false; // should the settings modal be displayed
  let imported_csv_file; // the uploaded CSV file to be imported

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

  // toggle the settings modal
  async function toggleSettingsModal() {
    show_settings_modal = !show_settings_modal;
  }

  // import movies from CSV
  async function uploadFile() {
    imported_csv_file = event.target.files[0];
    const formData = new FormData();
    formData.append('file', imported_csv_file);

    const response = await fetch('/api/admin/import', {
      method: 'POST',
      body: formData,
    });

    if (response.ok) {
      console.log('File uploaded successfully');
      show_settings_modal = false;
    } else {
      console.error('File upload failed');
    }
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
    <div id="sort-and-filter-grid" class="grid grid-cols-auto min-w-0 gap-4">
      <!-- START "Release Year" filter select box -->
      <form onsubmit="return false;" class="space-y-6 mb-10 w-full">
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
      <!-- START "Sort by" select box -->
      <form onsubmit="return false;" class="space-y-6 mb-10 w-full">
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
      <!-- START settings modal button -->
      <button
        class="col-end-9 h-1/2 my-2 font-semibold rounded bg-space-blue-200 text-white hover:text-white hover:bg-space-blue-300 hover:border-space-blue-300 hover:ring-4 hover:ring-blue-400 hover:ring-opacity-75 active:bg-space-blue-300 active:border-space-blue-300"
        on:click={toggleSettingsModal}
      >
        <span>Settings</span>
        <svg
          class="bi bi-gear-fill inline-block w-5 h-5 ml-2"
          xmlns="http://www.w3.org/2000/svg"
          fill="currentColor"
          viewBox="0 0 16 16"
          aria-hidden="true"
          ><path
            d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"
          /></svg
        >
      </button>
      <!-- START settings modal -->
      {#if show_settings_modal}
        <div
          class="z-90 fixed inset-0 overflow-y-auto overflow-x-hidden bg-gray-900 bg-opacity-75 p-4 lg:p-8"
          tabindex="-1"
          role="dialog"
          aria-labelledby="tk-modal-with-form"
          aria-hidden="false"
        >
          <div
            class="flex flex-col rounded shadow-sm bg-white overflow-hidden w-full max-w-lg mx-auto"
            role="document"
          >
            <div
              class="py-4 px-5 lg:px-6 w-full bg-gray-50 flex justify-between items-center"
            >
              <h3 class="font-medium flex items-center space-x-2">
                <svg
                  class="bi bi-gear-fill inline-block w-5 h-5"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="currentColor"
                  viewBox="0 0 16 16"
                  aria-hidden="true"
                  ><path
                    d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"
                  /></svg
                >
                <span>Settings</span>
              </h3>
              <div class="-my-4">
                <button
                  type="button"
                  class="inline-flex justify-center items-center space-x-2 border font-semibold focus:outline-none px-2 py-1 leading-5 text-sm rounded border-transparent text-gray-600 hover:text-gray-400 focus:ring focus:ring-gray-500 focus:ring-opacity-25 active:text-gray-600"
                  on:click={toggleSettingsModal}
                >
                  <svg
                    class="hi-solid hi-x inline-block w-4 h-4 -mx-1"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg"
                    ><path
                      fill-rule="evenodd"
                      d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                      clip-rule="evenodd"
                    /></svg
                  >
                </button>
              </div>
            </div>
            <!-- Download CSV template-->
            <div
              class="p-5 lg:p-6 grow w-full flex items-center justify-center"
            >
              <a class="w-3/5" href="/movie_import_template.csv" download>
                <button
                  type="button"
                  class="inline-flex w-full items-center justify-center space-x-2 border font-semibold rounded-lg px-6 py-3 leading-6 border-blue-700 bg-blue-700 text-white hover:text-white hover:bg-blue-600 hover:border-blue-600 focus:ring focus:ring-blue-400 focus:ring-opacity-50 active:bg-blue-700 active:border-blue-700 dark:focus:ring-blue-400 dark:focus:ring-opacity-90 appearance-none"
                >
                  <svg
                    class="hi-mini hi-arrow-down-tray inline-block w-5 h-5 opacity-50 text-white"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                    aria-hidden="true"
                    ><path
                      d="M10.75 2.75a.75.75 0 00-1.5 0v8.614L6.295 8.235a.75.75 0 10-1.09 1.03l4.25 4.5a.75.75 0 001.09 0l4.25-4.5a.75.75 0 00-1.09-1.03l-2.955 3.129V2.75z"
                    /><path
                      d="M3.5 12.75a.75.75 0 00-1.5 0v2.5A2.75 2.75 0 004.75 18h10.5A2.75 2.75 0 0018 15.25v-2.5a.75.75 0 00-1.5 0v2.5c0 .69-.56 1.25-1.25 1.25H4.75c-.69 0-1.25-.56-1.25-1.25v-2.5z"
                    /></svg
                  >
                  <span>Download CSV template</span>
                </button>
              </a>
            </div>
            <!-- Import CSV button -->
            <div
              class="p-5 lg:p-6 grow w-full flex items-center justify-center"
            >
              <label
                for="file-upload"
                class="inline-flex w-3/5 items-center justify-center space-x-2 border font-semibold rounded-lg px-6 py-3 leading-6 border-blue-200 bg-blue-100 text-blue-800 hover:border-blue-300 hover:text-blue-900 hover:shadow-sm focus:ring focus:ring-blue-300 focus:ring-opacity-25 active:border-blue-200 active:shadow-none dark:border-blue-200 dark:bg-blue-200 dark:hover:border-blue-300 dark:hover:bg-blue-300 dark:focus:ring-blue-500 dark:focus:ring-opacity-50 dark:active:border-blue-200 dark:active:bg-blue-200"
              >
                <svg
                  class="bi bi-upload inline-block w-5 h-5 mr-2"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="currentColor"
                  viewBox="0 0 16 16"
                  aria-hidden="true"
                  ><path
                    d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z"
                  /><path
                    d="M7.646 1.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 2.707V11.5a.5.5 0 0 1-1 0V2.707L5.354 4.854a.5.5 0 1 1-.708-.708l3-3z"
                  /></svg
                >
                Import CSV file
              </label>

              <input
                id="file-upload"
                type="file"
                class="hidden"
                on:change={uploadFile}
              />
            </div>
            <div
              class="py-4 px-5 lg:px-6 w-full bg-gray-50 text-right space-x-1"
            >
              <button
                type="button"
                class="inline-flex justify-center items-center space-x-2 border font-semibold focus:outline-none px-3 py-2 leading-5 text-sm rounded border-transparent text-red-600 hover:text-red-400 focus:ring focus:ring-red-500 focus:ring-opacity-50 active:text-red-600"
                on:click={toggleSettingsModal}
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      {/if}

      <!-- END settings modal -->
    </div>

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
            <h3 class="text-lg font-semibold mb-1">
              {movie.title}
            </h3>
            <h3 class="font-semibold my-3">
              ({movie.release_year})
            </h3>
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
  </div>
</div>
