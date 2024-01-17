from fastapi import APIRouter, status
from resume_generator.config import settings
from resume_generator.dependencies import get_temp_dir
from resume_generator.schemas import ResumeData

router = APIRouter(prefix="/generator")


@router.post("/", status_code=status.HTTP_201_CREATED)
def generate_resume(resume_data: ResumeData, latex_dir_name=get_temp_dir()):

    return {"status": "success", "data_dir": str(settings.DATA_DIR)}
