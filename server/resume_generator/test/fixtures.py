from pathlib import Path

import jinja2
import pytest
from resume_generator.config import init_jinja, settings

TEST_DIR = Path(__file__).parent
TEST_ASSET_DIR = TEST_DIR / "data"


@pytest.fixture
def test_data_path():
    return TEST_ASSET_DIR / "sample_data.yml"


@pytest.fixture()
def test_template_path():
    return TEST_ASSET_DIR / "template.tex"


@pytest.fixture()
def jinja_env():
    return init_jinja(TEST_ASSET_DIR)
