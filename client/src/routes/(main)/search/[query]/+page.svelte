<script lang="ts">
    import type { PageData } from './$types';
    import SearchComponent from '$lib/components/SearchComponent.svelte';
    
    export let data: PageData;
</script>

<SearchComponent data={data} />