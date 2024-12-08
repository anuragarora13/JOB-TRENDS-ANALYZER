import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from database import load_from_database

def analyse_data():
    df = load_from_database()
    
    if df.empty:
        print('no data found in database to analyse')
        return

    # df['Date'] = pd.to_datetime(df['Date'], format='%B %d', errors='coerce')
    
    # if df['Date'].isnull().any():
    #     print("Warning: Some dates could not be parsed.")
    
    # job_counts_by_date = df['Date'].value_counts().sort_index()
    
    # plt.figure(figsize=(12,6))
    
    # job_counts_by_date.plot(kind='line',marker='o',color='b')
    # plt.title('Job Listings Over Time')
    # plt.xlabel('Date')
    # plt.ylabel('Number of Job Listings')
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # plt.show()
    
    
    
    
    plt.figure(figsize=(10,6))
    top_companies = df['Company'].value_counts().head(10)
    sns.barplot(x=top_companies.values,y=top_companies.index,hue=top_companies.index,palette='viridis',dodge=False,
        legend=False)
    plt.title("Top 10 Companies Hiring")
    plt.xlabel("Number of job listing")
    plt.ylabel("Company")
    plt.show()
    if df.empty:
        print("No Data Found in the data base to analyse")
        return