<script lang="ts">
    import type { PageData } from './$types';
    import {page} from '$app/stores';

    let {olid} = $page.params;
    
    export let data: PageData;

    let conf = process.env.NODE_ENV;
</script> 


{conf}

