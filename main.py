import yfinance as yf
import pandas as pd
import numpy as np


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
        weekly_returns = weekly_data.pct_change().dropna()

        # Calculate z-score of weekly returns
        zscore = (weekly_returns - weekly_returns.mean()) / weekly_returns.std()

        # Get the most recent z-score
        latest_zscore = zscore.iloc[-1]

        return round(latest_zscore, 2)
    except Exception as e:
        print(f"Error fetching data for {ticker}: {str(e)}")
        return None


def main():
    print("Stock weekly variation Z-Score Calculator")
    print("Enter stock tickers separated by commas (e.g., AAPL, MSFT, GOOGL):")

    # Collect tickers from user
    ticker_input = input().strip()
    tickers = [t.strip().upper() for t in ticker_input.split(',')]

    print("\nCalculating z-scores for weekly price variations...")
    print("-" * 50)

    # Calculate and display z-scores for each ticker
    for ticker in tickers:
        zscore = get_stock_zscore(ticker)
        print(f"{ticker}: {zscore}")


if __name__ == "__main__":
    main()
