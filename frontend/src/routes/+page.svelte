<script>
    import { onMount } from "svelte";
    import { PUBLIC_DEV_URL, PUBLIC_K8S_SERVICE_URL } from "$env/static/public";

    let learningResources;
    onMount(async () => {
        const response = await fetch(PUBLIC_K8S_SERVICE_URL || PUBLIC_DEV_URL, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        });

        console.log("public dev url-", PUBLIC_DEV_URL);
        console.log("k8s service url-", PUBLIC_K8S_SERVICE_URL);

        const data = await response.json();

        if (response.ok) {
            learningResources = data;
        } else {
            throw new Error(
                "Error fetching data from the backend service. Please try again.",
            );
        }
    });
</script>

<h1>Go Deeper with Kubernetes</h1>
{#if learningResources}
    {#each Object.keys(learningResources) as category}
        <h2>{category}</h2>
        {#each learningResources[category] as resource}
            <a href={resource.link}><h3>{resource.title}</h3></a>
            <p>by {resource.author}</p>
            <img src={resource.image_url} alt="" />
        {/each}
    {/each}
{:else}
    <p>Oops, something went wrong. Please try again.</p>
{/if}

<style>
    @import "./styles.css";
</style>
