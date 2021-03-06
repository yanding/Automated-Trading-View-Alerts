import time, requests
from flask import Flask, request
from handler import *

app = Flask(__name__)

def get_timestamp():
    timestamp = time.strftime("%Y-%m-%d %X")
    return timestamp

def send_alert(data):
    requests.get(f'https://api.telegram.org/bot1856106907:AAFdAj1zCgzibrd7UrBF1WQJXh8iRxMG1Tc/sendMessage?chat_id=-1001507765005&text={str(data)}')

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
                if (data['action'] == 'buy' or data['action'] == 'BUY'):
                    MainTradeData = f'š šš”šš¢š šš”š šššš„š§\n\nš š²ššš®š“š²: š¢ {str(messageDat)}\nššš°šµš®š»š“š²: {str(exchangeDat)}\nšš°šš¶š¼š»: {str(actionDat)}\nš§š¶š°šøš²šæ: {str(tickerDat)}\nš©š¼š¹ššŗš²: {str(volumeDat)}\nš£šæš¶š°š²: {str(priceDat)}\nš§š¶šŗš²: {str(timeDat)}\n\nššš§š š¦š¢šš§šŖšš„š šØš”ššš„ ššš©ššš¢š£š šš”š§'
                else:
                    MainTradeData = f'š šš”šš¢š šš”š šššš„š§\n\nš š²ššš®š“š²: š  {str(messageDat)}\nššš°šµš®š»š“š²: {str(exchangeDat)}\nšš°šš¶š¼š»: {str(actionDat)}\nš§š¶š°šøš²šæ: {str(tickerDat)}\nš©š¼š¹ššŗš²: {str(volumeDat)}\nš£šæš¶š°š²: {str(priceDat)}\nš§š¶šŗš²: {str(timeDat)}\n\nššš§š š¦š¢šš§šŖšš„š šØš”ššš„ ššš©ššš¢š£š šš”š§'
                send_alert(MainTradeData)
                return "ALERT SENT SUCCESS", 200
            else:
                return "REQUEST REFUSED", 400
    except Exception as e:
        return "EXCEPTION ERROR ENCOUNTERED", 400
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=80)
