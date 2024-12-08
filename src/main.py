import pandas as pd
from web_scrapper import scrape_job_listing
from database import save_to_database
from data_analysis import analyse_data


def main():
    
    url='https://jobspresso.co/remote-ai-data-jobs/'     
               
    # step 1 scrap the data 
    
    df=scrape_job_listing(url)
    print(df.columns)  # Check if 'Date' is present
    print(df.head())   # Check the first few rows of the DataFrame

    if not df.empty:
        save_to_database(df)
        print("Data Saved to job listing.db")
        print("analyse data")
        analyse_data()
            
    else:
        print('No Data Scrapped')    
     
# df.to_csv('job_listing.csv',index=False)    

if __name__== '__main__':
    main()   
