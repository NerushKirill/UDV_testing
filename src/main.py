from fastapi import FastAPI

from .routers.collector import router as collector


app = FastAPI()
app.include_router(collector)


@app.get('/')
def read_root():
    return {
        "message": 200,
    }
