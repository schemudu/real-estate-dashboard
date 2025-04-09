import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

def plot_income_vs_home_price(data: pd.DataFrame):
    """ Scatter plot of Median Income vs. Median Home Price """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='Median Income', y='Median Home Price')
    plt.title('Median Income vs. Median Home Price Across ZIP Codes')
    plt.xlabel('Median Income')
    plt.ylabel('Median Home Price')
    st.pyplot(plt)

def plot_housing_unit_distribution(data: pd.DataFrame):
    """ Bar plot for Housing Units per ZIP Code """
    plt.figure(figsize=(10, 6))
    sns.barplot(x='ZIP Code', y='Housing Units', data=data)
    plt.title('Housing Units Distribution Across ZIP Codes')
    plt.xlabel('ZIP Code')
    plt.ylabel('Number of Housing Units')
    #plt.xticks(rotation=90)
    st.pyplot(plt)

def plot_income_distribution_boxplot(data: pd.DataFrame):
    """ Box plot for income distribution across ZIP codes """
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, x='ZIP Code', y='Median Income')
    plt.title('Income Distribution Across ZIP Codes')
    plt.xlabel('ZIP Code')
    plt.ylabel('Median Income')
    #plt.xticks(rotation=90)
    st.pyplot(plt)

def plot_correlation_heatmap(data: pd.DataFrame):
    """ Correlation heatmap for various data points """
    correlation_matrix = data.corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap of Real Estate Data')
    st.pyplot(plt)


