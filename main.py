from data import data
from ichimoku import ichimoku
import shelve
import os
import time
import logging
exists = False
# Position 0 is Sell Order
# Position 1 is Hold Money
# Position 2 is Buy Order

for filename in os.listdir("./"):
    if filename == "variables.dir":
        exists = True
        break
if not exists:
    vars = shelve.open('variables')
    vars['Balance'] = 500000

while True:
    logging.info("Refreshed")
    ichimoku.calculate("AMD")
    time.sleep(65)

