import yaml
import requests

with open("config.yaml", "r") as f:
    data = yaml.safe_load(f)


def test_1(login, search_id):
    res_get = requests.get(data["url"], params={"owner": "notMe"}, headers={"X-Auth-Token": login})
    list_id = [i["id"] for i in res_get.json()["data"]]
    assert search_id in list_id, "test_1 FAIL"


def test_2(login, title, description, content):
    res_post = requests.post(data["url"], params={"title": title, "description": description, "content": content},
                             headers={"X-Auth-Token": login})
    assert res_post, "test_2 FAIL"
