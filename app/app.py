from fastapi import FastAPI, HTTPException

app = FastAPI()

get_posts = {1 : {"title" : "new post", "content": "new cool posts"}, 
             2 : {"title" : "Latest Updates", "content": "Check out our newest features and improvements"},

3 : {"title" : "Tech Review", "content": "Analyzing the latest smartphone releases"},

4 : {"title" : "Travel Diary", "content": "Exploring hidden gems in Southeast Asia"},

5 : {"title" : "Recipe Share", "content": "Easy homemade pasta with fresh ingredients"},

6 : {"title" : "Fitness Tips", "content": "Morning routines for better energy all day"},

7 : {"title" : "Book Recommendations", "content": "Must-read novels from emerging authors"},

8 : {"title" : "Market Trends", "content": "How AI is transforming digital marketing"},

9 : {"title" : "DIY Project", "content": "Building a custom desk with recycled materials"},

10 : {"title" : "Health Advice", "content": "Simple habits to improve mental wellness"}}

@app.get("/posts")
def get_all_posts(limit : int = None):
    if limit:
        return list(get_posts.values())[:limit]
    return get_posts


@app.get("/posts/{id}")
def get_post(id : int):
    if(id not in get_post):
        return HTTPException(status_code=404, detail="Page not Found")
    return get_posts.get(id)