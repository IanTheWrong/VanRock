import shelve
import os
import time
import logging
from data import data
from ichimoku import ichimoku
while True:
    open('final.txt','w').close()
    ichimoku.calculate()
    data.get(900)


