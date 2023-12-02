import pytest
import requests

url = "https://test-stand.gb.ru/gateway/login"
login = "igorkrut777"
password = "c79f4a3a6f"

result = requests.post(url=url, data={"username": login, "password": password})
token = result.json()["token"]

res_get = requests.get(url="https://test-stand.gb.ru/api/posts", headers={"X-Auth-Token": token}, params={"owner": "notMe"})
print(res_get)
print(res_get.json())