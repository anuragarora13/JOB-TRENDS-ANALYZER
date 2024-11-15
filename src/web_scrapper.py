from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd
import logging

logging.basicConfig(
   filename='job_scrapper.log',
   level=logging.INFO,
   format='%(asctime)s - %(levelname)s - %(message)s'
   
)

def scrape_job_listing(url):
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)     
        page=browser.new_page()
        page.goto(url)
        page.wait_for_load_state('networkidle')
        html_content = page.content()
        # soup= BeautifulSoup(html_content,'html.parser')  
        # job_listings=soup.find_all(class_='job_listings')
        job_elements = page.locator('li.job_listing')
        # Adjust this selector if necessary
        job_data=[]
        
        success_count=0
        error_count=0
        
        
        for i in range(job_elements.count()):
            try:
                job_title = job_elements.nth(i).locator('h3.job_listing-title').inner_text(timeout=2000)
                job_company = job_elements.nth(i).locator('div.job_listing-company').inner_text(timeout=2000)
                job_location = job_elements.nth(i).locator('div.job_listing-location').inner_text(timeout=2000)
                
                job_data.append({
                    'Job Title': job_title,
                    'Company': job_company,
                    'Location': job_location,
                })
                logging.info(f"successfully scraped job {job_title} at {job_company}")
                success_count+=1
                
            except Exception as e:
                error_count+=1
                print(f"Error extracting job {i}: {e}")
                
        
        browser.close()
        logging.info(f"scrapping completed successfully scrapped {success_count} jobs , failed to scrape {error_count} jobs")
        
        return pd.DataFrame(job_data)


