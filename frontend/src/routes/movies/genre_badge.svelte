<script>
    export let genre;

    // assign specific text and background colors to each genre so that the badges are different colors
    const genre_lookup = {
        adventure: "text-emerald-700 bg-emerald-200",
        fantasy: "text-teal-700 bg-teal-200",
        animation: "text-blue-700 bg-blue-200",
        drama: "text-purple-700 bg-purple-200",
        horror: "text-pink-700 bg-pink-200",
        action: "text-teal-700 bg-teal-200",
        comedy: "text-red-700 bg-red-200",
        history: "text-orange-700 bg-orange-200",
        western: "text-blue-700 bg-blue-200",
        thriller: "text-emerald-700 bg-emerald-200",
        crime: "text-indigo-700 bg-indigo-200",
        documentary: "text-purple-700 bg-purple-200",
        "science fiction": "text-pink-700 bg-pink-200",
        mystery: "text-rose-700 bg-rose-200",
        music: "text-orange-700 bg-orange-200",
        romance: "text-purple-700 bg-purple-200",
        family: "text-orange-700 bg-orange-200",
        war: "text-orange-700 bg-orange-200",
        "tv movie": "text-emerald-700 bg-emerald-200",
    };

    let badge_color = genre_lookup[genre];
</script>

<h4
    class={`font-semibold inline-flex px-2 py-1 mx-1 my-1 leading-4 text-sm rounded-md ${badge_color}`}
>
    {genre}
</h4>
