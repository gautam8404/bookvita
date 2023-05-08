import type { HandleFetch } from "@sveltejs/kit";

export const handleFetch: HandleFetch = async ({ request, fetch }) => {
    console.log("handleFetch", request.url);
    request = new Request(
        request.url.replace("http://localhost:8000", "http://127.0.0.1:8000"),
        request
    )
    

    return fetch(request);
}