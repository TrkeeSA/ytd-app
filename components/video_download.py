from fastapi.responses import FileResponse
import os

async def video_download(file_path: str, ):

    if os.path.exists(file_path):
        response = FileResponse(
            path=file_path,
            filename=os.path.basename(file_path),
            media_type='application/octet-stream',
            headers={"Content-Disposition": f"attachment; filename={os.path.basename(file_path)}"}
        )
        return response
    else:
        return {"error": "File not found."}