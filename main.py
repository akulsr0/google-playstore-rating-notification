from ratings import getUpdatedRating
from sms import sendSMS
import schedule
import time

current_rating = 0


def main():
    updated_rating = getUpdatedRating()
    global current_rating
    if current_rating != updated_rating:
        sendSMS(current_rating, updated_rating)
        current_rating = updated_rating


schedule.every(30).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
