from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import uvicorn

app = FastAPI()

app.mount("/", StaticFiles(directory="build"), name="build")
app.mount("/data", StaticFiles(directory="data"), name="data")

@app.get("/", response_class=HTMLResponse)
async def root():
    index_path = Path("build") / "index.html"

    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)