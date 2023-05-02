<script lang=ts>
	import { stringify } from "postcss";

    export let book: any = {};


    let ol_cover_url = "https://covers.openlibrary.org/b/id/";
    let ol_error_url_lg = "https://openlibrary.org/images/icons/avatar_book-lg.png"
    let ol_error_url_md = "https://openlibrary.org/images/icons/avatar_book.png"
    let ol_error_url_sm = "https://openlibrary.org/images/icons/avatar_book-sm.png"

    let authors = '';
    let imgUrl = ol_error_url_lg;
    $: {
        authors = ''
        imgUrl = ol_error_url_lg
        if (book.authors.length == 0) {
            authors = "Unknown"
        } else {
            for (let i = 0; i < book.authors.length; i++) {
                authors += book.authors[i].name + ", "
            }
        }

        authors = authors.slice(0, -2)

        if (book.cover_id) {
            imgUrl = "https://covers.openlibrary.org/b/id/" + book.cover_id + "-M.jpg";
        }
    }


    function preloadImage(src: string): Promise<string>{
        return new Promise((resolve, reject) => {
            const img = new Image();
            img.src = src;
            img.onload = () => {
                resolve(src);
            };
            img.onerror = () => {
                reject(ol_error_url_lg);
            }
        });
    }

</script>

<div class="">
    <div class="Card flex flex-wrap flex-col m-3 w-52 line-clamp-3 font-body">
        {#await preloadImage(imgUrl)}
        <img class="Card__cover w-52 h-80 aspect-auto border-4 border-secondary bg-secondary animate-ping" src={ol_error_url_lg} alt="Book cover"/>
        {:then src}
        <img class="Card__cover w-52 h-80 aspect-auto border-2 border-secondary bg-secondary" src={src} alt="Book cover"/>
        {:catch error}
        <img class="Card__cover w-52 h-80 aspect-auto border-2 border-secondary bg-secondary" src={error} alt="Book cover"/>

        {/await}
        <div class="Card__title font-body text-lg font-semibold translate-y-2 w-52 line-clamp-3">{book.title}</div>

        <div class="Card__author font-body text-sm translate-y-2 pb-2 pt-1 line-clamp-2">
            {authors}
        </div>
    </div>
</div>

