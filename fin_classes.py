import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('API_KEY')
URL = 'https://financialmodelingprep.com/api/v3/income-statement/NKE'
payload = {"limit": 120, "apikey": API_KEY}

r = requests.get(URL, payload)
json = r.json()
ebitda_dict = {}
for year in json:
    ebitda_dict[year['calendarYear']] = year['ebitda']
print(ebitda_dict)

# ebitda (income statement), roic(financial metric), roe (financial metric), earningsyield (financial metric), freecashflow (cashflow statement)
