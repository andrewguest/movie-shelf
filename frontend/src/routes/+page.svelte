<!-- Page Container -->
<div
  id="page-container"
  class="flex flex-col mx-auto w-full min-h-screen bg-gray-100"
>
  <div class="grid grid-cols-3 gap-2 mb-8">
    <div class="col-span-1 col-start-2 row-start-6 flex">
      <form class="flex w-full mt-4">
        <input
          type="text"
          class="w-full p-4 rounded shadow-md border-2 border-gray-400 focus:outline-none focus:ring-2"
          placeholder="Search for a movie or TV show"
        />
        <button
          type="submit"
          class="bg-blue-500 text-white font-semibold mx-4 px-4 py-4 rounded hover:text-white hover:bg-blue-600 hover:border-blue-600 focus:ring focus:ring-blue-400 focus:ring-opacity-50 active:bg-blue-700 active:border-blue-700"
          >Search</button
        >
      </form>
    </div>
  </div>
  <!-- Page Content -->
  <main id="page-content" class="flex flex-auto flex-col max-w-full">
    <div class="min-h-screen flex items-center justify-center">
      <div class="w-full max-w-7xl lg:py-16">
        <!-- Box -->
        <div
          class="flex flex-col h-full md:flex-row rounded-xl shadow-sm overflow-hidden"
        >
          <!-- Movies image -->
          <a href="/movies" class="md:w-1/2 block">
            <div
              id="image"
              class="relative px-6 py-10 md:px-10 lg:p-16 md:w-full md:h-full mr-4 bg-opacity-80 flex items-center bg-cover rounded-lg"
              style="background-image: url(/movies_background.jpg);"
            />
            <div class="relative text-center sm:text-center">
              <h2 class="text-2xl font-bold mt-4">Movies</h2>
            </div>
          </a>
          <!-- END Movies image -->

          <!-- TV image -->
          <a href="/tv" class="md:w-1/2 block">
            <div
              id="image"
              class="relative px-6 py-10 md:px-10 lg:p-16 md:w-full md:h-full ml-4 bg-opacity-20 flex items-center bg-cover rounded-lg"
              style="background-image: url(/tv_shows_background.jpg);"
            />
            <div class="relative text-center sm:text-center">
              <h2 class="text-2xl font-bold mt-4">TV Shows</h2>
            </div>
          </a>
          <!-- END TV image -->
        </div>
        <!-- END Box -->
      </div>
    </div>
  </main>
  <!-- END Page Content -->
</div>

<!-- END Page Container -->

<style>
  a #image {
    -webkit-filter: grayscale(100%);
    -moz-filter: grayscale(100%);
    -ms-filter: grayscale(100%);
    height: 50vh;
    filter: grayscale(100%);
    filter: gray;
    position: relative;
    flex: 1;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover; /* IE 6-9 */
  }

  #image:hover {
    -webkit-filter: none;
    -moz-filter: none;
    -ms-filter: none;
    filter: none;
  }
</style>
