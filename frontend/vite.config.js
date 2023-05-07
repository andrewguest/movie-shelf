import { sveltekit } from "@sveltejs/kit/vite";
import { defineConfig } from "vitest/config";

export default defineConfig({
  plugins: [
    sveltekit({
      hot: !process.env.VITEST,
    }),
  ],
  test: {
    environment: "jsdom",
    globals: true,
    include: [
      "src/**/*.{test,spec}.{js,ts}",
      "tests/unit/**/*.test.js",
      "tests/unit/**/*.tests.js",
      "tests/unit/**/test*.js",
    ],
  },
});
