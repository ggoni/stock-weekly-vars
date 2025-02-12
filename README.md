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
````
