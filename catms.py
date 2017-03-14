''' get sms from a cat '''
from flask import Flask, request
import random
from twilio.rest import TwilioRestClient
import settings

app = Flask(__name__)
base_url = settings.BASE_URL

account_sid = settings.TWILIO_SID
auth_token = settings.TWILIO_TOKEN
number = settings.TWILIO_NUMBER
client = TwilioRestClient(account_sid, auth_token)

@app.route(base_url, methods=['POST'])
def receive_sms():
    ''' accept sms via twilio '''
    sender = request.form['From']
    body = meow()
    client.messages.create(body=body, to=sender, from_=number)
    return body


@app.route(base_url, methods=['GET'])
def web_responder():
    ''' display a response at the http endpoint in browser '''
    return meow()


def meow():
    ''' the cat's response '''
    return 'm' * random.randint(1, 4) + \
           'r' * random.randint(2, 8) + \
           'o' * random.randint(1, 9) + \
           'w'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3333)
