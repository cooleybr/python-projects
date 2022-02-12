from flask import Flask
from pymongo import MongoClient
import requests

app = Flask(__name__)
app_cert = '/app/certs/client.pem'
app_key = '/app/certs/client.key'
app_ca = '/app/certs/ca.pem'


@app.route('/')
def index():
  return "client"

@app.route('/test')
def test():
  resp = requests.get('https://server:5000/', cert=(app_cert, app_key), verify=app_ca)
  return resp.text

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=6000)
