from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
 
my_posts = [{"title": "first post", "content": "first post of the month", "id": 1},
         {"title": "second post", "content": "second post of the month", "id": 2}]

class Post(BaseModel): 
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None



@app.get("/")
def index():
    return {"message": "this is the index route"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_post(new_post: Post):
    print(new_post)
    print(new_post.dict())
    return {"data": new_post}

