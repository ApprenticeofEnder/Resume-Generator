from pathlib import Path
from typing import Any

import jinja2
import pytest
import yaml
from fastapi.testclient import TestClient
from resume_generator.dependencies import get_temp_dir
from resume_generator.main import app
from resume_generator.schemas import ResumeData, ResumeResponse
from resume_generator.services import generator
from resume_generator.services.encoding import b64_decode
from resume_generator.test.fixtures import jinja_env, test_data_path, test_template_path

client = TestClient(app)


class TestGenerator:
    # ---SETUP---
    STATIC_SUCCESS = 200
    GENERATE_ENDPOINT_SUCCESS = 201
    GENERATE_ENDPOINT = "/api/generator"
    SAMPLE_DATA_ENDPOINT = "/data/sample_data.yml"
    RESUME_NAME = "TestResume"

    def _get_test_data(self, test_data_path):
        with open(test_data_path) as data_file:
            resume_data_dict = yaml.safe_load(data_file)
        return resume_data_dict

    # ---TESTS---
    def test_sample_data_available(self):
        response = client.get(self.SAMPLE_DATA_ENDPOINT)
        assert response.status_code == self.STATIC_SUCCESS

    def test_generate_sample_data(self):
        resume_data_yaml = client.get(self.SAMPLE_DATA_ENDPOINT).text
        resume_data_dict = yaml.safe_load(resume_data_yaml)

        response = client.post(self.GENERATE_ENDPOINT, json=resume_data_dict)

        assert response.status_code == self.GENERATE_ENDPOINT_SUCCESS

    def test_generate_test_data(self, test_data_path):
        resume_data_dict = self._get_test_data(test_data_path)

        response = client.post(self.GENERATE_ENDPOINT, json=resume_data_dict)

        assert response.status_code == self.GENERATE_ENDPOINT_SUCCESS

    @pytest.mark.asyncio
    async def test_generator_service(
        self,
        test_data_path: Path,
        test_template_path: Path,
        jinja_env: jinja2.Environment,
    ):
        resume_data_dict: dict[str, Any] = self._get_test_data(test_data_path)

        resume_template: jinja2.Template = jinja_env.get_template(
            test_template_path.name
        )
        resume_data = ResumeData(**resume_data_dict)
        latex_dir_name = await get_temp_dir().__anext__()
        pdf_res: ResumeResponse = generator.generate_resume(
            resume_data,
            latex_dir_name,
            out_name=self.RESUME_NAME,
            template=resume_template,
        )
        assert pdf_res.name == self.RESUME_NAME
