import pandas as pd
import numpy as np

def clean_data(df):
    """
    Cleans the dataframe: Nulls, Duplicates, Outliers.
    
    Args:
        df (pd.DataFrame): Input dataframe.
        
    Returns:
        pd.DataFrame: Cleaned dataframe.
    """
    print("\n--- Cleaning Data (Member 1 Task) ---")
    initial_rows = len(df)
    
    # 1. Remove Duplicates
    print("  Checking for duplicates...")
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print(f"    - Found {duplicates} duplicate rows. Dropping them.")
        df = df.drop_duplicates()
    else:
        print("    - No duplicates found.")
        
    # 2. Handle Missing Values
    print("  Checking for missing values...")
    null_counts = df.isnull().sum()
    if null_counts.sum() > 0:
        print(f"    - Found missing values:\n{null_counts[null_counts > 0]}")
        # Strategy: Fill numeric with median, text with Mode
        for col in df.columns:
            if df[col].isnull().sum() > 0:
                if np.issubdtype(df[col].dtype, np.number):
                    median_val = df[col].median()
                    df[col] = df[col].fillna(median_val)
                else:
                    mode_val = df[col].mode()[0]
                    df[col] = df[col].fillna(mode_val)
        print("    - Filled missing values with Median/Mode.")
    else:
        print("    - No missing values found.")

    # 3. Handle Outliers (Basic Z-score for demonstration on 'Hours_Coding')
    # Valid Z-score usually < 3
    if 'Hours_Coding' in df.columns:
        print("  Checking for outliers in 'Hours_Coding'...")
        mean_hc = df['Hours_Coding'].mean()
        std_hc = df['Hours_Coding'].std()
        z_scores = abs((df['Hours_Coding'] - mean_hc) / std_hc)
        outliers = (z_scores > 3).sum()
        if outliers > 0:
            print(f"    - Found {outliers} outliers in 'Hours_Coding' (Z > 3). Removing them.")
            df = df[z_scores <= 3]
        else:
            print("    - No significant outliers found in 'Hours_Coding'.")

    final_rows = len(df)
    print(f"Data cleaning completed. Rows: {initial_rows} -> {final_rows}")
    return df
