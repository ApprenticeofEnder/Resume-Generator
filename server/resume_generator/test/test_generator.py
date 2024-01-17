import yaml
from fastapi.testclient import TestClient
from resume_generator.config import settings
from resume_generator.main import app

client = TestClient(app)


def test_generate():
    data_path = settings.DATA_DIR / "sample_data.yml"
    with open(data_path) as data_file:
        resume_data_dict = yaml.safe_load(data_file)
    response = client.post("/api/generator", json=resume_data_dict)
    assert response.status_code == 201
