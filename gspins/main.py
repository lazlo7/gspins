from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("gspins.main:app", host="0.0.0.0", port=8000, reload=True)
