from mySecret import *
import requests
import json
access_token = myAccessToken

url = 'https://webexapis.com/v1/rooms'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params={'title': 'DevNet Associate Training!'}
res = requests.post(url, headers=headers, json=params)

print(json.dumps(res.json(), indent=4))