import streamlit as st
import pandas as pd
import os
from PIL import Image

PROJECT_ROOT = os.getcwd()
DATA_PATH = os.path.join(PROJECT_ROOT, 'data', 'AI_Developer_Performance_Extended_1000.csv')
CHARTS_DIR = os.path.join(PROJECT_ROOT, 'charts')

st.title("Group 11 - Project Report")
st.sidebar.header("Navigation")
options = st.sidebar.radio("Go to:", ["Data Overview", "Visualizations"])

if options == "Data Overview":
    st.header("Dataset Overview")
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        st.write(f"**Shape:** {df.shape}")
        
        st.subheader("First 5 Rows")
        st.dataframe(df.head())
        
        st.subheader("Statistical Description")
        st.write(df.describe())
    else:
        st.error(f"Data file not found at: {DATA_PATH}")

elif options == "Visualizations":
    st.header("Visualizations")
    
    if os.path.exists(CHARTS_DIR):
        chart_files = sorted([f for f in os.listdir(CHARTS_DIR) if f.endswith('.png')])
        
        if not chart_files:
            st.warning("No charts found. Please run 'src/main.py' first.")
        
        for chart_file in chart_files:
            file_path = os.path.join(CHARTS_DIR, chart_file)
            image = Image.open(file_path)
            st.subheader(chart_file.replace('.png', '').replace('_', ' ').title())
            st.image(image, width="content")
    else:
        st.error(f"Charts directory not found at: {CHARTS_DIR}")

st.sidebar.info("Run `python src/main.py` locally to regenerate charts if missing.")
