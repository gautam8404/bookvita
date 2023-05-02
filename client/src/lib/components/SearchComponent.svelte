<script lang="ts">
    import BookMain from "./BookMain.svelte";
    export let data: {
    [x: string]: any;
    };
</script>

<div class="search-main">
    <BookMain data={data.results} />
</div>
