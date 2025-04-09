# real_estate_analytics dashboard

This project is a data visualization dashboard that provides insights into real estate metrics across different ZIP codes using data from the U.S. Census Bureau.

## Project Overview

The dashboard allows users to input ZIP codes and returns a set of key real estate indicators. It is built with:

- Python
- Streamlit (interactive web dashboard)
- Pandas (data processing)
- Matplotlib and Seaborn (data visualization)
- Requests (HTTP requests)
- U.S. Census Bureau API (data source)
- Git/GitHub (version control)

## Features

- Accepts one or more ZIP codes for analysis
- Retrieves and displays:
  - Median Household Income
  - Total Housing Units
  - Median Home Value (if available)
- Cleans and formats the data for readability
- Presents visualizations of housing unit distribution across ZIP codes
- Easy to extend with additional metrics or integrations

## How It Works

### 1. User Input
Users enter a list of ZIP codes through the Streamlit web interface.

### 2. Data Fetching
Data is retrieved from the U.S. Census Bureau ACS 5-Year Estimates API using the following variables:
- `B19013_001E`: Median Household Income
- `B25001_001E`: Total Housing Units
- `B25077_001E`: Median Home Value

### 3. Data Processing
Data is cleaned by:
- Converting to numeric types
- Dropping incomplete records
- Renaming columns for clarity

### 4. Data Visualization
A bar chart is generated using Seaborn to display the number of housing units by ZIP code.

### 5. Running the Application
streamlit run main.py
