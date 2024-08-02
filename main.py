import shelve
import os
import time
import logging
exists = False
# Position 0 is Sell Order
# Position 1 is Hold Money
# Position 2 is Buy Order
filepath = "./tickers.txt"
stocks = []
with open(filepath, 'r') as file:
    content = file.read()
    stocks = content.splitlines()
for filename in os.listdir("./"):
    if filename == "BalanceSheet.dir":
        exists = True
        break
if not exists:
    vars = shelve.open('BalanceSheet')
    vars['Balance'] = 500000
    for ticker in stocks:
        vars[f"{ticker}position"] = 1
        vars[f"{ticker}top"] = -1
        vars[f"{ticker}bottom"] = -1
        vars[f"{ticker}amt"] = 0
from data import data
from ichimoku import ichimoku
while True:
    #data.get(100)
    ichimoku.calculate()
    time.sleep(65)

