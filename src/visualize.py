import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

def plot_data(df_original, df_processed, save_dir='charts'):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        
    print(f"  Generating charts in '{save_dir}'...")
    
    sns.set_palette("viridis")
    sns.set_style("whitegrid")
    
    # 1. Histogram: Distribution of Hours Coding
    plt.figure(figsize=(10, 6))
    sns.histplot(df_original['Hours_Coding'], kde=True, bins=20, color='skyblue')
    plt.title('')
    plt.xlabel('Hours Coding')
    plt.ylabel('Frequency')
    plt.savefig(f'{save_dir}/1_histogram_hours_coding.png')
    plt.close()
    print("    - Saved 1_histogram_hours_coding.png")
    
    # 2. Bar Chart: Mean Task Success Rate by Stress Level Groups
    # Binning stress level for better bar chart
    df_vis = df_original.copy()
    df_vis['Stress_Group'] = pd.cut(df_vis['Stress_Level'], bins=[0, 33, 66, 100], labels=['Low', 'Medium', 'High'])
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_vis, x='Stress_Group', y='Task_Success_Rate', ci=None, palette='magma')
    plt.title('Average Task Success Rate by Stress Level')
    plt.xlabel('Stress Level Group')
    plt.ylabel('Avg Task Success Rate (%)')
    plt.savefig(f'{save_dir}/2_bar_stress_vs_success.png')
    plt.close()
    print("    - Saved 2_bar_stress_vs_success.png")

    # 3. Pie Chart: Performance Category Distribution
    plt.figure(figsize=(8, 8))
    perf_counts = df_original['Performance_Category'].value_counts()
    plt.pie(perf_counts, labels=perf_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
    plt.title('Distribution of Performance Categories')
    plt.savefig(f'{save_dir}/3_pie_performance.png')
    plt.close()
    print("    - Saved 3_pie_performance.png")

    # 4. Boxplot: Sleep Hours Distribution
    plt.figure(figsize=(8, 6))
    sns.boxplot(y=df_original['Sleep_Hours'], color='lightgreen')
    plt.title('Boxplot of Sleep Hours')
    plt.ylabel('Sleep Hours')
    plt.savefig(f'{save_dir}/4_boxplot_sleep_hours.png')
    plt.close()
    print("    - Saved 4_boxplot_sleep_hours.png")

    # 5. Heatmap: Correlation Matrix
    # Select only numeric columns for correlation
    numeric_df = df_original.select_dtypes(include=['float64', 'int64'])
    corr = numeric_df.corr()
    
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Feature Matrix')
    plt.tight_layout()
    plt.savefig(f'{save_dir}/5_heatmap_correlation.png')
    plt.close()
    print("    - Saved 5_heatmap_correlation.png")
