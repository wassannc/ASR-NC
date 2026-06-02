import streamlit as st
import requests
import pandas as pd

ODK_URL = st.secrets["ODK_URL"]
USERNAME = st.secrets["USERNAME"]
PASSWORD = st.secrets["PASSWORD"]
PROJECT_ID = st.secrets["PROJECT_ID"]

@st.cache_data(ttl=300)
def load_data(form_id):
    url = f"{ODK_URL}/v1/projects/{PROJECT_ID}/forms/{form_id}/submissions.csv"
    st.write("ODK_URL =", repr(ODK_URL))
    st.write("PROJECT_ID =", repr(PROJECT_ID))
    st.write("FORM_ID =", repr(form_id))
    st.write("URL =", url)
    response = requests.get(url, auth=(USERNAME, PASSWORD))

    if response.status_code != 200:
        st.error(f"Error: {response.status_code}")
        return pd.DataFrame()

    data = response.json()

    if "value" not in data:
        return pd.DataFrame()

    df = pd.json_normalize(data["value"])
    return df
