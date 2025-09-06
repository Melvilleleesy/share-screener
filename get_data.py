import requests
from dotenv import load_dotenv
import os   
from concurrent.futures import ThreadPoolExecutor 

load_dotenv()
FMP_KEY = os.getenv("FMP_KEY")

def fetch_url(url):
    return requests.get(url).json()

def get_data(ticker):
    if not isinstance(ticker, str):
            return "Please enter a valid ticker string."
        
    ticker = ticker.upper()
    
    # Define URLs
    url1 = f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}?limit=5&apikey={FMP_KEY}"
    url2 = f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?limit=5&apikey={FMP_KEY}"
    url3 = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?limit=5&apikey={FMP_KEY}"
    # url4 = f"https://financialmodelingprep.com/api/v3/key-metrics/{ticker}?limit=5&apikey={FMP_KEY}"
    # url5 = f"https://financialmodelingprep.com/api/v3/historical-price-full/stock_dividend/{ticker}?apikey={FMP_KEY}"
    # url6 = f"https://financialmodelingprep.com/api/v3/ratios/{ticker}?limit=3&apikey={FMP_KEY}"
    # url7 = f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?apikey={FMP_KEY}"

    urls = [url1, url2, url3] # [url1, url2, url3, url4, url5, url6, url7]
    with ThreadPoolExecutor() as executor:
        responses = list(executor.map(fetch_url, urls))

    return responses
    