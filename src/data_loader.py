import pandas as pd
import yfinance as yf

def load_sp500_changes(path):
    return pd.read_csv(path)

def fetch_price_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    return data[['Open', 'High', 'Low', 'Close', 'Volume']]

def get_event_window_data(ticker, event_date, window=30):
    start = pd.to_datetime(event_date) - pd.Timedelta(days=window)
    end = pd.to_datetime(event_date) + pd.Timedelta(days=window)
    return fetch_price_data(ticker, start, end)
