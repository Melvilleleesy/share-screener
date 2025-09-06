from dotenv import load_dotenv
import os
from dataCollector import get_data
from dataScreener import screen_data

load_dotenv()
FMP_KEY = os.getenv("FMP_KEY")

def main():
    ticker = input("Please Enter a Ticker Symbol: ")
    if isinstance(ticker, str):
        ticker = ticker.upper()
    company_data = get_data(ticker)
    print(screen_data(company_data))

main()
