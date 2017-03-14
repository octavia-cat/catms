''' get sms from a cat '''
from flask import Flask, request
from twilio.rest import TwilioRestClient
import settings

app = Flask(__name__)

account_sid = settings.TWILIO_SID
auth_token = settings.TWILIO_TOKEN
number = settings.TWILIO_NUMBER
client = TwilioRestClient(account_sid, auth_token)

@app.route('/', methods=['POST'])
def receive_sms():
    ''' accept sms via twilio '''
    sender = request.form['From']
    client.message.create(body=meow(), to=sender, from_=number)


@app.route('/', methods=['GET'])
def web_responder():
    ''' display a response at the http endpoint in browser '''
    return meow()


def meow():
    ''' the cat's response '''
    return 'mrrrow'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3333)
