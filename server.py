from flask import Flask
import requests

app = Flask(__name__)

@app.route("/mozart/access", methods=["GET"])
def process():
    return "hello"

def getKeys(path):
    with open(path) as f:
        contents = f.readlines()
        if len(contents) > 0:
            return contents[0]
        else:
            return ""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
