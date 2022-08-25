import os
from dotenv import load_dotenv
import requests

load_dotenv()

# ebitda (income statement), roic(financial metric), roe (financial metric), earningsyield (financial metric), freecashflow (cashflow statement)
class DataJson:
    BASE_URL = 'https://financialmodelingprep.com/api/v3'
    PAYLOAD = {"limit": 120, "apikey": os.getenv('API_KEY')}

    def __init__(self, stock_symbol: str):
        # Validations of received arguments
        assert len(stock_symbol) <= 5, 'Your stock symbol is too long'
        
        # Assign to self object
        self.stock_symbol = stock_symbol
        self.financial_statement = ['income-statement', 'cash-flow-statement', 'key-metrics', 'balance-sheet-statement']
        self.income_request_dict = self.get_json_data(self.set_url(self.financial_statement[0]))[0]
        self.key_metric_request_dict = self.get_json_data(self.set_url(self.financial_statement[1]))[0]
        self.cashflow_request_dict = self.get_json_data(self.set_url(self.financial_statement[2]))[0]
        self.balance_request_dict = self.get_json_data(self.set_url(self.financial_statement[3]))[0]

    def set_url(self, financial_statement: str):
        return f'{self.BASE_URL}/{financial_statement}/{self.stock_symbol}'

    def get_json_data(self, url: str):
        try:
            api_response = requests.get(url, self.PAYLOAD)
            return api_response.json()
        except AttributeError:
            return 'Something went wrong with the API request'

class Cleaner:
    def __init__(self, json: list):
        self.json = json
