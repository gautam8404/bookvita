import aiohttp
import asyncio
import requests
from django.core.cache import cache
from rest_framework.serializers import ValidationError

from .models import Book, Author

ol_book_url = "https://openlibrary.org/books/{book_id}.json"
ol_author_url = "https://openlibrary.org/authors/{author_id}"
ol_trending_url = "https://openlibrary.org/trending/{time}.json?limit={limit}&page={page}"
ol_subjects_url = "https://openlibrary.org/subjects/{subject}.json?limit={limit}&offset={offset}"


async def fetch(session, url):
    res = await session.get(url)
    return await res.json()


async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.create_task(fetch(session, url)))
        return await asyncio.gather(*tasks)


def get_trending(time="daily", limit=10, page=1):
    valid_times = ["now", "daily", "weekly", "monthly", "yearly", "all"]
    if time not in valid_times:
        time = "daily"
    if limit > 100:
        limit = 100
    if limit == 0 or limit is None:
        limit = 10
    if page == 0 or page is None:
        page = 1

    cache_key = "trending_{}".format(time, page)
    cached = cache.get(cache_key)
    if cached:
        if limit <= len(cached):
            return {"count": limit, "results": cached[:limit]}

    res = requests.get(ol_trending_url.format(time=time, limit=limit, page=page))
    res = res.json()
    trending = []

    for book in res['works']:
        book_obj = {}
        author_key = book['author_key'] if 'author_key' in book else None
        author_name = book['author_name'] if 'author_name' in book else None
        authors = []
        for key, name in zip(author_key, author_name) if author_key and author_name else []:
            author_obj = {}
            author_obj['author_id'] = key.split("/")[-1]
            author_obj['author_url'] = ol_author_url.format(author_id=author_obj['author_id'])
            author_obj['name'] = name
            authors.append(author_obj)
        cover_id = book['cover_i'] if 'cover_i' in book else book['covers'][0] if 'covers' in book else book['cover_id'] if 'cover_id' in book else None
        book_obj['title'] = book['title']
        book_obj['book_id'] = book['key'].split("/")[-1]
        book_obj['cover_id'] = cover_id
        book_obj['authors'] = authors
        trending.append(book_obj)
    cache.set(cache_key, trending, 60 * 60 * 24)
    return {"count": len(trending), "results": trending}


def get_subject(subject, limit=10, offset=0):
    if not subject:
        raise ValidationError("Subject is required")
    if limit > 100:
        raise ValidationError("Limit cannot be greater than 100")
    if offset < 0:
        offset = 0

    if limit == 0 or limit is None:
        limit = 10
    if offset is None:
        offset = 0

    cache_key = "subject_{}_{}_{}".format(subject, limit, offset)
    cached = cache.get(cache_key)
    if cached:
        return cached

    res = requests.get(ol_subjects_url.format(subject=subject, limit=limit, offset=offset))
    res = res.json()
    books = []

    for book in res['works']:
        book_obj = {}
        authors = []
        print(book['authors'] if 'authors' in book else [])
        for author in book['authors'] if 'authors' in book else []:
            author_obj = {}
            author_obj['author_id'] = author['key'].split("/")[-1]
            author_obj['author_url'] = ol_author_url.format(author_id=author_obj['author_id'])
            author_obj['name'] = author['name']
            authors.append(author_obj)

        book_obj['title'] = book['title']
        book_obj['book_id'] = book['key'].split("/")[-1]
        book_obj['cover_id'] = book['cover_id']
        book_obj['authors'] = authors
        books.append(book_obj)

    out = {"count": res['work_count'] if 'work_count' in res else None, "results": books, "offset": offset}
    cache.set(cache_key, out)
    return out


def get_authors(authors: list):
    if not authors or len(authors) == 0:
        return []
    authors = [author['author'] for author in authors if 'author' in author and 'key' in author['author']]
    author_urls = [f"https://openlibrary.org/" + author['key'] + ".json" for author in authors]
    author_data = asyncio.run(fetch_all(author_urls))

    parsed_authors = []
    for author in author_data:
        try:
            author_info = author['bio'] if 'bio' in author else None
            if author_info and "value" in author_info:
                author_info = author_info["value"]
            parsed_authors.append({
                "name": author['name'],
                "author_id": author['key'].split("/")[-1],
                "author_url": ol_author_url.format(author_id=author['key'].split("/")[-1]),
                "author_info": author_info,
                "author_image_id": author['photos'][0] if 'photos' in author else None,
            })
        except KeyError:
            continue
    return parsed_authors


def create_authors(parsed_authors: list):
    authors = []
    for author in parsed_authors:
        if Author.objects.filter(author_id=author['author_id']).exists():
            continue

        authors.append(Author(
            author_id=author['author_id'],
            name=author['name'],
            author_url=author['author_url'],
            author_info=author['author_info'],
            author_image_id=author['author_image_id'],
        ))
    Author.objects.bulk_create(authors)


def get_book(book_id: str):
    if not book_id:
        raise ValidationError("Book ID is required")

    cache_key = "res_book_{}".format(book_id)
    cached = cache.get(cache_key)
    if cached:
        book_data = cached
    else:
        res = requests.get(ol_book_url.format(book_id=book_id))
        if not res.ok:
            raise ValidationError("Book not found in Open Library")
        book_data = res.json()
        cache.set(cache_key, book_data, 60 * 60 * 24)

    authors = get_authors(book_data['authors']) if 'authors' in book_data else []
    date_params = ['publish_date', 'first_publish_year', 'publish_year', 'first_publish_date']

    published_date = None
    for param in date_params:
        if param in book_data:
            published_date = book_data[param]
            break

    description = book_data['description'] if 'description' in book_data else None
    if description is not None and "value" in description:
        description = description['value']

    book = {
        "book_id": book_data['key'].split("/")[-1],
        "title": book_data['title'],
        "publish_date": published_date,
        "description": description,
        "cover_id": book_data['covers'][0] if 'covers' in book_data else None,
        "subjects": book_data['subjects'] if 'subjects' in book_data else None,
        "authors": authors,
    }
    print(book)
    return book


def create_book(book_id: str):
    if Book.objects.filter(book_id=book_id).exists():
        raise ValidationError("Book already exists")

    cache_key = "res_book_{}".format(book_id)
    cached = cache.get(cache_key)
    if cached:
        book_data = cached
    else:
        res = requests.get(ol_book_url.format(book_id=book_id))
        if not res.ok:
            raise ValidationError("Book not found in Open Library")
        book_data = res.json()
        cache.set(cache_key, book_data, 60 * 60 * 24)

    authors = get_authors(book_data['authors']) if 'authors' in book_data else []
    create_authors(authors)

    date_params = ['publish_date', 'first_publish_year', 'publish_year', 'first_publish_date']
    published_date = None
    for param in date_params:
        if param in book_data:
            published_date = book_data[param]
            break

    description = book_data['description'] if 'description' in book_data else None
    if description is not None and "value" in description:
        description = description['value']

    book = Book(
        book_id=book_data['key'].split("/")[-1],
        title=book_data['title'],
        publish_date=published_date,
        description=description,
        cover_id=book_data['covers'][0] if 'covers' in book_data else None,
        subjects=book_data['subjects'] if 'subjects' in book_data else None,
    )
    book.save()

    for author in authors:
        book.author.add(Author.objects.get(author_id=author['author_id']))
    return book
