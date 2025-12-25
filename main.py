import os
import sys

# Add the project root directly to sys.path if needed, although running as module is preferred.
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.loader import load_data
from src.cleaning import clean_data
from src.transform import process_data
from src.visualize import plot_data
from src.utils import print_separator

DATA_PATH = 'data/AI_Developer_Performance_Extended_1000.csv'
CHARTS_DIR = 'charts'

def main():
    print_separator('=', 60)
    print("      Group 11 - AI Developer Performance      ")
    print_separator('=', 60)

    try:
        df = load_data(DATA_PATH)
    except Exception as e:
        print("Failed to load data. Exiting.")
        return

    df_clean = clean_data(df)

    print("\n--- Transforming Data ---")
    df_processed, df_original = process_data(df_clean)
    print("Transformation complete.")
    print(f"Processed DataFrame Shape: {df_processed.shape}")
    
    print("\n--- Visualizing Data ---")
    plot_data(df_original, df_processed, save_dir=CHARTS_DIR)
    print("Visualization processing complete.")

    print_separator('=', 60)
    print("Pipeline Execution Finished.")
    print_separator('=', 60)

if __name__ == "__main__":
    main()
