import yfinance as yf
import pandas as pd
import numpy as np
from main import get_stock_zscore  # reuse the existing function

def get_sp500_tickers():
    """
    Get S&P 500 tickers using Wikipedia, excluding BRK.B and BF.B
    """
    table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    df = table[0]
    # Exclude problematic tickers
    df = df[~df['Symbol'].isin(['BRK.B', 'BF.B'])]
    return df['Symbol'].tolist()

def analyze_sp500():
    print("Analyzing S&P 500 Weekly Variations")
    print("-" * 50)
    
    # Get S&P 500 tickers
    tickers = get_sp500_tickers()
    results = []
    
    # Process each ticker
    for i, ticker in enumerate(tickers, 1):
        print(f"Processing {i}/500: {ticker}")
        zscore = get_stock_zscore(ticker)
        results.append({
            'ticker': ticker,
            'zscore': zscore  # zscore will be float or None
        })
    
    # Create DataFrame and handle non-numeric values
    df_results = pd.DataFrame(results)
    
    # Filter out rows where zscore is not numeric
    df_results = df_results.dropna(subset=['zscore'])
    
    # Now sort by actual z-score
    df_results = df_results.sort_values('zscore', ascending=True)
    
    print("\nBottom 10 stocks by z-score:")
    print("-" * 50)
    bottom_10 = df_results.head(10)
    for _, row in bottom_10.iterrows():
        print(f"{row['ticker']}: {row['zscore']:.2f}")
    
    print(f"\nProcessed {len(df_results)} valid stocks out of {len(tickers)} total")

if __name__ == "__main__":
    analyze_sp500()
