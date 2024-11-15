import pandas as pd
from web_scrapper import scrape_job_listing
from database import save_to_database
    
def main():
    url='https://jobspresso.co/remote-ai-data-jobs/'                
    # step 1 scrap the data 
    df=scrape_job_listing(url)
   
    if not df.empty:
        save_to_database(df)
        print("Data Saved to job listing.db")
    else:
        print('No Data Scrapped')    
     
# df.to_csv('job_listing.csv',index=False)    

if __name__== '__main__':
    main()   
