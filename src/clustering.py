# src/clustering.py

from sklearn.cluster import KMeans
import pandas as pd

# Perform clustering based on the median income and housing units
def cluster_zip_codes(df):
    # Select the features for clustering: median income and housing units
    features = df[['B19013_001E', 'B25001_001E']].apply(pd.to_numeric, errors='coerce')
    
    # Remove any rows with missing data
    features = features.dropna()

    # Perform KMeans clustering (e.g., 3 clusters)
    kmeans = KMeans(n_clusters=3, random_state=0)
    df['Cluster'] = kmeans.fit_predict(features)

    return df
