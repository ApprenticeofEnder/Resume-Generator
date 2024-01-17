import dotenv

dotenv.load_dotenv("env/dev.env")

import uvicorn

if __name__ == "__main__":
    uvicorn.run("resume_generator.main:app", host="0.0.0.0", port=8000, reload=True)
