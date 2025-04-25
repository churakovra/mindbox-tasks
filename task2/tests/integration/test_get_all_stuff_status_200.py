from http import HTTPStatus

from task2.tests.conftest import client


def test_get_all_stuff_status_200():
    response = client.get("/all_stuff")
    assert response.status_code == HTTPStatus.OK
