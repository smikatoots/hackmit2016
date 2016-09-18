from flask import Flask, request
import requests
import traceback
import random
import json
import sampleModule

app = Flask(__name__)



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