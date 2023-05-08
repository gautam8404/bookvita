import type { PageServerLoad } from './$types';
import { error } from '@sveltejs/kit';

export const load = (async ({params, fetch}) => {
    const res = await fetch('http://127.0.0.1:8000/api/books/' + params.olid);
    if (!res.ok) {
        throw error(res.status, 'Book not found');  
    }
    const data = await res.json();
    return data;
}) satisfies PageServerLoad;