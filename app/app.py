from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .support.db.connection import createQueryBuilder
from app.routers.markers import router

app = FastAPI()

app.mount("/", router)

query = createQueryBuilder('events')
print(query.find_by_id(10))



@app.get("/")
def hello():
    return {
        'msg': "abc"
    }


app.mount("/static", StaticFiles(directory="pictures"), name="static")
