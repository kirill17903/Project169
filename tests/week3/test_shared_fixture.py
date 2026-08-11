def test_name(sample_data):
    assert sample_data["name"] == "test_user"


def test_age(sample_data):
    assert sample_data["age"] == 25