from flask import Flask, request
import requests
import traceback
import random
import json
import sampleModule

app = Flask(__name__)

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