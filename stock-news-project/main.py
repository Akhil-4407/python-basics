import requests
import os 
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv(".env")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_api_key = os.environ.get("STOCK_API_KEY")
print(os.environ.get("API_KEY"))
PARAMETERS = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":stock_api_key
}
response = requests.get(url=STOCK_ENDPOINT,params=PARAMETERS)
data = response.json()
time_series = data["Time Series (Daily)"]
days = sorted(time_series.keys(),reverse=True)
yesterday = time_series[days[0]]
day_before = time_series[days[1]]
closing_price_difference = abs(float(yesterday["4. close"]) - float(day_before["4. close"]))
percent = round((closing_price_difference/float(yesterday["4. close"]))*100)
print(percent)
if percent>5:
    news_api_key = os.environ.get("NEWS_API_KEY")
    PARAMETERS = {
        "q":COMPANY_NAME,
        "apiKey":news_api_key,
        "language":"en",
        "sortBy": "publishedAt",
        "pageSize": 3
    }
    news_response = requests.get(url=NEWS_ENDPOINT,params=PARAMETERS)
    news = news_response.json()
    articles = news["articles"]
    for i, article in enumerate(articles, start=1):
        acc_sid = os.environ.get("ACC_SID")
        acc_token = os.environ.get("ACC_TOKEN")
        client = Client(acc_sid,acc_token)
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            to='whatsapp:+918977990204',
            body=f"\nArticle {i}:\nTitle:   {article['title']}\nSource:  {article['source']['name']}\nAuthor:  {article['author']}\nPublished: {article['publishedAt']}\nURL:     {article['url']}"
        )