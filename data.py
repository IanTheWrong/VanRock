import json
from dotenv import load_dotenv
import os
from datetime import date
from datetime import timedelta
import requests
import time
load_dotenv()
key = os.getenv("API")
filepath = "./tickers.txt"
stocks = []
with open(filepath, 'r') as file:
    content = file.read()
    stocks = content.splitlines()

class data():
    
    def get(timePast):
        today = date.today()
        start = today - timedelta(days=timePast)
        i = 0
        for ticker in stocks:
            i += 1
            response = requests.get(f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{start}/{today}?sort=desc&apiKey={key}").json()
            with open(f"./StockData/{ticker}.json", 'w') as file:
                json.dump(response, file, indent=4)
            if i % 5 == 0:
                print(i, " done")
                time.sleep(65)