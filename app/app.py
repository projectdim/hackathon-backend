from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers.markers import router
from app.routers.events import events_router
app = FastAPI()

app.include_router(router)
app.include_router(events_router)

@app.get("/")
def hello():
    return {
        'msg': "abc"
    }


app.mount("/static", StaticFiles(directory="pictures"), name="static")
