<script lang=ts>
    import BrowseComponent from "$lib/components/BrowseComponent.svelte";
    export let data;
</script>

<div class="browse">
    <BrowseComponent data={data}/>
</div>