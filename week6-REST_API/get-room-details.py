from mySecret import *
import requests
import json

access_token = myAccessToken

room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vZWNlM2NiZDAtOTA3NC0xMWViLWEyODktZDczOWQ1ZjdhMWNh'
url = 'https://webexapis.com/v1/rooms/{}/meetingInfo'.format(room_id)
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)

print(json.dumps(res.json(), indent=4))
