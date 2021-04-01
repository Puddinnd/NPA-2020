### Change file name to Secret.py 
public_url = "http://xxx.ngrok.io" # `ngrok http 5000`
bot_token = "..."
my_token = "..."
mapquest_token = "..."
selected_room_id = "..." # room in webex team
webhook_spec = {
    "resource": "messages",
    "event": "created",
    "targetUrl": public_url,
    "name": "WebHook - TEST BOT room",
}
