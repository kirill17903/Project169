import pytest

cleanup_log = []


@pytest.fixture(autouse=True)
def track_cleanup():
    yield
    cleanup_log.append("cleaned")


def test_example():
    assert 1 + 1 == 2


def test_cleanup_happened():
    assert len(cleanup_log) >= 1