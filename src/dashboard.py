import streamlit as st
import pandas as pd
from data_loader import load_all_processed_data # Use the new loader

st.set_page_config(layout="wide")
st.title("GeoPulse: Global Economic Impact Dashboard")

# --- Data Loading ---
# This single function call loads all processed data.
@st.cache_data
def load_data():
    return load_all_processed_data()

data_sources = load_data()

# --- Main App ---
if not data_sources:
    st.error("No processed data found. Please run the data pipeline by executing `make pipeline` in your terminal.")
else:
    st.sidebar.title("Dataset Explorer")
    selected_dataset_name = st.sidebar.selectbox(
        "Select a dataset to view",
        sorted(list(data_sources.keys()))
    )
    
    st.header(f"Viewing Dataset: `{selected_dataset_name}`")
    
    selected_data_source = data_sources[selected_dataset_name]
    df = selected_data_source.get_data()
    
    # Display some summary stats
    st.subheader("Data Overview")
    st.write(f"**Shape:** {df.shape[0]} rows, {df.shape[1]} columns")
    
    st.dataframe(df)
    
    st.subheader("Descriptive Statistics")
    st.dataframe(df.describe())