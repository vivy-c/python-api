import requests
import json

#https://api.stackexchange.com/
response = requests.get(
    'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow'
)

print(response.json()['items'])