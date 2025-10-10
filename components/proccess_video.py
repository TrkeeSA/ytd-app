from htmy import Component, html
from fasthx.htmy import HTMY, CurrentRequest, RouteParams

def proccess_video() -> Component:
    return (
        html.div(
            html.h2("your link is:" + " {{ youtube_video_link }}")
        )
    )