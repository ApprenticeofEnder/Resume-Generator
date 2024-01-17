import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from resume_generator.routes import generator

app = FastAPI(title="ResGen")

api = FastAPI(title="ResGen API")
api.include_router(generator.router)

app.mount("/api", api)
app.mount("/", StaticFiles(directory="dist", html=True), name="dist")
app.mount("/data", StaticFiles(directory="data"), name="data")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
