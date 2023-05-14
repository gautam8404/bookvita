<script lang="ts">
	import NavBar from '$lib/components/NavBar.svelte';
	import SideBar from '$lib/components/SideBar.svelte';
</script>

<div class="wrapper">
	<div class="navbar">
		<NavBar />
	</div>

	<div class="flex mt-3 h-5/6">
		<div class="sidebar pr-20">
			<SideBar />
		</div>

		<div class="content mt-14 h-screen">
			<slot />
		</div>
	</div>
</div>
