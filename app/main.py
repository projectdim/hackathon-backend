import uvicorn

if __name__ == "__main__":
    uvicorn.run(app="app.app:app", reload=True, port=5000)