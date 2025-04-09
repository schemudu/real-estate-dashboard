import pandas as pd

def process_data(data: pd.DataFrame):
    # Check and process the columns
    # Median Income
    if 'B19013_001E' in data.columns:
        data['Median Income'] = data['B19013_001E'].apply(pd.to_numeric, errors='coerce')
    
    # Housing Units
    if 'B25001_001E' in data.columns:
        data['Housing Units'] = data['B25001_001E'].apply(pd.to_numeric, errors='coerce')
    
    # Median Home Price (if available)
    if 'B25077_001E' in data.columns:
        data['Median Home Price'] = data['B25077_001E'].apply(pd.to_numeric, errors='coerce')
    
    # Check if the ZIP Code column 
    if 'zip code tabulation area' in data.columns:
        data['ZIP Code'] = data['zip code tabulation area'].astype(str)
    
    # Perform any other data cleaning or processing here
    data = data.dropna(subset=['ZIP Code','Median Income', 'Housing Units', 'Median Home Price'], how='any')
    
    # Drop irrelevant columns after processing (e.g., original census variables)
    data = data.drop(columns=['NAME', 'B19013_001E', 'B25001_001E', 'B25077_001E', 'zip code tabulation area','STATE'], errors='ignore')
    
    # Reorder columns so ZIP Code is first
    column_order = ['ZIP Code', 'Median Income', 'Housing Units', 'Median Home Price']  # Adjust as necessary
    data = data[column_order]

    return data
