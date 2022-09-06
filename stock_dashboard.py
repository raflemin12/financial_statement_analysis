import streamlit as st
from fin_classes import DataJson, json_to_dict, dict_to_dataframe

st.title('Company Financials Dashboard')

dis = DataJson('DIS')
dis_income_statements_json = json_to_dict(dis.income_request_json)
dis_income_statements_df = dict_to_dataframe(
    dis_income_statements_json[1],
    dis_income_statements_json[0])

st.write(dis_income_statements_df)
