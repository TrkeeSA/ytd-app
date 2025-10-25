from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fasthx.jinja import Jinja
from components.video_info import video_info
from components.video_proccess import video_proccess
from components.video_download import video_download

app = FastAPI()
jinja = Jinja(Jinja2Templates("templates"))
app.mount("/downloads", StaticFiles(directory="downloads"), name="downloads")


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

@app.post("/video-proccess")
@jinja.hx("/partial/video-download.html")
async def htmx_download(
    request: Request,
    ) -> dict:
    form_data = await request.form()
    video_link = str(form_data.get("video_link"))
    file_response = await video_proccess(video_link)
    return {"FileResponse": file_response}

@app.get("/downloads/{file_path}")
async def download_file(file_path: str):
    return await video_download(file_path)