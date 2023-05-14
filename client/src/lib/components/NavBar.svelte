<script lang="ts">
	// import InstantSearch from "./InstantSearch.svelte";
	import SearchBar from './SearchBar.svelte';
</script>

<div>
	<nav class="flex items-center justify-between flex-wrap mt-9">
		<div class="logo flex-shrink">
			<h1 class="text-3xl font-body ml-9 mt-1">
				book<span class="text-primary font-black font-body">V</span>ita
			</h1>
		</div>

		<SearchBar />

		<div
			class="pfp flex justify-end items-end mr-10 flex-shrink border border-black dark:border-white"
		>
			<input
				type="image"
				src={'https://i.imgur.com/2d4kZ9h.png'}
				alt="profile picture"
				class="rounded-full w-14 h-14"
			/>
		</div>
	</nav>
</div>
