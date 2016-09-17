from flask import Flask
import requests
import sampleModule

app = Flask(__name__)

def getKeys(path):
    with open(path) as f:
        contents = f.readlines()
        return contents

verificationToken = getKeys("config/secrets")[0]
pageAccessToken = getKeys("config/secrets")[1]

@app.route("/mozart/test", methods=["GET"])
def processTest():
    return "done"

@app.route("/mozart/access", methods=["GET"])
def process():
    if request.args.get("hub.verify_token", "") == verificationToken:
        return request.args.get("hub.challenge", "")
    else:
        return "Error, wrong validation token"


@app.route('/mozart/access', methods=['POST'])
def handle_messages():
    payload = request.get_data()
    print(payload)
    for sender, message in process_events(payload):
        print("Incoming from %s: %s" % (sender, message))
        send_message(pageAccessToken, sender, message)
    return "ok"

def process_events(payload):
    data = json.loads(payload)
    events = data["event"][0]["messaging"]
    for event in events:
        if "message" in event and "text" in event["message"]:
            yield event["sender"]["id"], event["message"]["text"].encode('unicode_escape')
        else:
            yield event["sender"]["id"], "I can't echo this" 

def send_message(token, recipient, text):
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
    params={"access_token": token},
    data=json.dumps({
        "recipient": {"id": recipient},
        "message": {"text": text.decode('unicode_escape')}
    }),
    headers={'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        print(r.text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
    