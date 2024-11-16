import pandas as pd 
import logging
import sqlite3

logging.basicConfig(
   filename='job_scrapper.log',
   level=logging.INFO,
   format='%(asctime)s - %(levelname)s - %(message)s'
   
)

def save_to_database(df,db_name='job_listings.db'):
    try:
        conn = sqlite3.connect(db_name)
        
        df.to_sql('jobs',conn,if_exists='replace',index=False)
        logging.info("Data successfully saved to database")
    except Exception as e:
        logging.error("Error saving to database as e {e}")
    finally:
        conn.close()    
        
def load_from_database(db_name='job_listings.db'):
    conn = sqlite3.connect('job_listings.db')
    df=pd.read_sql_query("SELECT * FROM jobs",conn)
    conn.close()
    return df        