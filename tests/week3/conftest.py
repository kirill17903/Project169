import pytest
import requests


@pytest.fixture
def sample_data():
    return {"name": "test_user", "age": 25}


@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    yield session
    session.close()