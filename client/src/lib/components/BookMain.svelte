<script lang=ts>
    import BookCard from '$lib/components/BookCard.svelte';
    import Pagination from './Pagination.svelte';
    export let data: Object[];
</script>


<div class="flex flex-wrap flex-row cardWrap ">
    {#if data && data.length > 0}
        {#each data as book}
            <BookCard book={book}/>
        {/each}
    {/if}
</div>

<div class="pagination">
    <Pagination />
</div>
