# src/census_api.py

import requests
import pandas as pd

# Fetch data for specific ZIP codes from the Census API
def fetch_census_data(zip_codes):
    base_url = "https://api.census.gov/data/2021/acs/acs5"
    params = {
        "get": "NAME,B19013_001E,B25001_001E,B25077_001E,STATE",  
        "for": "zip code tabulation area:" + ",".join(zip_codes),
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()

        # Convert the data to a pandas DataFrame
        columns = data[0]
        rows = data[1:]

        df = pd.DataFrame(rows, columns=columns)
        df['zip code tabulation area'] = df['zip code tabulation area'].astype(str)

        return df

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error
