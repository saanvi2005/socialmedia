from fastapi import FastAPI, HTTPException

app = FastAPI()

get_posts = {1 : {"title" : "new post", "content": "new cool posts"}}

@app.get("/posts")
def get_all_posts():
    return get_posts

@app.get("/posts/{id}")
def get_post(id : int):
    if(id not in get_post):
        return HTTPException(status_code=404, detail="Page not Found")
    return get_posts.get(id)