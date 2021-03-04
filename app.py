from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        amount_paid = request.form['amount']
        sats_earned = request.form['sats']
        format_sats = convert_to_dec(sats_earned)
        price_of_bitcoin = get_price()

        #current fiat price of the sats earned
        fiat_worth = price_of_bitcoin * format_sats
        print(round(fiat_worth, 2))
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
    pre_str = "0."
    post_str = sats.zfill(8)
    amount = pre_str + post_str
    return float(amount)


#get_price()

if __name__ == '__main__':
    app.run(debug=True)
