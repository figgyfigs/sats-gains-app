from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    submit = False
    final_price = "___"
    final_percent = "___"
    
    if request.method == "POST":
        amount_paid = request.form['amount']
        sats_earned = request.form['sats']
        format_sats = convert_to_dec(sats_earned)
        bitcoin_price = get_price()

        #current fiat price of the sats earned
        fiat_worth = round(bitcoin_price * format_sats, 2)
        percent = round(calc_percent_gain(float(amount_paid), fiat_worth))
        display_price = round(calc_bitcoin_price(bitcoin_price, percent))
        submit = True
        final_price = str(display_price)
        final_percent = str(percent)
    return render_template('index.html', submit=submit, price=final_price, percent=final_percent)

#dollar percentage increase
#parameters needed: amount the user paid and current price of the sats sats_earned
#FORMULA: % increase = 100 x ((final * initial) / initial)
def calc_percent_gain(final, initial):
    print(final, initial)
    percentage_gain = ((final - initial) / initial)
    return (percentage_gain - 1) * 100


def calc_bitcoin_price(price, percentage):
    #convert percentage to decimal
    print(percentage)
    dec = percentage / 100
    print(dec)
    future_price = price * dec
    return future_price


#converts sats to decimal equivalent (i.e 8 decimal places)
# 2345 -> 0.00002345
def convert_to_dec(sats):
    pre_str = "0."
    post_str = sats.zfill(8)
    amount = pre_str + post_str
    return float(amount)

def get_price():
    price_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&\
                    include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false"
    response = requests.get(price_url)
    response = response.json()
    bitcoin_price = response['bitcoin']['usd']
    return bitcoin_price

if __name__ == '__main__':
    app.run(debug=True)
