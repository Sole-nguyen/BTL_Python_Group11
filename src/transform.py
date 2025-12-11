import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import warnings

warnings.filterwarnings('ignore')

def process_data(df):
    print("  Processing data...")
    
    # 1. Feature Engineering: Create useful derivatives
    df_eng = df.copy()
    
    # Efficiency: Lines of Code per Hour
    # Handle division by zero if Hours_Coding is 0 (though unlikely in this dataset, good practice)
    df_eng['Efficiency'] = df_eng.apply(lambda row: row['Lines_of_Code'] / row['Hours_Coding'] if row['Hours_Coding'] > 0 else 0, axis=1)
    
    # Performance_Category: Categorical binning of Task_Success_Rate
    # Low: < 60, Medium: 60-85, High: > 85
    bins = [0, 60, 85, 100]
    labels = ['Low', 'Medium', 'High']
    df_eng['Performance_Category'] = pd.cut(df_eng['Task_Success_Rate'], bins=bins, labels=labels, include_lowest=True)
    
    print("  Feature Engineering: Created 'Efficiency' and 'Performance_Category'.")
    
    # Keep a copy for visualization (before scaling)
    df_vis = df_eng.copy()
    
    # 2. Encoding Categorical Variables
    print("  Encoding: One-hot encoding 'Performance_Category'.")
    df_encoded = pd.get_dummies(df_eng, columns=['Performance_Category'], prefix='Perf')
    
    # 3. Scaling Numerical Data
    
    numeric_cols = df_encoded.select_dtypes(include=[np.number]).columns.tolist()
    
    print(f"  Scaling: Standardizing {len(numeric_cols)} numerical features.")
    scaler = StandardScaler()
    df_encoded[numeric_cols] = scaler.fit_transform(df_encoded[numeric_cols])
    
    return df_encoded, df_vis