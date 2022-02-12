from flask import Flask, request
from telegram import telegram_bot

app = Flask(__name__)


@app.route('/', method=["GET", "POST"])
def index():
    return "Hello World!"



@app.route("/tradingview", methods=["GET", "POST"])
def tradingview():
    json_data = request.json()
    symbol = str(json_data["symbol"])
    price = str(json_data["price"])
    message = symbol + ": " + price
    telegram_bot(message)
    return message



if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)