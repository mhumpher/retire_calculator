#############################################################
#Temporary fix for datareader until fixed for new Google API
from pandas_datareader.google.daily import GoogleDailyReader

@property
def url(self):
    return 'http://finance.google.com/finance/historical'

GoogleDailyReader.url = url
#############################################################

# get data
import pandas as pd
import pandas_datareader as pdr
import numpy as np
from datetime import datetime

#Includes for data load
tickers = ['SPY', 'BND', 'TLT']
start = datetime(2017,1,1)

#Calculate returns and add ticker symbol
tck = tickers[0]
data = pdr.get_data_google(tck, start)
returns = ((data['Close'][1:]-data['Close'].shift(1))/data['Close'][1:])[1:]
returns = returns.to_frame()
data['ticker'] = tck
returns['ticker'] = tck

for tck in tickers[1:]:
    temp = pdr.get_data_google(tck, start)
    temp['ticker'] = tck
    data = data.append(temp)
    temp = ((temp['Close'][1:]-temp['Close'].shift(1))/temp['Close'][1:])[1:]
    temp = temp.to_frame()
    temp['ticker'] = tck
    returns = returns.append(temp)
