import pandas_datareader.data as web
import yfinance as yf
from datetime import datetime
import pandas as pd
import numpy as np
from scipy.stats import norm

# Interval of Interested Data
start = datetime(2020,1,1)
end = datetime(2021,1,1)

# Downloading the data into a dataframe
def fetch_data(ticker):
    string = ticker.upper()
    ticker = yf.download(string, start, end)
    return ticker

# Setting the variables for d1 and d2 for the Black-Scholes Formula
def d1(S, K, r, vol, t):
    return (np.log(S/K) + (r + np.square(vol)/2)*t)/(np.sqrt(t)*vol) 

def d2(d1, vol, t):
    return d1 - (vol*np.sqrt(t))

# Black-Scholes Formula:
def bs(S, K, r, vol, t):
    d_1 = d1(S, K, r, vol, t)
    d_2 = d2(d_1, vol, t)

    call = S*norm(d_1) - (K * (np.e)**(-r*t)*norm(d_2))
    put = K * (np.e)**(-r*t)*norm(-d_2) - S*norm(-d_1)

    return put, call
    


d_1 = d1(100, 100, 0.05, 0.2, 1) # Should equal 0.35
print(d_1) 
d_2 = d2(d_1, 0.2, 1)
print(d_2)
aapl = fetch_data('aapl')
googl = fetch_data('googl')     # Should equal 0.15

# aapl = yf.download('AAPL', start, end)
# print(f"aapl type:{type(aapl)}")

# aapl
print(aapl.head())
print(aapl.size)
print(aapl.shape)
print(aapl.columns)


# googl
# print(googl.head())
# print(googl.size)
# print(googl.shape)


