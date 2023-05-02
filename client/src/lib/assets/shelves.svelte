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




<svg width="24" height="25" viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg" bind:this={svgElement}>
<path d="M6.14286 1H1.85714C1.38376 1 1 1.38376 1 1.85714V22.4286C1 22.902 1.38376 23.2857 1.85714 23.2857H6.14286C6.61624 23.2857 7 22.902 7 22.4286V1.85714C7 1.38376 6.61624 1 6.14286 1Z" stroke="black" stroke-width="1.71429" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M12.1429 4.42857H7.85714C7.38376 4.42857 7 4.81233 7 5.28571V22.4286C7 22.902 7.38376 23.2857 7.85714 23.2857H12.1429C12.6162 23.2857 13 22.902 13 22.4286V5.28571C13 4.81233 12.6162 4.42857 12.1429 4.42857Z" stroke="black" stroke-width="1.71429" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M17.8798 3.95926L14.5538 4.79161C14.0946 4.90653 13.8155 5.37197 13.9304 5.8312L18.0921 22.4612C18.2071 22.9204 18.6725 23.1996 19.1317 23.0846L22.4577 22.2523C22.917 22.1374 23.1961 21.6719 23.0811 21.2127L18.9194 4.58268C18.8045 4.12345 18.339 3.84434 17.8798 3.95926Z" stroke="black" stroke-width="1.71429" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M1 17.2857H7" stroke="black" stroke-width="1.71429" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M7 15.5714H13" stroke="black" stroke-width="1.71429" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M17.2857 19L22.2228 17.7657" stroke="black" stroke-width="1.71429" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
