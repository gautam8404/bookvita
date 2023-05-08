import type { PageServerLoad } from './$types';
const limit = 50;

export const load: PageServerLoad = async ({ fetch, params, url }) => {
	const query = params.query || '';
	const page = url.searchParams.get('page') || '1';
	const offset = (parseInt(page) - 1) * limit;
	if (query && query.length > 0) {
		const res = await fetch(
			'http://127.0.0.1:8000/api/search/?q=' + query + '&limit=' + limit + '&offset=' + offset
		);
		const data = await res.json();
		return data;
	}
	return {
		results: []
	};
};
