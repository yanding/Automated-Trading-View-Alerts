import json, time, config, requests
from flask import Flask, request
from handler import *

app = Flask(__name__)

def get_timestamp():
    timestamp = time.strftime("%Y-%m-%d %X")
    return timestamp

def send_alert(data):
    Message = f'🔘 𝗜𝗡𝗖𝗢𝗠𝗜𝗡𝗚 𝗔𝗟𝗘𝗥𝗧\n\n{str(data)}'
    requests.get(f'https://api.telegram.org/bot<TOKEN>/sendMessage?chat_id=<CHAT OR GRP ID>&text={str(Message)}')

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        if request.method == "POST":
            data = request.get_json()
            key = data["key"]
            if key == 'JC8TwHCH86':
                messageDat = data['message']
                exchangeDat = data['exchange']
                actionDat = data['action']
                tickerDat = data['ticker']
                volumeDat = data['volume']
                priceDat = data['price']
                timeDat = data['time']
                MainTradeData = f'🔘 𝗜𝗡𝗖𝗢𝗠𝗜𝗡𝗚 𝗔𝗟𝗘𝗥𝗧\n\n𝗠𝗲𝘀𝘀𝗮𝗴𝗲: {str(messageDat)}\n𝗘𝘅𝗰𝗵𝗮𝗻𝗴𝗲: {str(exchangeDat)}\n𝗔𝗰𝘁𝗶𝗼𝗻: {str(actionDat)}\n𝗧𝗶𝗰𝗸𝗲𝗿: {str(tickerDat)}\n𝗩𝗼𝗹𝘂𝗺𝗲: {str(volumeDat)}\n𝗣𝗿𝗶𝗰𝗲: {str(priceDat)}\n𝗧𝗶𝗺𝗲: {str(timeDat)}\n\n𝗕𝗘𝗧𝗔 𝗦𝗢𝗙𝗧𝗪𝗔𝗥𝗘 𝗨𝗡𝗗𝗘𝗥 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗠𝗘𝗡𝗧'
                send_alert(MainTradeData)
                return "ALERT SENT SUCCESS", 200
            else:
                return "REQUEST REFUSED", 400

    except Exception as e:
        return "EXCEPTION ERROR ENCOUNTERED", 400

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=80)
