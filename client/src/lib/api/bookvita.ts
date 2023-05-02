import type { Cookies } from "@sveltejs/kit";
import { goto } from "$app/navigation";

class BookVita {
    private baseURL = "http://localhost8000/api/";
    private headers = new Headers();

    constructor() {
        this.headers.append("Content-Type", "application/json");
    }

    async refreshToken(cookies: Cookies){
        this.headers.append("Authorization", "Bearer " + cookies.get("access_token"));
        const res = await fetch(this.baseURL + "token/refresh", {
            method: "POST",
            headers: this.headers,
            body: JSON.stringify({refresh: cookies.get("refresh_token")})
        });
        if (res.status == 401){
            cookies.set("access_token", "");
            cookies.set("refresh_token", "");
            goto("/login");

            throw new Error("Unauthorized");
        }

        const data = await res.json();
        cookies.set("access_token", data.access_token);
        cookies.set("refresh_token", data.refresh_token);
        
        return data;
    }

    async makeRequest(url: string, method: string, cookies?: Cookies, body?: any){
        if (cookies){
            this.headers.append("Authorization", "Bearer " + cookies.get("access_token"));
        }
        const res = await fetch(this.baseURL + url, {
            method: method,
            headers: this.headers,
            body: JSON.stringify(body)
        });

        if (cookies && res.status == 401){
            await this.refreshToken(cookies)
            .then(() => {
                return this.makeRequest(url, method, cookies, body);
            })
            .catch(() => {
                throw new Error("Unauthorized");
            });
        }


        if (res.status == 200){
            const data = await res.json();
            return data;
        }
        else {
            await res.json()
            .then((data) => {
                throw new Error(data.message);
            })
            .catch(() => {
                throw new Error("Something went wrong");
            }
            );
        }

    }
    

    async getBooks(){
        const res = await fetch(this.baseURL + "books");
        const data = await res.json();
        return data;
    }

    async getBook(id: string){
        const res = await fetch(this.baseURL + "books/" + id);
        const data = await res.json();
        return data;
    }

    async addBook(book_id: string){
        const res = await fetch(this.baseURL + "books/" , {
            method: "POST",
            headers: this.headers,
            body: JSON.stringify({book_id})
        });
        const data = await res.json();
        return data;
    }

    async deleteBook(id: string){
        const res = await fetch(this.baseURL + "books/" + id, {
            method: "DELETE",
            headers: this.headers
        });
        const data = await res.json();
        return data;
    }

    async likebook(id: string, cookies: Cookies){
        this.headers.append("Authorization", "Bearer " + cookies.get("access_token"));
        const res = await fetch(this.baseURL + "books/" + id + "/like", {
            method: "POST",
            headers: this.headers
        });

        if (res.status == 401){
            await this.refreshToken(cookies)
            .then(() => {
                return this.likebook(id, cookies);
            })
            .catch(() => {
                throw new Error("Unauthorized");
            });
        }
    }

    
}

export const bookvita = new BookVita();