nimport pandas as pd

import streamlit as st

st.set_page_config(page_title="Medicine utilisation", page_icon=":guardsman:", layout="wide")
st.image("chailogo.png", width=200)
st.title("Top 20% medicine procured by NDoH contributing 80% annual spend")


file_1 = st.file_uploader("Upload the first CSV file", type=["csv"])
file_2 = st.file_uploader("Upload the second CSV file (optional)", type=["csv"])

if file_1:
    df1 = pd.read_csv(file_1)
    st.dataframe(df1.head())

    if file_2:
        df2 = pd.read_csv(file_2)
        st.dataframe(df2.head())

        df_appended = pd.concat([df1, df2], axis=0)
        st.dataframe(df_appended.head())
    if st.button('Append'):
        st.success('Appending the two dataset...')
else:
    st.warning("No file was uploaded.")

file_1 = st.file_uploader("Upload the first CSV file", type=["csv"])
file_2 = st.file_uploader("Upload the second CSV file (optional)", type=["csv"])

if file_1:
    df1 = pd.read_csv(file_1)
    st.dataframe(df1.head())

    if file_2:
        df2 = pd.read_csv(file_2)
        st.dataframe(df2.head())

        df_appended = pd.concat([df1, df2], axis=0)
        st.dataframe(df_appended.head())
    if st.button('Append'):
        st.success('Appending the two dataset...')
else:
    st.warning("No file was uploaded.")

if st.button('Append'):
    st.success('Appending the two dataset...')
    df_appended["pct_contribution"] = df_appended.groupby("outcome")["outcome"].transform(lambda x: x/x.sum()*100)
    df_appended_sorted = df_appended.sort_values(by="pct_contribution", ascending=False)
    df_appended_sorted["cumulative_pct"] = df_appended_sorted["pct_contribution"].cumsum()
    important_factors = df_appended_sorted[df_appended_sorted["cumulative_pct"] <= 80]
    st.dataframe(important_factors)
    
    if st.button('Download CSV'):
        important_factors.to_csv("important_factors.csv", index=False)
        st.success('Important factors downloaded as CSV')
