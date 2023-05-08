<script lang="ts">
	import type { PageData } from './$types';
	import SearchComponent from '$lib/components/SearchComponent.svelte';

	export let data: PageData;
</script>

<div class="searchComp">
	<SearchComponent {data} />
</div>
