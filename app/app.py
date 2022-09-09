from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers.markers import router
from .entities.evententity import EventEntity
app = FastAPI()

app.mount("/", router)
data = EventEntity().find_by_id(10)
print(data)
@app.get("/")
def hello():
    return {
        'msg': "abc"
    }


app.mount("/static", StaticFiles(directory="pictures"), name="static")
