<script lang="ts">
	import BookCardContainer from './BookCardContainer.svelte';
	export let data: {
		[x: string]: any;
	};
</script>

<div class="search-main">
	<BookCardContainer data={data.results} />
</div>
