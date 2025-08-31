# -*- coding: utf-8 -*-
"""
Reusable data processing modules for CUMCM.
This script contains a collection of common data handling functions
that can be adapted for various problems.
"""

import pandas as pd
from typing import Optional

def load_data(file_path: str) -> Optional[pd.DataFrame]:
    """
    Loads data from a specified file path (CSV, Excel).

    Args:
        file_path (str): The path to the data file.

    Returns:
        Optional[pd.DataFrame]: A pandas DataFrame if loading is successful, otherwise None.
    """
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file_path)
        else:
            print(f"Unsupported file format for: {file_path}")
            return None
        print(f"Data loaded successfully from {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: The file was not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None

def summarize_data(df: pd.DataFrame):
    """
    Provides a quick summary of the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to summarize.
    """
    print("--- Data Summary ---")
    print("\nShape:")
    print(df.shape)
    print("\nInfo:")
    df.info()
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nDescriptive Statistics:")
    print(df.describe())
    print("--- End of Summary ---")


# AI-PROMPT: The following function is a template for data cleaning.
# Please adapt it based on the specific requirements of the problem,
# such as how to handle missing values (e.g., mean, median, mode, or a more
# complex imputation method) and which columns to process.

def clean_data_template(df: pd.DataFrame) -> pd.DataFrame:
    """
    A template for a data cleaning function.

    Args:
        df (pd.DataFrame): The raw DataFrame.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    df_cleaned = df.copy()

    # Example: Fill missing numerical data with the median
    for col in df_cleaned.select_dtypes(include=['float64', 'int64']).columns:
        if df_cleaned[col].isnull().any():
            median_val = df_cleaned[col].median()
            df_cleaned[col].fillna(median_val, inplace=True)
            print(f"Filled missing values in '{col}' with median ({median_val}).")

    # Example: Remove duplicate rows
    initial_rows = len(df_cleaned)
    df_cleaned.drop_duplicates(inplace=True)
    rows_dropped = initial_rows - len(df_cleaned)
    if rows_dropped > 0:
        print(f"Dropped {rows_dropped} duplicate rows.")

    return df_cleaned