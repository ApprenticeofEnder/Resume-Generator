import tempfile
from pathlib import Path

from resume_generator.config import sample_jinja_template
from resume_generator.schemas import ResumeData


def generate_resume(data: ResumeData):
    with tempfile.TemporaryDirectory() as latex_dir_name:
        pass
        # latex_dir = Path(latex_dir_name)

        # tex_file = 'test.tex'
        # pdf_file = 'test.pdf'

        # tex_path = latex_dir / tex_file
        # pdf_path = latex_dir / pdf_file

        # shutil.copy('test.tex', latex_dir)
        # subprocess.run(['pdflatex', f'-output-directory={latex_dir}', tex_path])
        # shutil.copy(pdf_path, pdf_file)
