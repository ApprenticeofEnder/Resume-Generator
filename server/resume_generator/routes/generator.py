from fastapi import APIRouter, status
from resume_generator.schemas import ResumeData
from resume_generator.config import settings

router = APIRouter(prefix="/generator")


@router.post("/", status_code=status.HTTP_201_CREATED)
def generate_resume(resume_data: ResumeData):
    return {"status": "success", "data_dir": str(settings.DATA_DIR)}
