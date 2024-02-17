<script>
  import { onMount } from "svelte";
  let learningResources;
  onMount(async () => {
    const response = await fetch("http://127.0.0.1:5000", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const data = await response.json();

    if (response.ok) {
      learningResources = data;
    } else {
      throw new Error("Error fetching data");
    }
  });
</script>

{#if learningResources}
  {#each Object.keys(learningResources) as category}
    <h1>{category}</h1>
    {#each learningResources[category] as resource}
      <a href={resource.link}><h3>{resource.title}</h3></a>
      <p>by {resource.author}</p>
      <img src={resource.image_url} alt="" />
    {/each}
  {/each}
{:else}
  <p>Error. Please try again.</p>
{/if}
