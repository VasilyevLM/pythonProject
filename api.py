from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import sqlite3



def db_create():
    connection = sqlite3.connect('mydb.db')
    cur = connection.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    userid INTEGER PRIMARY KEY AUTOINCREMENT,
    mastuserid TEXT,
    cookie TEXT);
    """)
    connection.commit()
    connection.close()

app = FastAPI()
origins = [
    "*"
]
db_create()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    cookie: str
    mastuserid: str

@app.get("/")
async def read_root(request:Request):
    print(request.url)
    print(request.method)
    print(request.headers)
    print(request.cookies)
    print(request.__dict__)
    return {"Hello": "World"}



@app.post("/")
async def post_item(cookie: User, request:Request):
    print(cookie)
    print(request.url)
    print(request.method)
    print(request.headers)
    print(request.cookies)
    print(request.__dict__)
    connection = sqlite3.connect('mydb.db')
    cur = connection.cursor()
    cur.execute("""INSERT INTO users(mastuserid, cookie) 
           VALUES(?, ?);""", (cookie.mastuserid, cookie.cookie))
    connection.commit()
    connection.close()
    return {'name': cookie}




