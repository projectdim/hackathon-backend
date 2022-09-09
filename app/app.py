from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers.markers import router

app = FastAPI()

app.mount("/static", StaticFiles(directory="pictures"), name="static")
app.mount("/", router)

@app.get("/")
def hello():
    return {
        'msg': "abc"
    }
