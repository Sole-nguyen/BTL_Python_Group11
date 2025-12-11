import pandas as pd

def clean_data(df):

    print("\n--- Cleaning Data (Member 1 Task) ---")
    print("Performing basic cleaning checks...")

    null_counts = df.isnull().sum().sum()
    if null_counts > 0:
        print(f"Warning: Found {null_counts} missing values. (Handling to be implemented by Member 1)")
    else:
        print("No missing values found (skipping detailed check).")

    print("Data cleaning completed (Pass-through).")
    return df
