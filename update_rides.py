from stravalib import Client
import os
import requests

client = Client()
authorization_url = client.authorization_url(client_id=16055, redirect_uri='http://localhost:8282/authorized')
resp = requests.get(authorization_url)

# grab and authorization code
code = response.get('code')
access_token = client.exchange_code_for_token(client_id=16055, client_secret=os.environ['STRAVA_CLIENT_SECRET'], code=code)
client.access_token = access_token

for activity in client.get_activities(after = "2016-01-01T00:00:00Z", limit=1):
    a = activity
    print("{0.name} {0.moving_time} {0.gear_id} {0.gear.name}".format(activity))
