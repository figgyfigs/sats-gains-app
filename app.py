from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        user_amount = request.form['amount']
        sats_back = request.form['sats']
        print(type(sats_back))
        price = get_price()
        print("The user spent: " + user_amount + " and got " + sats_back + " in sats back." + " The current price of bitcoin is " + str(price))
        print("test" + str(convert_to_dec(sats_back)))
    return render_template('index.html')

def get_price():
    price_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&\
                    include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false"
    response = requests.get(price_url)
    response = response.json()
    bitcoin_price = response['bitcoin']['usd']
    return bitcoin_price

def calculate_percent():
    pass

#converts sats to decimal equivalent (i.e 8 decimal places)
# 2345 -> 0.00002345
def convert_to_dec(sats):
    second_str = sats.zfill(8)
    btc = "0." + second_str
    print(int(btc))


get_price()

if __name__ == '__main__':
    app.run(debug=True)
