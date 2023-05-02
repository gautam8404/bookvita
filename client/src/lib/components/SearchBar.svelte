<script lang="ts">
    import { goto } from "$app/navigation";

    import InstantSearch from "./InstantSearch.svelte";

    export let data: any;

    let form: HTMLFormElement;


    let timer: number;
    let text: string;   

    const debounce = (func: Function, delay: number) => {
        clearTimeout(timer);
        timer = setTimeout(func, delay);
    }
    
    const requestSubmit = () => form.requestSubmit();
    function debounceSubmit() {
        debounce(requestSubmit, 500);
    }
    const submit = () => {
        clearInterval(timer);
        let value = text.replace(/\s/g, "+");
        goto(`/search/${value}`);
    }

    let insBox : HTMLDivElement;
    let searchBox: HTMLInputElement;
    let instantSearchVisible = false;


    function clickOutside(event: any) {
        if (!insBox.contains(event.target) && !searchBox.contains(event.target)) {
            instantSearchVisible = false;
        } else {
            instantSearchVisible = true;
        }
    }
</script>

<svelte:window on:mousedown={clickOutside}/>

<div class="search flex- items-center justify-center flex" bind:this={insBox}>
    <form bind:this={form} class="w-2/5 h-8 flex-grow items-center justify-center flex" data-sveltekit-keepfocus action="?/browse">
        <input type="text" placeholder="Search by title or author" class="border-2 border-gray-300 rounded-2xl p-2 w-2/5 h-8
        placeholder-secondary focus:outline-none absolute z-10" bind:value={text} on:input={debounceSubmit} name="q"
        on:keydown={
            (e) => {
                if (e.key == "Enter") {
                    e.preventDefault();
                    submit();
                }
            }
        } bind:this={searchBox}>
        <div class="ins-box flex-grow items-center justify-center flex rounded-lg absolute top-20 w-2/5">
            {#if data}
                {#if instantSearchVisible}
                    <InstantSearch data={data.results}/>
                {/if}
            {/if}
        </div>
    </form>
</div>