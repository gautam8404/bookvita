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


<svg width="23" height="25" viewBox="0 0 23 25" fill="none" xmlns="http://www.w3.org/2000/svg" bind:this={svgElement}>
<path d="M19.8571 23.2857H2.71429C2.25963 23.2857 1.82359 23.1051 1.5021 22.7836C1.18061 22.4621 1 22.0261 1 21.5714V2.71429C1 2.25963 1.18061 1.82359 1.5021 1.5021C1.82359 1.18061 2.25963 1 2.71429 1H19.8571C20.3118 1 20.7478 1.18061 21.0693 1.5021C21.3908 1.82359 21.5714 2.25963 21.5714 2.71429V21.5714C21.5714 22.0261 21.3908 22.4621 21.0693 22.7836C20.7478 23.1051 20.3118 23.2857 19.8571 23.2857Z" stroke="black" stroke-width="1.71429" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M6.14286 1V23.2857" stroke="black" stroke-width="1.71429" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M12.1429 7H15.5714" stroke="black" stroke-width="1.71429" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
