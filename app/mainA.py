from fastapi import FastAPI
from . import models
from .database import engine
from fastapi.middleware.cors import CORSMiddleware
from .routers import Oauth, post, users, vote


# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "https://google.com",
    "https://youtube.com",
    "http://myapp.com",
    "http://localhost:5341",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(users.router)
app.include_router(Oauth.router)
app.include_router(vote.router)

app.get("/")


def root():
    return {"hello": "world"}
