import "@testing-library/jest-dom";
import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/svelte";

import page from "src/routes/movies/+page.svelte";

describe("Test /movies page", () => {
  test("the search input is present", () => {
    render(page);

    // make sure there are 2 dropdown boxes
    expect(screen.getAllByRole("combobox").length).toBe(2);

    // Release Year dropdown
    expect(screen.getByLabelText("Release Year")).toBeInTheDocument();
    expect(
      screen.getByRole("combobox", { name: "Release Year" }),
    ).toBeInTheDocument();

    // Sort movies by dropdown
    expect(screen.getByLabelText("Sort movies by")).toBeInTheDocument();
    expect(
      screen.getByRole("combobox", { name: "Sort movies by" }),
    ).toBeInTheDocument();
    // there should be 4 available options in the `Sort movies by` dropdown
    expect(
      screen.getByRole("combobox", { name: "Sort movies by" }).length,
    ).toBe(4);
    // `Title (Ascending)` should be the default (selected) value for this select box
    expect(
      screen.getByRole("option", { name: "Title (Ascending)" }).selected,
    ).toBe(true);
  });
});
