from flask import Flask
import requests
import json

app = Flask(__name__)


@app.route('/<string:x>/<string:y>')
def hello_world(x,y):
    from_cur = x
    to_cur = y
    apikey = 'BA0DSY2O5I5S3ABT'
    payload = {'function' : 'CURRENCY_EXCHANGE_RATE','from_currency':from_cur,'to_currency': to_cur, 'apikey':apikey}
    try:
        r = requests.get("https://www.alphavantage.co/query",params = payload)
        print(r.status_code)
        data = json.loads(r.text)['Realtime Currency Exchange Rate']
        rate = data['5. Exchange Rate']
        from_currency = data['2. From_Currency Name']
        to_currency = data['4. To_Currency Name']
        msg = {'data' :str(rate), 'from currency' : from_currency, 'to currency' : to_currency}
        return json.dumps(msg),200
    except KeyError:
        msg = {'Error message' :'wrong currencies'}
        return json.dumps(msg),403



if __name__ == '__main__':
    app.run()
