<script lang="ts">
    export let data: object[];
    import InstantSearchCard from "./InstantSearchCard.svelte";
    console.log(data);
</script>


<div class="ins flex flex-col max-h-72 overflow-y-auto z-20 relative w-full bg-white border rounded-xl overflow-x-hidden shadow-black shadow-lg" id="insCard">
    {#each data as item}
        <InstantSearchCard data={item}/>
    {/each}
</div>