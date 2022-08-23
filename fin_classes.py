import os
from dotenv import load_dotenv
import requests

load_dotenv()

'''
ebitda_dict = {}
for year in json:
    ebitda_dict[year['calendarYear']] = year['ebitda']
print(ebitda_dict)
'''
# ebitda (income statement), roic(financial metric), roe (financial metric), earningsyield (financial metric), freecashflow (cashflow statement)
class DataJson:
    BASE_URL = 'https://financialmodelingprep.com/api/v3'
    PAYLOAD = {"limit": 120, "apikey": os.getenv('API_KEY')}

    def __init__(self, financial_statement: str, stock_symbol: str):
        # Validations of received arguments
        assert len(stock_symbol) <= 5, 'Your stock symbol is too long'
        assert financial_statement in ['income-statement', 'cash-flow-statement', 'key-metrics']

        # Assign to self object
        self.stock_symbol = stock_symbol
        self.financial_statement = financial_statement
        self.url = self.set_url()

    def set_url(self):
        return f'{self.BASE_URL}/{self.financial_statement}/{self.stock_symbol}'

    def get_url(self):
        return self.url

    def get_json_data(self):
        try:
            api_response = requests.get(self.get_url(), self.PAYLOAD)
        except AttributeError:
            return 'Something went wrong with the API request'
        return api_response.json()
