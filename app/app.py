from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from app.routers.markers import markers_router
from app.routers.events import events_router
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(markers_router)
app.include_router(events_router)

app.mount("/static", StaticFiles(directory="pictures"), name="static")

@app.get("/")
def hello():
    return {
        'msg': "abc"
    }
