import shelve
import os
import json
filepath = "./tickers.txt"
stocks = []
vars = shelve.open('BalanceSheet')
with open(filepath, 'r') as file:
    content = file.read()
    stocks = content.splitlines()
class ichimoku():
    def calculate():
        for ticker in stocks:
            TenkenSan = 0 #Conversion
            KijunSen = 0 #Base
            SenkouA = 0 #Line A
            SenkouB = 0 #Line B
            ChikouSan = 0 #Lagging
            tempHigh = 0
            pastA = 0
            with open(f"./StockData/{ticker}.json", 'r') as file:
                data = json.load(file)
            tempLow = data['results'][0]['l']
            for i in range(0,9):
                if(tempHigh < data['results'][i]['h']):
                    tempHigh = data['results'][i]['h']
                if(tempLow > data['results'][i]['l']):
                    tempLow = data['results'][i]['l']
            TenkenSan = (tempLow+tempHigh)/2
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
            SenkouB = (tempHigh+tempLow)/2
            ChikouSan = data['results'][0]['c']
            tempLow = 0
            tempHigh = 0
            #buy
            if(TenkenSan > KijunSen and SenkouA > SenkouB and ChikouSan > SenkouA and vars[f'{ticker}position'] == 1 and vars['Balance'] >= 500):
                vars['Balance'] -= 500
                vars[f"{ticker}amt"] = 500/data['results'][0]['c']
                vars[f'{ticker}bottom'] = SenkouB
                vars[f'{ticker}position'] = 2
                vars[f'{ticker}top'] = (ChikouSan-SenkouB)+ChikouSan
                print("long at", data['results'][0]['c'], f"on {ticker}", "for", vars[f"{ticker}amt"], "shares", vars['Balance'], "remaining")
            #sell
            elif(TenkenSan < KijunSen and SenkouA < SenkouB and ChikouSan < SenkouA and vars[f'{ticker}position'] == 1 and vars['Balance'] >= 500):
                vars['Balance'] -= 500
                vars[f"{ticker}amt"] = 500/data['results'][0]['c']
                vars[f'{ticker}top'] = SenkouB
                vars[f'{ticker}position'] = 0
                vars[f'{ticker}bottom'] = (ChikouSan-SenkouB)+ChikouSan
                print("short at", data['results'][0]['c'], f"on {ticker}", "for", vars[f"{ticker}amt"], "shares", vars['Balance'], "remaining")
            #top sell stop
            elif(vars[f'{ticker}position'] == 2 and data['results'][0]['c'] > vars[f'{ticker}top'] and vars[f'{ticker}top'] != -1):
                vars['Balance'] += data['results'][0]['c'] * vars[f"{ticker}amt"]
                vars[f'{ticker}position'] = 1
                vars[f'{ticker}top'] = -1
                vars[f'{ticker}bottom'] = -1
                vars[f"{ticker}amt"] = 0
            #bottom sell stop
            elif(vars[f'{ticker}position'] == 2 and data['results'][0]['c'] < vars[f'{ticker}bottom'] and vars[f'{ticker}top'] != -1):
                vars['Balance'] += data['results'][0]['c'] * vars[f"{ticker}amt"]
                vars[f'{ticker}position'] = 1
                vars[f'{ticker}top'] = -1
                vars[f'{ticker}bottom'] = -1
                vars[f"{ticker}amt"] = 0
            #top sell sell stop
            if(vars[f'{ticker}position'] == 0 and data['results'][0]['c'] < vars[f'{ticker}top'] and vars[f'{ticker}top'] != -1):
                vars['Balance'] += data['results'][0]['c'] * vars[f"{ticker}amt"] + vars[f"{ticker}amt"]
                vars[f'{ticker}position'] = 1
                vars[f'{ticker}top'] = -1
                vars[f'{ticker}bottom'] = -1
                vars[f"{ticker}amt"] = 0
            elif(vars[f'{ticker}position'] == 0 and data['results'][0]['c'] > vars[f'{ticker}bottom'] and vars[f'{ticker}top'] != -1):
                vars['Balance'] += vars[f"{ticker}amt"] - (data['results'][0]['c'] * vars[f"{ticker}amt"])
                vars[f'{ticker}position'] = 1
                vars[f'{ticker}top'] = -1
                vars[f'{ticker}bottom'] = -1
                vars[f"{ticker}amt"] = 0



            
            
        

