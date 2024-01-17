import subprocess
import tempfile
from pathlib import Path

from fastapi.responses import FileResponse
from resume_generator.config import sample_jinja_template
from resume_generator.schemas import ResumeData


def generate_resume(data: ResumeData, out_name: str, latex_dir_name):
    latex_dir = Path(latex_dir_name)

    generated_tex = sample_jinja_template.render(data.model_dump())

    tex_file_name = f"{out_name}.tex"
    pdf_file_name = f"{out_name}.pdf"

    tex_path = latex_dir / tex_file_name
    pdf_path = latex_dir / pdf_file_name

    with open(tex_path, "w") as tex_file:
        tex_file.write(generated_tex)

    subprocess.run(["pdflatex", f"-output-directory={latex_dir}", tex_path])

    # shutil.copy('test.tex', latex_dir)
    # subprocess.run(['pdflatex', f'-output-directory={latex_dir}', tex_path])
    # shutil.copy(pdf_path, pdf_file)
