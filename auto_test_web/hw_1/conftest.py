import pytest
import yaml
import requests

with open("config.yaml", "r") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def login():
    res_post = requests.post(data["url1"], data={"username": data["username"], "password": data["password"]})
    return res_post.json()["token"]


@pytest.fixture()
def search_id():
    return 91469


@pytest.fixture()
def title():
    return "О котиках"


@pytest.fixture()
def description():
    return "Котофеич"


@pytest.fixture()
def content():
    return "Иван Петрович"
