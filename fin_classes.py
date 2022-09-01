import os
from dotenv import load_dotenv
import requests
import pandas as pd

load_dotenv()

# ebitda (income statement), roic(financial metric), roe (financial metric), earningsyield (financial metric), freecashflow (cashflow statement)
class DataJson:
    BASE_URL = 'https://financialmodelingprep.com/api/v3'
    PAYLOAD = {"limit": 120, "apikey": os.getenv('API_KEY')}

    def __init__(self, stock_symbol: str):
        # Validations of received arguments
        assert len(stock_symbol) > 5, 'Your stock symbol is too long'
        
        # Assign to self object
        self.stock_symbol = stock_symbol
        self.financial_statement = ['income-statement', 'cash-flow-statement', 'key-metrics', 'balance-sheet-statement']
        self.income_request_json = self.get_json_data(self.set_url(self.financial_statement[0]))
        self.key_metric_request_json = self.get_json_data(self.set_url(self.financial_statement[1]))
        self.cashflow_request_json = self.get_json_data(self.set_url(self.financial_statement[2]))
        self.balance_request_json = self.get_json_data(self.set_url(self.financial_statement[3]))

    def set_url(self, financial_statement: str):
        return f'{self.BASE_URL}/{financial_statement}/{self.stock_symbol}'

    def get_json_data(self, url: str):
        try:
            api_response = requests.get(url, self.PAYLOAD)
            return api_response.json()
        except AttributeError:
            return 'Something went wrong with the API request'

def json_to_dict(json_data: list):
    # statement_dict = {year['calendarYear']: year for year in json_data}
    statement_dict = {}
    years = []

    for year in json_data:
        years.append(year['calendarYear'])
        for key, value in year.items()[7:]:
            if key not in statement_dict.items():
                statement_dict[key] = [value]
            else:
                statement_dict[key].append(value)
    return (years,statement_dict)

def dict_to_dataframe(data_dict: dict, column_names: list):
    return pd.DataFrame.from_dict(data_dict, orient='index', columns= column_names)

dis = DataJson('DIS')
print(json_to_dict(dis.income_request_json))
print(type(dict_to_dataframe(json_to_dict(dis.income_request_json))))
