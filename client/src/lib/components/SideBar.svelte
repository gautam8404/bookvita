<script lang="ts">
    import Browse from '$lib/assets/browse.svelte'
    import Library from '$lib/assets/library.svelte';
    import Shelves from '$lib/assets/shelves.svelte';
    import Liked from '$lib/assets/liked.svelte';
    import Social from '$lib/assets/social.svelte';

    import { page } from '$app/stores';

    const sidebarOpts = [
        {
            name: "Browse",
            id: "browse",
            component: Browse,
            path: "/browse"
        },
        {
            name: "Library",
            id: "library",
            component: Library,
            path: "/library"
        },
        {
            name: "Shelves",
            id: "shelves",
            component: Shelves,
            path: "/shelves"
        },
        {
            name: "Liked",
            id: "liked",
            component: Liked,
            path: "/liked"
        },
        {
            name: "Social",
            id: "social",
            component: Social,
            path: "/social"
        }
    ]

    let stroke_color = "#000000";
    let active_stroke_color = "#FE7410"
</script>


<div class="sidebar flex flex-col ml-9 text-2xl mt-9">
    {#each sidebarOpts as item}
        <sidebar class="flex flex-row mt-5">
            <svelte:component this={item.component} path={item.path}/>
            
            <div class="text-component ml-3 -translate-y-1">
                {#if $page.url.pathname == item.path}
                <a href={item.path} class="text-primary relative before:content-[' '] before:absolute before:w-4 before:bg-primary before:h-0.5
                before:-bottom-1 before:-left-8 before:animate-bounce">{item.name}</a>
                {:else}
                <a href={item.path}>{item.name}</a>
                {/if}
            </div>

        </sidebar>
    {/each}

</div>
