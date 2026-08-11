import time
import pytest


@pytest.fixture(scope="module")
def module_resource():
    created_at = time.time()
    yield {"value": "resource", "created_at": created_at}


def test_one(module_resource):
    print(f"\ntest_one: fixture created at {module_resource['created_at']}")
    assert module_resource["value"] == "resource"


def test_two(module_resource):
    print(f"\ntest_two: fixture created at {module_resource['created_at']}")
    assert module_resource["value"] == "resource"


def test_api_client(api_client):
    response = api_client.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200