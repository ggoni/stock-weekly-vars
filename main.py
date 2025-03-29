import yfinance as yf
import pandas as pd
import numpy as np


def get_stock_zscore(ticker, period="5y"):
    """
    Fetch stock data and calculate daily price variation z-score
    """
    try:
        # Download stock data
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)

        # Resample data to daily and get last price of each week
        daily_data = hist["Close"].resample("D").last()

        # Calculate weekly returns and drop NA values
        daily_returns = daily_data.pct_change(fill_method=None).dropna()


        # Calculate z-score of daily returns
        zscore = (daily_returns - daily_returns.mean()) / daily_returns.std()

        # Get the most recent z-score
        latest_zscore = zscore.iloc[-1]

        return round(latest_zscore, 2)
    except Exception as e:
        print(f"Error fetching data for {ticker}: {str(e)}")
        return None


def main():
    print("Stock daily variation Z-Score Calculator")
    print("Enter stock tickers separated by commas (e.g., AAPL, MSFT, GOOGL):")

    # Collect tickers from user
    ticker_input = input().strip()
    tickers = [t.strip().upper() for t in ticker_input.split(',')]

    print("\nCalculating z-scores for daily price variations...")
    print("-" * 50)

    # Calculate and display z-scores for each ticker
    for ticker in tickers:
        zscore = get_stock_zscore(ticker)
        print(f"{ticker}: {zscore}")


if __name__ == "__main__":
    main()
