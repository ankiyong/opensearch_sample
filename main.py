from fastapi import FastAPI
import opensearchpy
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Query,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import requests

templates = Jinja2Templates(directory='./templates/startbootstrap-sb-admin-gh-pages/')

app = FastAPI()
app.mount("/assets",StaticFiles(directory="static/assets"))
app.mount("/css",StaticFiles(directory="static/css"))
app.mount("/js",StaticFiles(directory="static/js"))

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})