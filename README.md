# Stock weekly Variation Z-Score Calculator

A Python tool that calculates z-scores for stock price variations, helping identify unusual price movements in the market.

## Description

This script calculates the weekly price variation z-scores for any given stock tickers. Z-scores help identify how far from the mean a data point is in terms of standard deviations, making it useful for spotting unusual price movements.

## Features

- Calculate z-scores for multiple stock tickers
- Weekly price variation analysis
- User-friendly command-line interface
- Supports any stock available on Yahoo Finance

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

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. Enter stock tickers one per line (e.g., AAPL, MSFT, GOOGL)
3. Press Enter twice to start the calculation
4. View the z-scores for each stock

Example output:

```bash
Stock weekly Variation Z-Score Calculator
Enter stock tickers separated by commas (e.g., AAPL, MSFT, GOOGL):
AAPL, MSFT

Calculating z-scores for weekly price variations...
--------------------------------------------------

AAPL: 0.81
MSFT: -0.1
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
curl -X POST 'http://localhost:8000/calculate-zscores' \\
     -H 'Content-Type: application/json' \\
     -d '{\"tickers\": [\"AAPL\", \"MSFT\", \"GOOGL\"], \"period\": \"5y\"}'
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

## Bash editors from TIKR

```bash
cut -f1 tickers-250405.md | paste -s -d ',' -
```
