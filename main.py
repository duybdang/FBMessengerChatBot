import random
from flask import Flask
import pymessenger.bot import Bot

app = Flask(__name__)
accessToken = 'ACCESS_TOKEN'
verifyToken = 'VERIFY_TOKEN'
bot = Bot(accessToken)

@app.route('/', methods=['GET', 'POST'])

def receiveMessage():
    if request.method == 'GET':
        tokenSent = request.args.get("hub.verifyToken")
        return verify_fb_token(tokenSent)
    else:
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipientID = message['sender']['id']
                if message['message'].get('text'):
                    responseSentText = getMessage()
                    sendMessage(recipientID, responseSentText)
                if message['message'].get('attachments'):
                    responseSentNonText = getMessage()
                    sendMessage(recipientID, responseSentNonText)
    return "Message Processed"


if __name__ == '__main__':
    app.run()
