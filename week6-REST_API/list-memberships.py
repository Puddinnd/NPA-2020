from mySecret import *
import requests
import json

access_token = myAccessToken

room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vZWNlM2NiZDAtOTA3NC0xMWViLWEyODktZDczOWQ1ZjdhMWNh'
url = 'https://webexapis.com/v1/memberships'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {'roomId': room_id}
res = requests.get(url, headers=headers, params=params)

print(json.dumps(res.json(), indent=4))
