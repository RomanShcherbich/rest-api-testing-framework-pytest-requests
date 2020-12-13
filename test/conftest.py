import pytest
import requests
import json

AUTH_PATH = "/auth"


def print_http_request(method, url):
    print("\r{} request to {}".format(method, url))


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, path='/', params=None, data=None, headers=None):
        url = self.base_url + path
        print_http_request("POST", url)
        return requests.post(url=url, params=params, data=data, headers=headers)

    def get(self, path='/', params=None, data=None, headers=None):
        url = self.base_url + path
        print_http_request("GET", url)
        return requests.get(url=url, params=params, data=data, headers=headers)


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://restful-booker.herokuapp.ru",
        help="Restful booker server url"
    )
    parser.addoption(
        "--username",
        action="store",
        help="Username of admin"
    )
    parser.addoption(
        "--password",
        action="store",
        help="Password of admin"
    )


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_url=base_url)


@pytest.fixture(scope="session")
def headers():
    return {"Content-Type": "application/json"}


@pytest.fixture(scope="session")
def token(api_client, request, headers):
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    body = json.dumps({"username": username, "password": password})
    resp = api_client.post(AUTH_PATH, data=body, headers=headers)
    token = resp.json()['token']
    assert resp.status_code == 200
    assert token is not None
    assert type(token) is str
    assert len(token) >= 15
    return token
