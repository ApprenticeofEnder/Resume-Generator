from functools import lru_cache
from pathlib import Path

import jinja2
from jinja2 import Environment, select_autoescape
from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATA_DIR: DirectoryPath

    model_config = SettingsConfigDict()


@lru_cache
def get_settings():
    return Settings()


@lru_cache
def init_jinja(data_dir: Path):
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
        autoescape=select_autoescape(),
        loader=jinja2.FileSystemLoader(data_dir),
    )


@lru_cache
def get_template(jinja_env: jinja2.Environment):
    return jinja_env.get_template("template.tex")


settings = get_settings()

jinja_env = init_jinja(settings.DATA_DIR)

sample_jinja_template = get_template(jinja_env)
