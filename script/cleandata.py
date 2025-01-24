import pandas as pd
import numpy as np

def clean_data(df):
    """Clean the DataFrame."""
    # Handling missing values
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        median_value = df[column].median()
        df[column] = df[column].fillna(median_value)

    df = df.dropna(subset=['FraudResult'])  # Adjust column name as necessary
    df.drop_duplicates(inplace=True)

    # Outlier detection and removal
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    for column in numeric_columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    
    return df