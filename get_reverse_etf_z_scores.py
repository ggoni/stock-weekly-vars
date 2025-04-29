import yfinance as yf
import pandas as pd
import numpy as np

# List of reverse ETF tickers
REVERSE_ETFS = [
    "SQQQ", "SH", "PSQ", "SPXU", "SOXS", "SDS", "SPXS", "TSLQ", "TZA",
    "YANG", "QID", "RWM", "SDOW", "SPDN", "FNGD", "DOG", "FAZ", "TECS",
    "SRTY", "DUST", "NRGD", "DXD", "JDST", "HDGE", "TWM"
]

def get_stock_zscore(ticker, period="5y"):
    """
    Fetch stock data and calculate weekly price variation z-score
    """
    try:
        # Download stock data
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)

        # Resample data to weekly and get last price of each week
        weekly_data = hist["Close"].resample("W").last()

        # Calculate weekly returns and drop NA values
        weekly_returns = weekly_data.pct_change(fill_method=None).dropna()

        # Calculate z-score of weekly returns
        zscore = (weekly_returns - weekly_returns.mean()) / weekly_returns.std()

        # Get the most recent z-score
        latest_zscore = zscore.iloc[-1]

        return round(latest_zscore, 2)
    except Exception as e:
        print(f"Error fetching data for {ticker}: {str(e)}")
        return None


def main():
    print("Stock weekly variation Z-Score Calculator for Reverse ETFs")
    print(f"Analyzing {len(REVERSE_ETFS)} reverse ETFs...")
    print("\nCalculating z-scores for weekly price variations...")
    print("-" * 50)

    # Calculate and display z-scores for each ticker
    for ticker in REVERSE_ETFS:
        zscore = get_stock_zscore(ticker)
        if zscore is not None:
            print(f"{ticker}: {zscore}")


if __name__ == "__main__":
    main() 