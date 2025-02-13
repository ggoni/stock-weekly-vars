from fastapi import FastAPI, HTTPException
from typing import List, Union
import yfinance as yf
import pandas as pd
from pydantic import BaseModel

app = FastAPI(
    title="Stock Z-Score API",
    description="API for calculating weekly price variation z-scores for stocks"
)

class StockRequest(BaseModel):
    tickers: List[str]
    period: str = "5y"

class StockResponse(BaseModel):
    ticker: str
    zscore: Union[float, str]

def get_stock_zscore(ticker: str, period: str = "5y") -> Union[float, str]:
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
        return f"Error fetching data for {ticker}: {str(e)}"

@app.get("/")
def root():
    return {"message": "Welcome to Stock Z-Score API"}

@app.post("/calculate-zscores", response_model=List[StockResponse])
def calculate_zscores(request: StockRequest) -> List[StockResponse]:
    """
    Calculate z-scores for a list of stock tickers
    """
    results = []
    
    for ticker in request.tickers:
        ticker = ticker.strip().upper()
        zscore = get_stock_zscore(ticker, request.period)
        results.append(StockResponse(ticker=ticker, zscore=zscore))
    
    return results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 