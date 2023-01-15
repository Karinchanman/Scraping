from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('1KR9QQFNl2gOdvsUTEWHBVgsiS1ZX23eyC4KwHvqiOiHBCRe0K5xEA5flNAeI/f4TMKvql19ZxrNZXLL7vVZdbpNcYYje4JU6J8giPG2AOTYbQd8KJPC2LCtFuQQ/x61iRN7N6UTdn+O/q+hrYT4EQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5251ad1409ab69ac9b7af4addcb33c51')


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature'] 
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run()
