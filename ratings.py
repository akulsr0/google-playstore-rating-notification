from bs4 import *
import requests as rq


def getUpdatedRating():
    app_url = 'https://play.google.com/store/apps/details?id=com.akul.reactnativeui&hl=en-GB'
    app_html = rq.get(app_url).text

    soup = BeautifulSoup(app_html, 'html.parser')

    updated_rating_soup = soup.find("span", class_="AYi5wd TBRnV")
    updated_rating_str = updated_rating_soup.contents[0].text
    updated_rating = int(updated_rating_str)
    return updated_rating
