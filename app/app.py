from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers.markers import router

app = FastAPI()

app.include_router(
    router,
)


@app.get("/")
def hello():
    return {
        'msg': "abc"
    }


app.mount("/static", StaticFiles(directory="pictures"), name="static")
