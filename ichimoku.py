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
            TenkenSen = 0 #Conversion
            KijunSen = 0 #Base
            SenkouA = 0 #Line A
            SenkouB = 0 #Line B
            ChikouSen = 0 #Lagging
            tempHigh = 0
            pastSenkouA = 0
            pastSenkouB = 0
            pastTenkenSen = 0
            PastKijunSen = 0
            with open(f"./StockData/{ticker}.json", 'r') as file:
                data = json.load(file)

            #TenkenSen
            tempLow = data['results'][0]['l']
            for i in range(0,9):
                if(tempHigh < data['results'][i]['h']):
                    tempHigh = data['results'][i]['h']
                if(tempLow > data['results'][i]['l']):
                    tempLow = data['results'][i]['l']
            TenkenSen = (tempLow+tempHigh)/2
            tempLow = data['results'][0]['l']
            tempHigh = 0

            #PastTenkenSen
            for i in range(26,36):
                if(tempHigh < data['results'][i]['h']):
                    tempHigh = data['results'][i]['h']
                if(tempLow > data['results'][i]['l']):
                    tempLow = data['results'][i]['l']
            pastTenkenSen = (tempLow+tempHigh)/2
            tempLow = data['results'][0]['l']
            tempHigh = 0

            #KijunSen + SenkouA
            for x in range(0,26):
                if(tempHigh < data['results'][x]['h']):
                    tempHigh = data['results'][x]['h']
                if(tempLow > data['results'][x]['l']):
                    tempLow = data['results'][x]['l']
            KijunSen = (tempLow+tempHigh)/2
            SenkouA = (KijunSen+TenkenSen)/2
            tempLow = data['results'][0]['l']
            tempHigh = 0

            #PastKijun + PastSenkouA
            for x in range(26,43):
                if(tempHigh < data['results'][x]['h']):
                    tempHigh = data['results'][x]['h']
                if(tempLow > data['results'][x]['l']):
                    tempLow = data['results'][x]['l']
            pastKijunSen = (tempLow+tempHigh)/2
            pastSenkouA = (pastKijunSen+pastTenkenSen)/2
            tempLow = data['results'][0]['l']
            tempHigh = 0

            #SenkouB
            for f in range(0,52):
                if(tempHigh < data['results'][f]['h']):
                    tempHigh = data['results'][f]['h']
                if(tempLow > data['results'][f]['l']):
                    tempLow = data['results'][f]['l']
            SenkouB = (tempHigh+tempLow)/2

            #PastSenkouB
            for f in range(26,79):
                if(tempHigh < data['results'][f]['h']):
                    tempHigh = data['results'][f]['h']
                if(tempLow > data['results'][f]['l']):
                    tempLow = data['results'][f]['l']
            pastSenkouB = (tempHigh+tempLow)/2
            ChikouSen = data['results'][0]['c']
            tempLow = 0
            tempHigh = 0
            #buy
            bottom = pastSenkouA
            top = pastSenkouA
            if(pastSenkouB < pastSenkouA):
                bottom = pastSenkouB
                top = pastSenkouA
            if(TenkenSen > KijunSen and SenkouA > SenkouB and ChikouSen > pastSenkouA and ChikouSen > pastSenkouB):
                print("long at", data['results'][0]['c'], f"on {ticker}")
                with open("results.txt", 'a') as file:
                    if(ChikouSen * .95 <= top):
                        file.write(f"----------LONG {ticker} LOSS @ {bottom} LIMIT @ {round((ChikouSen-bottom)*2 + ChikouSen, 2)}\n")
                    else:
                        file.write(f"LONG {ticker} LOSS @ {bottom} LIMIT @ {round((ChikouSen-bottom)*2 + ChikouSen, 2)}\n")
            #sell
            elif(TenkenSen < KijunSen and SenkouA < SenkouB and ChikouSen < pastSenkouA and ChikouSen < pastSenkouB):
                with open("results.txt", 'a') as file:
                    if(ChikouSen * 1.05 >= bottom):
                        file.write(f"----------SHORT {ticker} LOSS @ {top} LIMIT @ {round((ChikouSen-top)*2 + ChikouSen, 2)}\n")
                    else:
                        file.write(f"SHORT {ticker} LOSS @ {top} LIMIT @ {round((ChikouSen-top)*2 + ChikouSen, 2)}\n")
            
            
        

