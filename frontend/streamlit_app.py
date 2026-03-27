import streamlit as st
import requests

st.title("AI Contract Analyzer")
file = st.file_uploader("Upload contract PDF")

if file:
    response = requests.post("http://localhost:8000/analyze", files={"file": file})
    st.write(response.json())