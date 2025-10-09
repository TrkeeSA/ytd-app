from htmy import Component, html
from fasthx.htmy import HTMY, ComponentHeader, CurrentRequest, RouteParams

def input_video_link() -> Component:
    
    return (
        html.div(
            html.label(
                "Enter Youtube Video Link",
                for_="textInputDefault",
                class_="w-fit pl-0.5 text-sm",
                x_data="{ name: '}"
            ),
            html.input_(
                 id_="textInputDefault",
                 class_="w-full rounded-sm border border-neutral-300 bg-neutral-50 text-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-black disabled:cursor-not-allowed disabled:opacity-75 dark:border-neutral-700 dark:bg-neutral-900/50 dark:focus-visible:outline-white",
                 name_="youtube-vido-link",
                 placeholder_="Enter youtube video lin here"
                 
            ),
            html.input_(
                type_="submit",
                value_="Submit",
                # --HTMX directives.
                hx_post="/process_video",
            )
        )
    )