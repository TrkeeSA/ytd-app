import yt_dlp # type: ignore

def video_info(video_link: str):

    ydl_opts: dict = {}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(video_link, download=False)

    return ydl.sanitize_info(video_info)

def download_video():
    ...