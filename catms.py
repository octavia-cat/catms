''' get sms from a cat '''
from flask import Flask, request
import re
from random import choice, randint, sample
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
    body = meow(request.form['Body'])
    client.messages.create(body=body, to=sender, from_=number)
    return body


@app.route(base_url, methods=['GET'])
def web_responder():
    ''' display a response at the http endpoint in browser '''
    return meow()


def meow(message=u''):
    ''' the cat's response '''

    responses = {
        r'.*\bselfie\b.*': u'\U0001F431',
        r'.*are you a [cat|kitty|kitling|kitten].*': u'\U0001F431' * 3,
        r'.*I (love|\u2764) you.*': u'{meow} \u2764'
    }

    reply = '{meow}'

    if len(message) > 3:
        for (regex, response) in responses.items():
            if re.match(regex, message, re.IGNORECASE):
                reply = response
                break

    meows = [
        'm' * randint(1, 2) + 'r' * randint(2, 8) + 'o' * randint(1, 10) + 'w',
        'a' * randint(3, 9) + 'e' * randint(2, 6),
        'merp' + ' erp' * randint(0, 3),
        'e' * randint(3, 5) + 'a' * randint(1, 5) + 'wwr' + 'a' * randint(2, 5),
        'm' + 'e' * randint(2, 7) + 'p',
        'mrp mir mrr' + 'e' * randint(3, 6) + 'p',
        'm' + 'r' * randint(5, 10),
        'a' * randint(1, 3) + 'ww' + 'r' * randint(3, 5) + 'a' * randint(2, 10),
        'm' + 'rm' * randint(3, 6),
        'h' + 'r' * randint(1, 7) + 'mmram',
        'snxr' + 'x' * randint(1, 3),
    ] * 4 + [
        u'\U0001F431',
        u'\U0001F640',
        u'\U0001F638',
    ] * 3 + [
        u'\u2049',
        u'\u203C',
    ] * 2 + [
        u'\u260E',
        u'\U0001F331',
        u'\U0001F41F',
        u'\U0001F480',
        u'\U0001F4A3',
        u'\U0001F4A4',
        u'\U0001F4B0',
        u'\U0001F408',
    ]

    meow_reply = ' '.join(sample(meows, choice([1, 2, 2, 3, 4])))
    reply = re.sub(r'{meow}', meow_reply, reply)

    return reply

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3333)
