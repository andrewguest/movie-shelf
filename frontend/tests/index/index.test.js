import "@testing-library/jest-dom";
import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/svelte";

import page from "src/routes/+page.svelte";

describe("Test index page", () => {
  test("the search input is present", () => {
    render(page);

    // expect the search input box to be in the document
    expect(
      screen.getByPlaceholderText("Search for a movie or TV show"),
    ).toBeInTheDocument();
    // expect the "Search" button to be in the document
    expect(screen.getByText("Search")).toBeInTheDocument();
  });

  // tests for the images that act as links and their titles on the index page
  test("the media sections are present", () => {
    render(page);

    // expect the `Movies` heading to be present
    expect(screen.getByText("Movies")).toBeInTheDocument();
    // expect the `TV Shows` heading to be present
    expect(screen.getByText("TV Shows")).toBeInTheDocument();
  });
});
