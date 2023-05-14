import type { RequestHandler } from './$types';

export const GET: RequestHandler = async ({ url, fetch }) => {
	const query = url.searchParams.get('q') || '';
	const res = await fetch('/api/search/?q=' + query + '&limit=5');
	return res;
};
