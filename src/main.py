from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .routers import IndexRouter

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(IndexRouter)

templates = Jinja2Templates(directory="templates")
