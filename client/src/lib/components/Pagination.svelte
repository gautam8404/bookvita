<script lang="ts">
    import { page } from '$app/stores';

    export let pages: number = 10; // default number of pagination pages
    export let pageSize: number = 42; // default number of items per page

    let pageNum: number |null = 1;

    page.subscribe((p) => {
        let pnumstr = p.url.searchParams.get("page") || "1";
        pageNum = parseInt(pnumstr);
    });

    function changePageUrl(p:any){
        $page.url.searchParams.set("page", p);
        return $page.url.toString();
    }
</script>

<div class="pagination py-6 flex flex-row justify-center items-center">
    {#if pages > 1}
        {#each Array(pages) as _, i}
            {#if i+1 == pageNum}
                <a 
                class="page m-3 bg-primary text-white p-5 items-center justify-center flex w-5 h-5 font-body rounded-full hover:border hover:border-secondary opacity-70" id="page-{i+1}"
                href={changePageUrl(i+1)}
                >{i+1}</a>
            {:else}
                <a 
                class="page p-5 m-3 font-body rounded-full items-center justify-center flex w-5 h-5 hover:border hover:border-black" id="page-{i+1}"
                href={changePageUrl(i+1)}
                >{i+1}</a>
            {/if}

        {/each}
    {/if}
</div>