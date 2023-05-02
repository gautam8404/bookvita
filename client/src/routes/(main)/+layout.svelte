<script lang="ts">
    import NavBar from '$lib/components/NavBar.svelte';
    import SideBar from '$lib/components/SideBar.svelte';
    import Pagination from '$lib/components/Pagination.svelte';
	import type { LayoutServerData } from './$types';

    let content: string;
    let form: HTMLFormElement;

    export let data: LayoutServerData;
</script>


<div class="wrapper">
    <div class="navbar">
        <NavBar data={data}/>
    </div>

    <div class="flex mt-3 h-5/6">
        <div class="sidebar w-3/4">
            <SideBar />
        </div>
    
        <div class="content mt-14 h-screen">
            <slot></slot>
        </div>
    </div>
</div>




