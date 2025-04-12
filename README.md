# Stock weekly Variation Z-Score Calculator

A Python tool that calculates z-scores for stock price variations, helping identify unusual price movements in the market, with a focus on daily losing stocks from Yahoo Finance.

## Description

This script automatically fetches the daily losing stocks from Yahoo Finance and calculates their weekly price variation z-scores. Z-scores help identify how far from the mean a data point is in terms of standard deviations, making it useful for spotting unusual price movements.

## Features

- Automatic fetching of daily losing stocks from Yahoo Finance
- Calculate z-scores for losing stocks
- Weekly price variation analysis
- User-friendly command-line interface
- Web scraping with retry mechanism and error handling

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ggoni/stock-weekly-vars
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Requirements

- Python 3.11 or higher
- Dependencies:
  - pandas
  - yfinance
  - numpy
  - beautifulsoup4
  - requests

## Usage

Run the script to analyze Yahoo Finance losers:
```bash
python get_yahoo_losers_z_score.py
```

Example output:

```bash
Stock weekly variation Z-Score Calculator for Yahoo Finance Losers
Fetching today's losing stocks...

Found 20 stocks to analyze
Calculating z-scores for weekly price variations...
--------------------------------------------------
TICKER1: 0.81
TICKER2: -0.1
...
```

# Stock Z-Score Calculator API

## API Usage

The API provides endpoints to calculate weekly price variation z-scores for stocks.

### Running the API

Start the API server using either of these methods:

```bash
# Method 1: Direct Python execution
python api.py

# Method 2: Using uvicorn (recommended for development)
uvicorn api:app --reload
```

The API will be available at http://localhost:8000

### Using the API

There are several ways to interact with the API:

1. **Using Python requests**:
```python
import requests

url = 'http://localhost:8000/calculate-zscores'
payload = {
    'tickers': ['AAPL', 'MSFT', 'GOOGL'],
    'period': '5y'
}

response = requests.post(url, json=payload)
print(response.json())
```

2. **Using cURL**:
```bash
curl -X POST 'http://localhost:8000/calculate-zscores' \
     -H 'Content-Type: application/json' \
     -d '{"tickers": ["AAPL", "MSFT", "GOOGL"], "period": "5y"}'
```

3. **Using Swagger UI**:
- Open http://localhost:8000/docs in your browser
- Click on the POST /calculate-zscores endpoint
- Click 'Try it out'
- Input your request and click 'Execute'

### API Parameters

- `tickers`: List of stock ticker symbols (e.g., ['AAPL', 'MSFT'])
- `period`: Time period for analysis (optional, default: '5y')
  - Available options: '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'

### Example Response

```json
[
    {
        "ticker": "AAPL",
        "zscore": 0.75
    },
    {
        "ticker": "MSFT",
        "zscore": 1.23
    },
    {
        "ticker": "GOOGL",
        "zscore": -0.45
    }
]
```
```

The main changes I made to the README are:
1. Updated the description to reflect the automatic fetching of losing stocks
2. Added the new dependencies (beautifulsoup4 and requests)
3. Updated the usage section to show how to use `get_yahoo_losers_z_score.py`
4. Updated the example output to match the new script's format
5. Removed the old manual ticker input instructions
6. Added information about the automatic fetching of losing stocks feature

Would you like me to make any adjustments to these changes before you save them to the README.md file?