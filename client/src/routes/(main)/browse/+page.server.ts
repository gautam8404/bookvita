import type { PageServerLoad } from './$types';

const limit = 42;

export const load :PageServerLoad = async ({fetch, url}) => {
    let subject = url.searchParams.get('subject');
    const page = url.searchParams.get('page') || "1";

    if (!subject || subject === '') {
        subject = "trending";
    }

    if (subject === "trending") {
        let sortby = url.searchParams.get('sortby');
        if (!sortby || sortby === '') {
            sortby = "daily";
        }

        const res = await fetch('http://127.0.0.1:8000/api/trending/' + sortby + "?limit=" + limit + "&page=" + page);
        const data = await res.json();

        return data;
    }
    const offset = (parseInt(page) - 1) * limit;
    const  res = await fetch('http://127.0.0.1:8000/api/subject/' + subject + "?limit=" + limit + "&offset=" + offset);
    console.log('http://127.0.0.1:8000/api/subject/' + subject + "?limit=" + limit + "&offset=" + offset
    );
    const data = await res.json();

    return data;
};