import os
import requests
from datetime import datetime, timedelta
import json

class data():
    def __init__(self):
        self.Stonks = "GME"
        self.APIurl = "https://api.polygon.io/v2/aggs/ticker/"
        self.start_date = datetime.today().date()
        self.end_date = self.start_date -timedelta(days=3)
        self.API_KEY = "cONqvzinqAUbQ0TSqI7MAYOo3hdsf5d8"

    def get(self,ticker):
        url = f"{self.APIurl}{ticker}/range/1/day/{self.end_date}/{self.start_date}?adjusted=true&sort=asc&limit=50000000&apiKey={self.API_KEY}"
        self.response = requests.get(url)
        return self.response.json()

    def load(self):
        self.stonks_json = self.fetch_json_data(self.Stonks)
        return self.stonks_json

    def save(self):
        with open(f"stocks_dataPrices{self.start_date}&{self.end_date}.json", "w") as f:
            json.dump(self.stonks_json, f, indent = 4)
