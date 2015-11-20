#credits to bitm0de
import requests
import json

url_vars = {
  'token': 'api-token', #your api-token
  'channel': 'chennel-id', #can be found by channels.list
  'as_user': '1', #0 to post as bot
  'text': 'Chitty is gay.', #message
}

while 0==0: #courtesy of nevermore
    requests.get('https://slack.com/api/chat.postMessage?' + ('&'.join(map('='.join, url_vars.items()))))

