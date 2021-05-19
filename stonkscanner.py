import numpy as np
import csv
import robin_stocks
from datetime import datetime
from matplotlib import pyplot as plt

tickerlist = [] 
dicts = []

def main():  
    
    robin_stocks.login('wadepe@yahoo.com', 'hW82+4CxWP')
    tickers('nasdaqtickers.csv')
    tickers('nysetickers.csv')
    starttime = datetime.now()
    dictionarys()
    endtime = datetime.now()
    print(starttime)
    print(endtime)
    print('Total time for dictionaries: ', endtime - starttime)

def tickers(symbol): 
    with open(symbol) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            check = robin_stocks.stocks.get_instruments_by_symbols(row[0], info='tradeable')
            if check == [True]:
                tickerlist.append(row[0])

def dictionarys():
    for i in tickerlist:
        dictionary = robin_stocks.stocks.get_fundamentals(i, info=None)
        dicts.append(dictionary)

main()