import requests
from datetime import datetime

api_endpt = "https://pixe.la/v1/users"
TOKEN = "hasjfshdlsj"
USER_NAME = "akhil-4407"
user_params = {
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# responce = requests.post(url=api_endpt,json=user_params)
# print(responce.text)
graph_endpt = f"{api_endpt}/{USER_NAME}/graphs"
headers = {
    "X-USER-TOKEN":TOKEN
}
graph_config = {
    "id":"graph1",
    "name":"Consistency",
    "Unit": "Days",
    "type":"int",
    "color":"sora"
}
# responce = requests.post(url=graph_endpt,json=graph_config,headers=headers)
# print(responce.text)
today = datetime(year=2026,month=3,day=30)
pixel_key = f"{api_endpt}/{USER_NAME}/graphs/graph1"
pixel_config ={
    "date":today.strftime("%Y%m%d"),
    "quantity":"1",
}
# responce = requests.post(url=pixel_key,json=pixel_config,headers=headers)
# print(responce.text)


update_key = f"{api_endpt}/{USER_NAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
update_config = {
    "quantity": "4"
}
responce = requests.put(url=update_key,json=update_config,headers=headers)
print(responce.text)