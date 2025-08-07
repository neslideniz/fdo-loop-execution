from imp import reload
from importlib import reload
import uvicorn
from fastapi import FastAPI
import random

app = FastAPI()

@app.get('/')
async def root():
    return{'example': 'this is an example','data': 0}

#127.0.0.1:8000
@app.get('/random')
async def get_random():
    rn: int= random.randint(0, 100)
    return {'number': rn, 'limit': 100}


@app.get('/random/{limit}')
async def get_random(limit:int):
    rn: int= random.randint(0, limit)
    return {'number': rn, 'liamit': 100}

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    #math operator file_id pid
    return {"item_id": item_id, "q": q}





