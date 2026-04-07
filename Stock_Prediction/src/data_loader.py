import yfinance as yf
import pandas as pd

def load_stock_data(ticker, period="5y"):
    data = yf.download(ticker, period=period)
    data = data[["Close"]]
    data.dropna(inplace=True)
    return data