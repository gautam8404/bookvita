<script lang="ts">
	import type { PageServerData } from './$types';

	import BookInfoPage from '$lib/components/BookInfoPage.svelte';
	export let data: PageServerData;
</script>

<BookInfoPage {data} />
