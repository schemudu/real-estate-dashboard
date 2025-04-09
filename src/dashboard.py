# src/dashboard.py

import streamlit as st
import pandas as pd
from src.census_api import fetch_census_data
from src.data_processing import process_data
from src.visualizations import (
    plot_income_vs_home_price,
    plot_housing_unit_distribution,
    plot_income_distribution_boxplot,
    plot_correlation_heatmap,
)

def render_dashboard():
    
    # Title for the dashboard
    st.title("Real Estate Insights Dashboard")
    st.write("""
        Welcome to the Real Estate Insights Dashboard. 
        This tool allows you to explore key census data related to income levels, housing units, 
        and affordability across different ZIP codes. 
        Please enter one or more ZIP codes to begin your analysis.
    """)
    
    # Ask user for ZIP codes
    zip_codes_input = st.text_input("Enter ZIP codes (comma separated):")
    if zip_codes_input:
        zip_codes = zip_codes_input.split(',')

        # Fetch census data for the entered ZIP codes
        st.write(f"Fetching data for ZIP codes: {zip_codes}...")
        census_data = fetch_census_data(zip_codes)

        # If data is available, process it and display visualizations
        if not census_data.empty:
            processed_data = process_data(census_data)
            st.write("Processed Census Data:", processed_data)

            # Display visualizations
            plot_income_vs_home_price(processed_data)
            plot_housing_unit_distribution(processed_data)
            plot_income_distribution_boxplot(processed_data)
            plot_correlation_heatmap(processed_data)


        else:
            st.write("No data found for the entered ZIP codes.")
