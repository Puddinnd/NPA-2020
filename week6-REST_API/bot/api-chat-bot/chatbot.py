from __future__ import print_function # Print to console in flesk's method 
import requests
import json
import time
import sys
import datetime
import html
import googleapiclient.discovery
from youtube_title_parse import get_artist_title    ###https://pypi.org/project/youtube-title-parse/
from spotipy.oauth2 import SpotifyClientCredentials ###https://github.com/plamere/spotipy
import spotipy                                      ### ^
from flask import Flask, request
from Secret import *
from pprint import pprint


################################### Register our URL to Webhook ###############################
def verifyWebhook():
    wh_data = getWebhook()
    if len(wh_data) > 1:
        print(" * Remove duplicate webhooks")
        for wh in wh_data:
            deleteWebhook(wh['id'])
        verifyWebhook()
    if wh_data == []:
        print(" * Create new webhook...")
        registerURL2Webhook()
        verifyWebhook()
    else:
        wh_data = wh_data[0]
        # pprint(wh_data)
        if checkWebhookDetails(wh_data):
            print(" * Webhook is active!!!")
        else:
            print(" * Remove old webhook")
            deleteWebhook(wh_data['id'])
            verifyWebhook()

def getWebhook():
    url = "https://webexapis.com/v1/webhooks"
    header = {"Authorization": "Bearer %s" % my_token, "content-type": "application/json"}
    requests.packages.urllib3.disable_warnings()
    api_response = requests.get(url, headers=header, verify=False).json()
    # print("Get webhook details: ")
    # pprint(api_response)
    try:
        return api_response['items']
    except:
        return []

def checkWebhookDetails(data):
    # print("Check webhook details")
    # pprint(data)
    for key in webhook_spec:
        try:
            if webhook_spec[key] != data[key]:
                return False
        except:
            return False
    return True

def registerURL2Webhook():
    header = {"Authorization": "Bearer %s" % my_token, "content-type": "application/json"}
    requests.packages.urllib3.disable_warnings()
    webhook_url = "https://api.ciscospark.com/v1/webhooks"
    api_response = requests.post(webhook_url, json=webhook_spec, headers=header, verify=False)
    # print("regis response:", api_response.status_code)
    return api_response

def deleteWebhook(webhookId):
    header = {"Authorization": "Bearer %s" % my_token, "content-type": "application/json"}
    requests.packages.urllib3.disable_warnings()
    webhook_url = "https://api.ciscospark.com/v1/webhooks/" + webhookId
    api_response = requests.delete(webhook_url, headers=header, verify=False)

################################## Handling data from Webhook #################################
app = Flask(__name__)
@app.route("/",methods=['POST']) # all request from webhook will come with POST method
def webhook():
    try:
        ### Get the json data
        json = request.json
        ### sending back
        room_id = json["data"]["roomId"] # Room: TEST BOT
        # print(room_id, file=sys.stdout)
        if room_id == selected_room_id:
            bot_sendMessange(json)
        return "Success"
    except:
        return "Something wrong with data from webhook"

