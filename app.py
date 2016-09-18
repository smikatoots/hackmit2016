from flask import Flask, request
import requests
import traceback
import random
import json
import sampleModule

app = Flask(__name__)

# API access
from urllib.request import urlopen
import json

AMADAEUS_KEY = 'TmP45v08vUF28rYQ0AxfVOkM93idify9'

def amadeus_search(origin, destination, departure_date, price, airline):
    api_key = AMADAEUS_KEY
    url = 'https://api.sandbox.amadeus.com/v1.2/flights/inspiration-search?apikey='+ api_key
    if origin != NULL: #if user does not input a destination
        url = url + "&origin=" + origin
    if price != NULL:
        url = url += "&destination=" + destination
    #departure date includes return date and is formatted: yyyy-MM-dd--yyyy-MM-dd (departure date--return date)
    if departure_date != NULL:
        url = url += "&departure_date=" + departure_date
    if price != NULL:
        url = url += "&price=" + price
    if airline != NULL:
        url = url += "&airline=" + airline

    json_obj = urlopen(final_url).read().decode('UTF-8')
    data = json.loads(json_obj)

    for item in data['results']:
        print (item['destination'], item['departure_date'], item['return_date'], item['price'], item['airline'])

#Bot takes user input and parses it

verificationToken = "mozart_verification"
token = "EAAduIpA2oNMBANEb4HonZBtUlE5CBiZAEd2ZCH152NLM4gN9ynFAVHmcaw6Ckif0YDbEwJUwSWppmVN8bJ4I0BCUmBpDkQG0n6KjIlvxyp6882a7X0L69ZCO6Lb0ZAmifQELQSebcdFZAORCzOZCk8Wbuu6wOB8nqE8zF6J0pg8SgZDZD"

loopIndex = 0

verificationToken = "mozart_verification"
token = "EAAduIpA2oNMBANEb4HonZBtUlE5CBiZAEd2ZCH152NLM4gN9ynFAVHmcaw6Ckif0YDbEwJUwSWppmVN8bJ4I0BCUmBpDkQG0n6KjIlvxyp6882a7X0L69ZCO6Lb0ZAmifQELQSebcdFZAORCzOZCk8Wbuu6wOB8nqE8zF6J0pg8SgZDZD"

loopIndex = 0

@app.route('/', methods=['GET', 'POST'])
def webh():
  return "done"

@app.route('/mozart/access', methods=['GET', 'POST'])
def webhook():
  if request.method == 'POST':
    try:
      data = json.loads(request.data.decode("utf-8"))
      text = data['entry'][0]['messaging'][0]['message']['text'] # Incoming Message Text
      sender = data['entry'][0]['messaging'][0]['sender']['id'] # Sender ID
      payload = {'recipient': {'id': sender}, 'message': {'text': "Hello World"}} # We're going to send this back
      message = ""
      if loopIndex == 0:
        message = "Hello Welcome to Mozart Travels! Please enter an origin and destination in the format <origin><destination>! For instance: Chicago,Boston"
        loopIndex++
      if loopIndex == 1:
        message = text
        loopIndex = 0

      payload = {'recipient': {'id': sender}, 'message': {'text': message}} # We're going to send this back

      r = requests.post('https://graph.facebook.com/v2.7/me/messages/?access_token=' + token, json=payload) # Lets send it
    except Exception as e:
      print(traceback.format_exc()) # something went wrong
  elif request.method == 'GET': # For the initial verification
    if request.args.get('hub.verify_token') == verificationToken:
      return request.args.get('hub.challenge')
    return "Wrong Verify Token"
  return "Hello World" #Not Really Necessary

if __name__ == '__main__':
  app.run(debug=True)
