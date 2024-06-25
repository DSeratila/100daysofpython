import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'


user_params = {
    "token": "zzyzhzhzhzhzhzhzhzzhzhzhzljlzlzlzl",
    "username": "dmitriys",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
# {"message":"Success. Let's visit https://pixe.la/@dmitriys , it is your profile page!","isSuccess":true}


USER_NAME = 'dmitriys'
TOKEN = 'zzyzhzhzhzhzhzhzhzzhzhzhzljlzlzlzl'
GRAPH_NAME = 'graph1'

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_NAME,
    "name": "test_graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response_graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response_graph.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_NAME}"

pixel_data = {
    "date": datetime.today().strftime("%Y%m%d"),
    "quantity": "100"
}

response_pixel = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response_pixel.text)