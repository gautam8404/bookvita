<script lang="ts">
	import type { PageServerData } from '../../../.svelte-kit/types/src/routes/$types';

	export let data: PageServerData;
	import BookCard from '$lib/components/BookCard.svelte';
</script>

<div class="book-card left-0">
	<pre>{JSON.stringify(data, null, 2)}</pre>
</div>
