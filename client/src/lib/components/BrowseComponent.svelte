<script lang="ts">
	import BookCardContainer from './BookCardContainer.svelte';

	export let data: {
		[x: string]: any;
	};

	let form: HTMLFormElement;

	let opts = [
		{ id: 'trending', text: 'Trending' },
		{ id: 'love', text: 'Love' },
		{ id: 'romance', text: 'Romance' },
		{ id: 'mystery', text: 'Mystery' },
		{ id: 'thriller', text: 'Thriller' },
		{ id: 'fantasy', text: 'Fantasy' },
		{ id: 'science-fiction', text: 'Science Fiction' },
		{ id: 'horror', text: 'Horror' },
		{ id: 'humor', text: 'Humor' },
		{ id: 'fiction', text: 'Fiction' },
		{ id: 'non-fiction', text: 'Non Fiction' },
		{ id: 'biography', text: 'Biography' },
		{ id: 'history', text: 'History' },
		{ id: 'juvenile_fiction', text: 'Kids Book' },
		{ id: 'plays', text: 'Plays' },
		{ id: 'poetry', text: 'Poetry' },
		{ id: 'psychology', text: 'Psychology' },
		{ id: 'religion', text: 'Religion' },
		{ id: 'science', text: 'Science' },
		{ id: 'travel', text: 'Travel' },
		{ id: 'literature', text: 'Literature' }
	];

	let trending_opts = [
		{ id: 'now', text: 'Now' },
		{ id: 'daily', text: 'Daily' },
		{ id: 'weekly', text: 'Weekly' },
		{ id: 'monthly', text: 'Monthly' },
		{ id: 'yearly', text: 'Yearly' },
		{ id: 'all', text: 'All Time' }
	];

	let selected = opts[0].id;
	let trending_selected = trending_opts[0].id;

	const requestSubmit = () => {
		form.requestSubmit();
	};
</script>

<div class="main">
	<div class="dropdowns col-span-full pb-3">
		<form bind:this={form}>
			<select
				bind:value={selected}
				on:change={requestSubmit}
				name="subject"
				class="rounded-2xl px-3 border border-secondary mx-2 bg-white py-1.5"
			>
				{#each opts as opt}
					<option value={opt.id}>{opt.text}</option>
				{/each}
			</select>

			{#if selected == 'trending'}
				<select
					bind:value={trending_selected}
					on:change={requestSubmit}
					name="sortby"
					class="rounded-2xl py-1.5 px-3 border border-secondary mx-2 bg-white"
				>
					{#each trending_opts as opt}
						<option value={opt.id}>{opt.text}</option>
					{/each}
				</select>
			{/if}
		</form>
	</div>

	<div class=" h-screen">
		<BookCardContainer data={data.results} />
	</div>
</div>
