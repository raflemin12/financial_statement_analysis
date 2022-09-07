import streamlit as st
from fin_classes import DataJson, json_to_dict, dict_to_dataframe

st.title('Company Financials Dashboard')

# cache JSON data
dis = DataJson('DIS')

financial_statement_options = st.selectbox(
    "What financial statement would you like to analyze?",
    ("Income Statement", "Balance Sheet", "Cashflow Statement")
)
# load appropriate data depending on selection

dis_income_statements_json = json_to_dict(dis.income_request_json)
dis_income_statements_df = dict_to_dataframe(
    dis_income_statements_json[1],
    dis_income_statements_json[0])

st.write(dis_income_statements_df)
