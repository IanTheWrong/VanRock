import shelve
import os
import time
import logging
from data import data
from ichimoku import ichimoku
while True:
    data.get(900)
    open('results.txt', 'w').close()
    ichimoku.calculate()


