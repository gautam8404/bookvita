<script lang="ts">
	import { page } from '$app/stores';
	export let path = '';
	export let default_stroke_color = '#000000';
	export let active_stroke_color = '#FE7410';
	export let classes = '';

	let svgElement: SVGSVGElement;

	let active_page: string;

	page.subscribe((value) => {
		active_page = value.url.pathname;
	});

	const setStrokeColor = (stroke_color: string) => {
		svgElement.setAttribute('class', classes);
		svgElement.innerHTML = svgElement.innerHTML.replace(
			/stroke=".*?"/g,
			`stroke="${stroke_color}"`
		);
	};

	$: {
		if (svgElement) {
			if (active_page === path) {
				setStrokeColor(active_stroke_color);
			} else {
				setStrokeColor(default_stroke_color);
			}
		}
	}
</script>

<svg
	width="25"
	height="25"
	viewBox="0 0 25 25"
	fill="none"
	xmlns="http://www.w3.org/2000/svg"
	bind:this={svgElement}
>
	<path
		d="M7.85714 1H2.71429C1.76751 1 1 1.76751 1 2.71429V7.85714C1 8.80392 1.76751 9.57143 2.71429 9.57143H7.85714C8.80392 9.57143 9.57143 8.80392 9.57143 7.85714V2.71429C9.57143 1.76751 8.80392 1 7.85714 1Z"
		stroke="black"
		stroke-width="1.71429"
		stroke-linecap="round"
		stroke-linejoin="round"
	/>
	<path
		d="M21.5714 1H16.4286C15.4818 1 14.7143 1.76751 14.7143 2.71429V7.85714C14.7143 8.80392 15.4818 9.57143 16.4286 9.57143H21.5714C22.5182 9.57143 23.2857 8.80392 23.2857 7.85714V2.71429C23.2857 1.76751 22.5182 1 21.5714 1Z"
		stroke="black"
		stroke-width="1.71429"
		stroke-linecap="round"
		stroke-linejoin="round"
	/>
	<path
		d="M7.85714 14.7143H2.71429C1.76751 14.7143 1 15.4818 1 16.4286V21.5714C1 22.5182 1.76751 23.2857 2.71429 23.2857H7.85714C8.80392 23.2857 9.57143 22.5182 9.57143 21.5714V16.4286C9.57143 15.4818 8.80392 14.7143 7.85714 14.7143Z"
		stroke="black"
		stroke-width="1.71429"
		stroke-linecap="round"
		stroke-linejoin="round"
	/>
	<path
		d="M21.5714 14.7143H16.4286C15.4818 14.7143 14.7143 15.4818 14.7143 16.4286V21.5714C14.7143 22.5182 15.4818 23.2857 16.4286 23.2857H21.5714C22.5182 23.2857 23.2857 22.5182 23.2857 21.5714V16.4286C23.2857 15.4818 22.5182 14.7143 21.5714 14.7143Z"
		stroke="black"
		stroke-width="1.71429"
		stroke-linecap="round"
		stroke-linejoin="round"
	/>
</svg>
