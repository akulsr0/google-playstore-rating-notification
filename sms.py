import os
from twilio.rest import Client
from dotenv import load_dotenv


def sendSMS(current_rating, updated_rating):
    load_dotenv()

    account_sid = os.getenv('account_sid')
    auth_token = os.getenv('auth_token')
    client = Client(account_sid, auth_token)

    sender_phone = os.getenv('sender_phone')
    target_phone = os.getenv('target_phone')

    diff = updated_rating - current_rating

    sms_text = 'You have got {} new rating on React Native UI app, Google Playstore.'.format(
        diff)

    sent_msg = client.messages.create(
        to=target_phone,
        from_=sender_phone,
        body=sms_text
    )
