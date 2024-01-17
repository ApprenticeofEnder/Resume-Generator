from functools import lru_cache
from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATA_DIR: DirectoryPath

    model_config = SettingsConfigDict()


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
