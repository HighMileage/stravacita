from stravalib import Client
import os
import requests

client = Client()
# Run the lines below and then follow the line and grant access
# Set the response code as the env variable STRAVA_CODE_WRITE
# authorization_url = client.authorization_url(client_id=16055, redirect_uri='http://localhost:8282/authorized', scope='write')

access_token = client.exchange_code_for_token(client_id=16055, client_secret=os.environ['STRAVA_CLIENT_SECRET'], code=os.environ['STRAVA_CODE_WRITE'])
client.access_token = access_token

for activity in client.get_activities(after = "2016-01-01T00:00:00Z"):
    if activity.name in ['Evening Ride', 'Morning Ride'] and activity.gear_id == 'b249182' and activity.distance.num < 10000:
        print("Updating {0.id} from gear_id {0.gear_id} to 'b352561'").format(activity)
        client.update_activity(activity.id, gear_id='b352561')
    else:
        print("Not updating ride {0.id} {0.name} {0.moving_time} {0.start_date} {0.gear_id} {0.distance}".format(activity))
