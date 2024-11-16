import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from database import load_from_database

def analyse_data():
    df = load_from_database()
    
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
    


    