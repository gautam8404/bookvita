<script lang="ts">
	import { fly, fade } from  'svelte/transition';

	export let book: any = {};
	export let cover_size = 'M';

	let ol_cover_url = 'https://covers.openlibrary.org/b/id/';
	let ol_error_url_lg = 'https://openlibrary.org/images/icons/avatar_book-lg.png';
	let ol_error_url_md = 'https://openlibrary.org/images/icons/avatar_book.png';
	let ol_error_url_sm = 'https://openlibrary.org/images/icons/avatar_book-sm.png';

	let authors = '';
	let imgUrl = ol_error_url_lg;
	$: {
		authors = '';
		imgUrl = ol_error_url_lg;
		if (book.authors.length == 0) {
			authors = 'Unknown';
		} else {
			for (let i = 0; i < book.authors.length; i++) {
				authors +=
					"<a class='author_anchor' href='/author/" +
					book.authors[i].author_id +
					"'>" +
					book.authors[i].name +
					'</a> ,';
			}
		}

		authors = authors.slice(0, -2);

		if (book.cover_id) {
			imgUrl = 'https://covers.openlibrary.org/b/id/' + book.cover_id + '-' + cover_size + '.jpg';
		}
	}

	function preloadImage(src: string): Promise<string> {
		return new Promise((resolve, reject) => {
			const img = new Image();
			img.src = src;
			img.onload = () => {
				resolve(src);
			};
			img.onerror = () => {
				reject(ol_error_url_md);
			};
		});
	}
</script>
<!--{#key book.book_id}-->
<div class="" > <!---in:fly={{y:200, duration:2000}} --->
	<div class="Card flex flex-wrap flex-col m-3 w-52 line-clamp-3 font-body">
		<a href="/book/{book.book_id}">
			{#await preloadImage(imgUrl)}
				<img
					class="Card__cover w-52 h-80 aspect-auto border-1 border-secondary bg-secondary animate-pulse"
					src={ol_error_url_md}
					alt="Book cover"
					rel="preload"
				/>
			{:then src}
				<img
					class="Card__cover w-52 h-80 aspect-auto border-2 border-secondary bg-secondary hover:border-primary"
					{src}
					alt="Book cover"
					rel="preload"
				/>
			{:catch error}
				<img
					class="Card__cover w-52 h-80 aspect-auto border-2 border-secondary bg-secondary hover:border-primary"
					src={error}
					alt="Book cover"
					rel="preload"
				/>
			{/await}
			<div
				class="Card__title font-body text-lg font-semibold translate-y-2 w-52 line-clamp-3 hover:text-primary"
			>
				{book.title}
			</div>
		</a>

		<div class="Card__author font-body text-sm translate-y-2 pb-2 pt-1 line-clamp-2">
			{@html authors}
		</div>
	</div>
</div>
<!--{/key}-->

<style lang="postcss">
	:global(:hover.author_anchor) {
		color: theme(colors.primary);
	}
</style>
