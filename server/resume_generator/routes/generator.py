from fastapi import APIRouter, Depends, status
from resume_generator.dependencies import get_temp_dir
from resume_generator.schemas import ResumeData, ResumeResponse
from resume_generator.services import generator

router = APIRouter(prefix="/generator")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ResumeResponse)
async def generate_resume(
    resume_data: ResumeData, latex_dir_name=Depends(get_temp_dir)
):
    pdf_res = generator.generate_resume(resume_data, latex_dir_name)
    return pdf_res
