from fastapi.responses import FileResponse
import yt_dlp  # type: ignore
import os
import uuid

async def video_proccess(video_link: str):
    download_id = str(uuid.uuid4())
    output_path = f"downloads/{download_id}/{download_id}.%(ext)s"

    ydl_opts = {
        'outtmpl': output_path,
        'format': 'best',
        'download_sections': []
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_link, download=True)
        file_name = ydl.prepare_filename(info)
        
    return FileResponse(
        path=file_name,
        filename=os.path.basename(file_name),
        media_type='video/mp4'
    )

os.makedirs("downloads", exist_ok=True)