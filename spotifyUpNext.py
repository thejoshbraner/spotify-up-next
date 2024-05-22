import requests
from dotenv import load_dotenv
import os
from requests.auth import HTTPBasicAuth


load_dotenv()

client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

get_token_url = 'https://accounts.spotify.com/api/token'
get_recent_url = 'https://api.spotify.com/v1/me/player/recently-played'


get_auth = requests.post(get_token_url, {'grant_type': 'client_credentials'}
                                         , auth=HTTPBasicAuth(client_id, client_secret))
if get_auth.status_code == 200:
    access_token = get_auth.json().get('access_token')
    print(access_token)
else:
    print(f'Error: {get_auth.status_code}')

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

response = requests.get(get_recent_url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}')
