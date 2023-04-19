/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{html,js,svelte,ts}"],
  theme: {
    extend: {
      colors: {
        "space-blue-100": "#3868AA",
        "space-blue-200": "#224370",
        "space-blue-300": "#1B3559",
        "space-gray": "#F0F0F0",
        "space-yellow": "#F9D949",
        "space-orange": "#F45050",
      },
    },
  },
  plugins: [],
  darkMode: false,
};
