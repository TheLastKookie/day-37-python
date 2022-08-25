import requests
import os
from datetime import datetime

TOKEN = os.environ.get("TOKEN")
USERNAME = os.environ.get("USERNAME")
GRAPHID = os.environ.get("GRAPHID")

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPHID,
    "name": "Coding Graph",
    "unit": "Projects",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
today = datetime.now()
today = today.strftime("%Y%m%d")
pixel_config = {
    "date": today,
    "quantity": input("How many projects did you complete today? "),
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

update_pixel_endpoint = f"{pixel_endpoint}/{today}"
update_config = {
    "quantity": "1",
}

# response = requests.put(url=update_pixel_endpoint, json=update_config, headers=headers)
# print(response.text)

delete_endpoint = f"{pixel_endpoint}/{today}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
