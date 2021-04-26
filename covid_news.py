# Webscrapper for cp24 for covid related local news

import requests
from bs4 import BeautifulSoup

from send_email import send_email

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}
# The user-agent identifies the information of browser and os from executed request
url = "https://www.cp24.com/news"
link = requests.get(url, headers=headers)

soup = BeautifulSoup(link.text, "html.parser")
covid_news = []

for title in soup.find_all("h2", {"class": "teaserTitle"}):
    urls = [x["href"] for x in title.find_all("a", href=True)]
    news = title.get_text()

    if "COVID" in news and urls:
        covid_news = news, urls
        
        message = "Subject: New covid news!\n\n"
        message += f"{covid_news}\n"
        send_email(message)
