import yfinance as yf
import datascience
import numpy as np
import pandas as pd
import matplotlib
#%matplotlib inline




#todo list
#get stock 
#plot stock 
#do montecarlo simulation 

def getStockData(stockName,start_date = '2021-01-01',end_date='2021-07-12'):
    print('Recuperando info')
    return yf.download(stockName, start_date, end_date)


def main():
    inicio='1990-01-01'
    fin='2021-07-12'
    nombreStock = 'AMZN'
    stock=getStockData(nombreStock)
    #print(stock)

main()