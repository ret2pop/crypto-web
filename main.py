import requests
import json
from flask import Flask, render_template
import os


app = Flask(__name__)
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './secret/apikey.txt')

with open(filename, "r") as f:
    apikey = f.read()
CURRENCY = os.environ.get('CURRENCY', "BTC").strip()
MARKET = os.environ.get('MARKET', 'EUR').strip()
APIKEY = os.environ.get('APIKEY', apikey).strip() # don't actually use the environ.get; use a k8s secret
print(MARKET)
print(CURRENCY)

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    re = requests.get(f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={CURRENCY}&market={MARKET}&apikey={APIKEY}")

    if 'Information' in re.json():
        return "<h1>ERROR</h1><p>API key request limit exceeded</p>"

    data = re.json()['Time Series (Digital Currency Daily)'].items()
    string = "<h1>Historical Time Series (BTC)</h1><ul>"
    for item in data:
        date = item[0]
        usedata = item[1]
        single_entry = f"<li>{date}: open: {usedata['1. open']}, close: {usedata['4. close']}</li>"
        string += single_entry
    string += "</ul>"
    return render_template('index.html', string=string)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8888)
