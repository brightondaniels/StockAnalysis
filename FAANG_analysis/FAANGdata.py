# Import FAANG Data
import os 
import pandas as pd

# Retrieve Data 
ticker = 'FB'
#ticker = 'AAPL'
#ticker = 'AMZN'
#ticker = 'NFLX'
#ticker = 'GOOG'

#path = "/Users/CODEUSR/Documents/PROJECTS/finance/StockAnalysis/FAANG_analysis/data/stocks"
#files = os.listdir(path)

path = os.getcwd()+'/FAANG_analysis/'


files = os.listdir(path+'data/stocks')
stocks = {}
for file in files:
    if file.split('.')[1] == 'csv':
        name = file.split('.')[0]
        stocks[name] = pd.read_csv('data/stocks/'+file, index_col='Date')
        stocks[name].index = pd.to_datetime(stocks[name].index)
print('List of stocks: ', end = ' ')
for i in stocks.keys():
    print(i.upper(), end=' ')
