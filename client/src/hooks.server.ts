import type { HandleFetch } from '@sveltejs/kit';
import {env} from '$env/dynamic/private';

const SERVER_URL = env.SERVER_URL || 'http://127.0.0.1:8000';
export const handleFetch: HandleFetch = async ({ request, fetch }) => {
	console.log('handleFetch', request.url);
	console.log('handleFetch', SERVER_URL);
	if (request.url.startsWith('http://localhost:5173/api/') || request.url.startsWith('http://127.0.0.1:8000/api/')) {
		let replaceUrl = "http://localhost:5173/api/";
		if (request.url.startsWith('http://127.0.0.1:8000/api/')) {
			replaceUrl = "http://127.0.0.1:8000/api/"
		}
		request = new Request(
			request.url.replace(replaceUrl, SERVER_URL + '/api/'),
			request
		)
	}
	console.log('handleFetch', request.url);
	return fetch(request);
};