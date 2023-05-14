<script lang="ts">
	import '../app.css';
    import {Toaster} from "svelte-french-toast";
    import ProgressBar from 'svelte-progress-bar';
	import { beforeNavigate, afterNavigate } from '$app/navigation';

	let progress: any;

	beforeNavigate(() => {
		progress.start();
	});

	afterNavigate(() => {
		progress.complete();
	});
</script>

<Toaster />
<ProgressBar color="#ff0000" width="5px" bind:this={progress} />

<slot />
