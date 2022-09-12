import streamlit as st
from fin_classes import DataJson, json_to_dict, dict_to_dataframe, clean_rows

st.title('Company Financials Dashboard')

# cache JSON data
dis = DataJson('DIS')

financial_statement_options = st.selectbox(
    "1) What financial statement would you like to analyze?",
    ("Income Statement", "Balance Sheet", "Cashflow Statement", "Key Metrics")
)
# load appropriate data depending on selection
if financial_statement_options == 'Income Statement':
    dis_income_statements_json = json_to_dict(dis.income_request_json)
    dis_income_statements_df = clean_rows(
        dict_to_dataframe(
            dis_income_statements_json[1],
            dis_income_statements_json[0]
            )
        )
    st.write(dis_income_statements_df)
elif financial_statement_options == 'Balance Sheet':
    dis_balance_json = json_to_dict(dis.balance_request_json)
    dis_balance_df = clean_rows(
        dict_to_dataframe(
            dis_balance_json[1],
            dis_balance_json[0]
            )
        )
    st.write(dis_balance_df)
elif financial_statement_options == 'Cashflow Statement':
    dis_cashflow_json = json_to_dict(dis.cashflow_request_json)
    dis_cashflow_df = clean_rows(
        dict_to_dataframe(
            dis_cashflow_json[1],
            dis_cashflow_json[0]
            )
        )
    st.write(dis_cashflow_df)
else:
    dis_key_metric_json = json_to_dict(dis.key_metric_request_json)
    dis_key_metric_df = clean_rows(
        dict_to_dataframe(
            dis_key_metric_json[1],
            dis_key_metric_json[0]
            )
        )
    st.write(dis_key_metric_df)
