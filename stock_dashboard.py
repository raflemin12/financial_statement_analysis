import streamlit as st
from fin_classes import DataJson, json_to_dict, dict_to_dataframe, clean_rows

st.title('Company Financials Dashboard')

# cache JSON data
stock_symbol = st.text_input(
    "1) What stock would you like to analyze?", 
    value= "Enter stock ticker"
)

stock= DataJson(stock_symbol)

financial_statement_options = st.selectbox(
    "1) What financial statement would you like to analyze?",
    ("Income Statement", "Balance Sheet", "Cashflow Statement", "Key Metrics")
)
# load appropriate data depending on selection
if financial_statement_options == 'Income Statement':
    stock_income_statements_json = json_to_dict(stock.income_request_json)
    stock_income_statements_df = clean_rows(
        dict_to_dataframe(
            stock_income_statements_json[1],
            stock_income_statements_json[0]
            )
        )
    st.write(stock_income_statements_df)
elif financial_statement_options == 'Balance Sheet':
    stock_balance_json = json_to_dict(stock.balance_request_json)
    stock_balance_df = clean_rows(
        dict_to_dataframe(
            stock_balance_json[1],
            stock_balance_json[0]
            )
        )
    st.write(stock_balance_df)
elif financial_statement_options == 'Cashflow Statement':
    stock_cashflow_json = json_to_dict(stock.cashflow_request_json)
    stock_cashflow_df = clean_rows(
        dict_to_dataframe(
            stock_cashflow_json[1],
            stock_cashflow_json[0]
            )
        )
    st.write(stock_cashflow_df)
else:
    stock_key_metric_json = json_to_dict(stock.key_metric_request_json)
    stock_key_metric_df = clean_rows(
        dict_to_dataframe(
            stock_key_metric_json[1],
            stock_key_metric_json[0]
            )
        )
    st.write(stock_key_metric_df)
