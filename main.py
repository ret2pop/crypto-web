import requests
import json
from flask import Flask, render_template
import os


app = Flask(__name__)
CURRENCY = os.environ.get('CURRENCY', "BTC")
MARKET = os.environ.get('MARKET', 'EUR')
APIKEY = os.environ.get('APIKEY', '1LQJENC2TRTGR2KS')

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    re = requests.get(f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={CURRENCY}&market={MARKET}&apikey={APIKEY}")
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
# print(data.keys())
