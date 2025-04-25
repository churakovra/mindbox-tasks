from task2.tests.conftest import client


def test_get_all_stuff_returns_list():
    value = client.get("/all_stuff").json()
    assert isinstance(value, list)
