<script lang="ts">
    import {page } from '$app/stores';
    export let path = "";
    export let default_stroke_color = "#000000";
    export let active_stroke_color = "#FE7410";
    export let classes = "";

    let svgElement: SVGSVGElement ;

    let active_page: string;

    page.subscribe(value => {
        active_page = value.url.pathname;
    });

    const setStrokeColor = (stroke_color: string) => {
        svgElement.setAttribute("class", classes);
        svgElement.innerHTML = svgElement.innerHTML.replace(/stroke=".*?"/g, `stroke="${stroke_color}"`);
    }



    $: {
        if (svgElement){
            if (active_page === path) {
                setStrokeColor(active_stroke_color);
            }
            else {
                setStrokeColor(default_stroke_color);
            }
        }
    }

</script>


<svg width="25" height="21" viewBox="0 0 25 21" fill="none" xmlns="http://www.w3.org/2000/svg" bind:this={svgElement}>
<path d="M12.1563 19.6089L2.69344 11.0374C-2.44942 5.89458 5.11058 -3.97971 12.1563 4.00887C19.202 -3.97971 26.7277 5.92887 21.6192 11.0374L12.1563 19.6089Z" stroke="black" stroke-width="1.71429" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
