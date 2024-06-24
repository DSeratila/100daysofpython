import requests

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_NAME = "TSLA"
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
NEWS_API_KEY = 'd543e8c31da54eeb95a32b61955efe63'
COMPANY_NAME = "TESLA"

with open("api_key", "r") as file:
    STOCK_API_KEY = file.read()

print(STOCK_API_KEY)

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params).json()
data = response["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterdays_closing_price = float(data_list[0]["4. close"])
print(yesterdays_closing_price)

day_before_yesterdays_closing_price = float(data_list[1]["4. close"])
print(day_before_yesterdays_closing_price)

diff = abs(yesterdays_closing_price - day_before_yesterdays_closing_price)
diff_prc = (diff/yesterdays_closing_price)*100
print(round(diff_prc, 2))

if diff_prc > 0:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params).json()
    articles = news_response["articles"][:2]
    print(articles)
