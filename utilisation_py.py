import pandas as pd
import streamlit as st

st.set_page_config(page_title="Medicine utilisation", page_icon=":guardsman:", layout="wide")
st.image("chailogo.png", width=200)
st.title("Top 20% medicine procured by NDoH contributing 80% annual spend")


file_1 = st.file_uploader("Upload the first CSV file", type=["csv"])
file_2 = st.file_uploader("Upload the second CSV file (optional)", type=["csv"])

if file_1:
    df1 = pd.read_csv(file_1)
    st.subheader("The first 5 rows of dataset 1", color="blue")
    st.dataframe(df1.head())

    if file_2:
        df2 = pd.read_csv(file_2)
        st.subheader("The first 5 rows of dataset 2", color="blue")
        st.dataframe(df2.head())

    if st.button('Append'):
        st.success('Appending the two dataset...')
        df_appended = pd.concat([df1, df2], axis=0)
        st.subheader("The first 5 rows of the appended dataset", color="blue")
        st.dataframe(df_appended.head())
        df_appended["pct_contribution"] = df_appended.groupby("nsn")["order_qty"].transform(lambda x: x/x.sum()*100)
        df_appended_sorted = df_appended.sort_values(by="pct_contribution", ascending=False)
        df_appended_sorted["cumulative_pct"] = df_appended_sorted["pct_contribution"].cumsum()
        important_medicines = df_appended_sorted[df_appended_sorted["cumulative_pct"] <= 80]
        st.dataframe(important_medicines)
else:
    st.warning("No file was uploaded.")
   
    if st.button('Download CSV'):
        important_medicines.to_csv("important_medicines.csv", index=False)
        st.success('Important medicines downloaded as CSV')
