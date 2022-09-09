from fastapi import FastAPI
import imageio as iio
import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
#path = "C:\\Users\\MilaS_wnlsblx\\OneDrive\\Desktop\\learnings\\test_1.jpg"


@app.get("/")
def hello():
    return {
        'msg': "abc"
    }


app.mount("/static", StaticFiles(directory="pictures"), name="static")
#
#
# @app.get("/vector_image", responses={200: {"description": "A picture of a vector image.", "content" : {"image/jpeg" : {"example" : "No example available. Just imagine a picture of a vector image."}}}})
# def image_endpoint():
#     file_path = os.path.join("app\\test_1.jpg")
#
#     print(file_path,file_path_2)
#     if os.path.exists(file_path):
#         return FileResponse(file_path, media_type="image/jpeg", filename="test_1.jpg")
#     return {"error" : "File not found!"}