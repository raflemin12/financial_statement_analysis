import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('API_KEY')
URL = 'https://financialmodelingprep.com/api/v3/income-statement/NKE'
payload = {"limit": 120, "apikey": API_KEY}

r = requests.get(URL, payload)
print(r.json())
