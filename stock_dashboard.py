import streamlit as st
from fin_classes import DataJson, json_to_dict, dict_to_dataframe, clean_rows, json_to_df

st.title('Company Financials Dashboard')

# cache JSON data
stock_symbol = st.text_input(
    "1) Enter stock ticker below: "
)

stock= DataJson(stock_symbol)

financial_statement_options = st.selectbox(
    "1) Which financial statement would you like to analyze?",
    ("Income Statement", "Balance Sheet", "Cashflow Statement")
)
# load appropriate data depending on selection
if financial_statement_options == 'Income Statement':
    st.write(json_to_df(stock.get_income_statement_json()))
elif financial_statement_options == 'Balance Sheet':
    st.write(json_to_df(stock.get_balance_sheet_json()))
else:
    st.write(json_to_df(stock.get_cashflow_statement_json()))
