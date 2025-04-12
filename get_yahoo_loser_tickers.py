
"""
Script to extract stock symbols from Yahoo Finance losers page.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import time

def get_yahoo_finance_losers():
    """
    Extracts the first column (symbols) from Yahoo Finance losers table.
    
    Returns:
        list: A list of stock symbols
    """
    url = "https://finance.yahoo.com/markets/stocks/losers/"
    
    # Set user agent to mimic a browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }
    
    try:
        # Make the HTTP request with a timeout
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the table
        table = soup.find('table', {'class': 'W(100%)'})
        
        if not table:
            # If the main table class isn't found, try looking for any table
            table = soup.find('table')
            
        if not table:
            print("Error: Could not find the table on the page.", file=sys.stderr)
            return []
        
        # Extract symbols from the first column
        symbols = []
        
        # Find all rows in the table body
        rows = table.find_all('tr')
        
        # Skip the header row if it exists
        for row in rows[1:]:
            # Get the first cell in each row
            cells = row.find_all('td')
            if cells:
                # The first column should contain the symbol
                symbol_cell = cells[0]
                
                # Extract the text or check for nested anchor tags
                symbol_link = symbol_cell.find('a')
                if symbol_link:
                    symbol = symbol_link.text.strip()
                else:
                    symbol = symbol_cell.text.strip()
                
                if symbol:
                    symbols.append(symbol)
        
        # If we couldn't find symbols using the direct approach, try an alternative method
        if not symbols:
            # Try to find elements with specific attributes that might contain symbols
            symbol_elements = soup.find_all('a', {'data-test': 'quoteLink'})
            if symbol_elements:
                symbols = [element.text.strip() for element in symbol_elements]
        
        return symbols
    
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}", file=sys.stderr)
        return []
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return []

def main():
    print("Fetching losers data from Yahoo Finance...")
    
    # Add a retry mechanism
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        symbols = get_yahoo_finance_losers()
        
        if symbols:
            # Join all symbols with commas and print on a single line
            print(",".join(symbols))
            break
        else:
            retry_count += 1
            if retry_count < max_retries:
                wait_time = 2 * retry_count
                print(f"Retrying in {wait_time} seconds... (Attempt {retry_count+1}/{max_retries})")
                time.sleep(wait_time)
            else:
                print("Failed to retrieve symbols after multiple attempts.")

if __name__ == "__main__":
    main()