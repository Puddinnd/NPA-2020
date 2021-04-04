### Change file name to Secret.py 
public_url = "http://xxx.ngrok.io" # `ngrok http 5000`
bot_token = "..."
my_token = "..."
mapquest_token = "..."
selected_room_id = "..." # RoomID in webex team
webhook_spec = {
    "resource": "messages",
    "event": "created",
    "targetUrl": public_url,
    "name": "WebHook - TEST BOT room",
}

## Youtube 
youtube_api_service_name = "youtube"
youtube_api_version = "v3"
youtube_DEVELOPER_KEY = "..."
### Spotify
spotify_client_id = "..."
spotify_client_secret = "..."