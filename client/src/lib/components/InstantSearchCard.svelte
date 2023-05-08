<script lang="ts">
	export let data: {
		[x: string]: any;
	};

	let ol_cover_url = 'https://covers.openlibrary.org/b/id/';
	let ol_error_url_lg = 'https://openlibrary.org/images/icons/avatar_book-lg.png';
	let ol_error_url_md = 'https://openlibrary.org/images/icons/avatar_book.png';
	let ol_error_url_sm = 'https://openlibrary.org/images/icons/avatar_book-sm.png';

	let authors = '';
	let date = '';

	$: {
		authors = '';
		date = '';

		if (data.authors.length == 0) {
			authors = 'Unknown';
		} else {
			for (let i = 0; i < data.authors.length; i++) {
				authors += data.authors[i].name + ', ';
			}
		}

		if (data.publish_date == undefined) {
			date = '';
		} else {
			date = '(' + data.publish_date + ')';
		}
		authors = authors.slice(0, -2);
	}
</script>

<a
	class="ins-card relative items-center inline-flex flex-row flex-wrap justify-start p-2 border-y
	hover:bg-secondary hover:shadow-lg hover:cursor-pointer"
	id="insCard"
	href="/book/{data.book_id}"
>
	<div class="ins-card__cover">
		{#if data.cover_id}
			<img
				class="ins-card__cover-img w-16 h-20 aspect-auto"
				src="{ol_cover_url}{data.cover_id}-M.jpg"
				alt="book cover"
			/>
		{:else}
			<img
				class="ins-card__cover-img w-16 h-20 aspect-auto"
				src={ol_error_url_sm}
				alt="book cover"
			/>
		{/if}
	</div>
	<div class="text-info break-words max-w-lg font-body">
		<div class="ins-card__title font-body text-lg font-medium pl-2 max-w-lg line-clamp-2">
			{data.title}
		</div>

		<div class="ins-card__author font-body text-sm pl-2">
			{authors}
		</div>
	</div>
	<div class="date">
		<div class="ins-card__date font-body text-sm pl-2 -translate-y-2 line-clamp-1">
			{date}
		</div>
	</div>
</a>
