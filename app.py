from flask import Flask, render_template
import requests, json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

price_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&\
                include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false"
response = requests.get(price_url)
response = response.json()
bitcoin_price = response['bitcoin']['usd']
print(type(bitcoin_price))
print(bitcoin_price)

if __name__ == '__main__':
    app.run(debug=True)
