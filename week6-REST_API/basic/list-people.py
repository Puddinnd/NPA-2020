import requests
import json
from mySecret import *

access_token = myAccessToken
#################### First way to get personal information######################
# url = 'https://webexapis.com/v1/people'
# headers = {
#     'Authorization': 'Bearer {}'.format(access_token)
# }
# params = {
#  'email': '60070069@KMITL.AC.TH'
# }
# res = requests.get(url, headers=headers, params=params)
#################### Second way to get personal information#####################
person_id = "Y2lzY29zcGFyazovL3VzL1BFT1BMRS83OTAyN2QyNS00Mzk4LTQ3YWMtODQwYy03ZmE4ODM5ZjYzYTY"
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-type': 'application/json'
}
res = requests.get(url, headers=headers)


print(json.dumps(res.json(), indent=4))