import dotenv

dotenv.load_dotenv("env/dev.env")

import uvicorn
from resume_generator.main import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
