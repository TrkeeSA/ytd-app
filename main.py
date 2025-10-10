from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fasthx.jinja import Jinja
from components.header import header
from components.input_video_link import input_video_link
from components.proccess_video import proccess_video

app = FastAPI()
jinja = Jinja(Jinja2Templates("templates"))

@app.get("/")
@jinja.page("index.html")
def index() -> None:
    pass