from task2.tests.conftest import client
from task2.app.models.all_stuff import AllStuff


def test_get_all_stuff_values_correct():
    values = client.get("/all_stuff").json

    assert_res = True

    for value in values:
        assert_res = isinstance(value, AllStuff)

    assert assert_res == True
