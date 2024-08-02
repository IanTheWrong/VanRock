import shelve
import os
import json

class ichimoku():
    def check():
        print("check()")

    def calculate(ticker):
        TenkenSan = 0 #Conversion
        KijunSen = 0 #Base
        SenkouA = 0 #Line A
        SenkouB = 0 #Line B
        ChikouSan = 0 #Lagging
        tempHigh = 0
        tempLow = data['results'][0]['l']
        with open(f"./StockData/{ticker}.json", 'r') as file:
            data = json.load(file)
        for i in range(0,9):
            if(tempHigh < data['results'][i]['h']):
                tempHigh = data['results'][i]['h']
            if(tempLow > data['results'][i]['l']):
                tempLow = data['results'][i]['l']
        TenkenSan = (tempLow+tempHigh)/2
        print(TenkenSan)
        tempLow = data['results'][0]['l']
        tempHigh = 0
        for i in range(0,26):
            if(tempHigh < data['results'][i]['h']):
                tempHigh = data['results'][i]['h']
            if(tempLow > data['results'][i]['l']):
                tempLow = data['results'][i]['l']
        KijunSen = (tempLow+tempHigh)/2
        SenkouA = (KijunSen+TenkenSan)/2
        tempLow = data['results'][0]['l']
        tempHigh = 0
        for i in range(0,52):
            if(tempHigh < data['results'][i]['h']):
                tempHigh = data['results'][i]['h']
            if(tempLow > data['results'][i]['l']):
                tempLow = data['results'][i]['l']
        SenkouB = (tempHigh/tempLow)/2
        ChikouSan = data['results'][0]['c']
        tempLow = 0
        tempHigh = 0

