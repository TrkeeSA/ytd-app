from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fasthx.htmy import HTMY
from htmy import Slots, Snippet
from components.header import header
from components.content import content

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

page = Snippet(
    "templates/layout.html",
    Slots({
        "header": header(),
        "content": content()
    })
)

def index_page(_: None) -> Snippet:
    return page


htmy = HTMY()

@app.get("/")
@htmy.page(index_page)

async def index() -> None:
    pass