################################# BOT responding messange ###################################
def bot_sendMessange(data):
    msg_json = getMessangeDetails(data['data']['id'])
    response_text = ""
    #### Filter data before sent to API
    if msg_json == []:
        return 
    if msg_json['roomId'] != selected_room_id:  # Manually filter roomId bc API's filter not working...
        return 
    #### Fetch data from APIs
    if  msg_json['text'].startswith('/'):
        print(" * Bot has received a command..(/)")
        location = msg_json['text'].strip()[1:]
        latlng = getLatLong(location)
        if not latlng: return
        iss_passtimes = getISSPassTimes(latlng)
        if not iss_passtimes: return
        timestamp = datetime.datetime.fromtimestamp(iss_passtimes['risetime'])
        dt = timestamp.strftime('on %A %d %B %Y at %H:%M:%S')
        response_text = "ISS will pass {} {}".format(location.capitalize(), dt)
    elif msg_json['text'].startswith('>'):
        print(" * Bot has received a command..(>)")
        searchstr = msg_json['text'].strip()[1:]
        youtube_api_response = searchForVideo(searchstr)
        # print("GOT:", youtube_api_response['title'] + ":" + youtube_api_response['artist'])
        # print("link:", youtube_api_response['link']['youtube'])
        spotify_api_response = searchInSpotify(youtube_api_response['title'] + " " + youtube_api_response['artist'])
        response_text = "Title: " + youtube_api_response['title'] + " - " + youtube_api_response['artist'] + "\r\n"
        if youtube_api_response:
            response_text += "youtube: " + youtube_api_response['link']['youtube'] + "\r\n"
        else:
            response_text += "youtube: -\r\n"
        if spotify_api_response:
            response_text += "spotify: " + spotify_api_response['link']['spotify']
        else:
            response_text += "spotify: -\r\n"
    else:
        return
    #### Send response messange
    header = {"Authorization": "Bearer %s" % bot_token, "content-type": "application/json"}
    requests.packages.urllib3.disable_warnings()
    postmsg_url = "https://webexapis.com/v1/messages"
    payload = {
        "roomId": selected_room_id,
        "text": response_text,
    }
    api_response = requests.post(postmsg_url, headers=header, json=payload, verify=False)
    if api_response.status_code == 200:
        print(" * Post messange success!")
    else:
        print(" - Can not post messange..")

### Get messange details from webex
def getMessangeDetails(msgId):
    header = {"Authorization": "Bearer %s" % my_token, "content-type": "application/json"}
    requests.packages.urllib3.disable_warnings()
    getmsg_url = "https://webexapis.com/v1/messages/" + msgId
    try:   
        api_response = requests.get(getmsg_url, headers=header, verify=False).json()
        # print("regis response:", api_response.status_code)
        return api_response
    except:
        return []

### /ISS
def getLatLong(location):
    # print("Location:", location)
    mapquest_url = "http://www.mapquestapi.com/geocoding/v1/address"
    param= {
        "key": mapquest_token,
        "location": location
    }
    api_response = requests.get(mapquest_url, params=param)
    if api_response.status_code == 200:
        # pprint(api_response.json())
        try:
            return api_response.json()['results'][0]['locations'][0]['displayLatLng']
        except:
            return
    else:
        return

def getISSPassTimes(latlng):
    iss_url = "http://api.open-notify.org/iss-pass.json"
    param = {
        'lat': latlng['lat'],
        'lon': latlng['lng']
    }
    api_response = requests.get(iss_url, params=param)
    if api_response.status_code == 200:
        # pprint(api_response.json())
        try:
            return api_response.json()['response'][0]
        except:
            return
    else:
        return

### >Youtube
def searchForVideo(searchstr):
    # print("Search for:", searchstr)
    try:
        youtube = googleapiclient.discovery.build(
            youtube_api_service_name,
            youtube_api_version,
            developerKey = youtube_DEVELOPER_KEY
        )
        request = youtube.search().list(
            order="viewCount",
            q=searchstr,
            part="id,snippet",
        )
        response = request.execute()
        # pprint(response['items'][0])
        youtube_link = "https://youtu.be/" + response['items'][0]['id']['videoId']
        youtube_title = html.unescape(response['items'][0]['snippet']['title'])
        youtube_title = youtube_title.split("feat.")[0].split("ft.")[0]
        # print("Youtube title:", youtube_title)
        artist, title = get_artist_title(youtube_title)
        return {'link':{"youtube":youtube_link}, 'title':title, 'artist':artist}
    except:
        return

def searchInSpotify(searchstr):
    print("search:", searchstr)
    results = {}
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=spotify_client_id,client_secret=spotify_client_secret))
        results = sp.search(q=searchstr, limit=1)
        return {'link':{"spotify":results['tracks']['items'][0]['external_urls']['spotify']}}
    except:
        return 

if __name__ == '__main__':
    verifyWebhook()
    app.run(host='localhost', use_reloader=True, debug=True)