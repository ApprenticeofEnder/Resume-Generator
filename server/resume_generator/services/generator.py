import subprocess
from pathlib import Path

from jinja2 import Template
from resume_generator.config import sample_jinja_template
from resume_generator.schemas import ResumeData, ResumeResponse
from resume_generator.services.encoding import b64_encode


def generate_resume(
    resume_data: ResumeData,
    latex_dir_name: str,
    out_name: str = "Resume",
    template: Template = sample_jinja_template,
) -> ResumeResponse:
    latex_dir = Path(latex_dir_name)

    generated_tex = sample_jinja_template.render(resume_data.model_dump())

    tex_file_name = f"{out_name}.tex"
    pdf_file_name = f"{out_name}.pdf"

    tex_path = latex_dir / tex_file_name
    pdf_path = latex_dir / pdf_file_name

    with open(tex_path, "w") as tex_file:
        tex_file.write(generated_tex)

    subprocess.run(
        ["pdflatex", f"-output-directory={latex_dir}", tex_path], capture_output=True
    )

    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    response = ResumeResponse(name=out_name, resume_b64=b64_encode(pdf_bytes))
    return response
