<script>
  import { onMount } from "svelte";
  let books;
  onMount(async () => {
    const response = await fetch("http://127.0.0.1:5000", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const data = await response.json();

    if (response.ok) {
      books = data;
    } else {
      throw new Error("Error fetching data");
    }
  });
</script>

{#if books}
  <main>
    <ul>
      {#each books as book}
        <h2>{book.title}</h2>
        <p>{book.author}</p>
      {/each}
    </ul>
  </main>
{/if}
