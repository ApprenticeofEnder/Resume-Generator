import dotenv

dotenv.load_dotenv("env/dev.env")

import uvicorn

if __name__ == "__main__":
    uvicorn.run("resume_generator.main:app", host="127.0.0.1", port=8000, reload=True)
