import type { RequestHandler } from './$types';

export const GET: RequestHandler = async ({url, fetch}) => {
    const query = url.searchParams.get('q') || '';
    const res = await fetch('http://127.0.0.1:8000/api/search/?q=' + query + '&limit=5');
    return res;
};