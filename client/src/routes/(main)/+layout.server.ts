import type { LayoutServerLoad } from './$types';

export const load:LayoutServerLoad = async ({fetch, url}) => {
    const query = url.searchParams.get('q') || '';
    console.log(query);
    if (query && query.length > 0) {
        const res = await fetch('http://127.0.0.1:8000/api/search/?q=' + query + '&limit=5')
        const data = await res.json();
        return data;
    }
    return {
        results: [],
    };
};
