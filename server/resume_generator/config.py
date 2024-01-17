from functools import lru_cache
from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict
import jinja2


class Settings(BaseSettings):
    DATA_DIR: DirectoryPath

    model_config = SettingsConfigDict()


@lru_cache
def get_settings():
    return Settings()


@lru_cache
def init_jinja(settings: Settings):
    return jinja2.Environment(
        block_start_string="\\BLOCK{",
        block_end_string="}",
        variable_start_string="\\VAR{",
        variable_end_string="}",
        comment_start_string="\\#{",
        comment_end_string="}",
        line_statement_prefix="%%",
        line_comment_prefix="%#",
        trim_blocks=True,
        autoescape=False,
        loader=jinja2.FileSystemLoader(settings.DATA_DIR),
    )


@lru_cache
def get_template(settings: Settings, jinja_env: jinja2.Environment):
    return jinja_env.get_template(settings.DATA_DIR / "template.tex")


settings = get_settings()

jinja_env = init_jinja(settings)

sample_jinja_template = get_template()
