from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fasthx.jinja import Jinja
from components.video_proccess import video_info

app = FastAPI()
jinja = Jinja(Jinja2Templates("templates"))

@app.get("/")
@jinja.page("index.html")
def index() -> None:
    ...

@app.post("/video-show")
@jinja.hx("/partial/video-show.html")

async def htmx_data(
    request: Request,
    ) -> dict:
    form_data = await request.form()
    video_link = str(form_data.get("video_link"))
    return {"video_info": video_info(video_link), "video_link": video_link}