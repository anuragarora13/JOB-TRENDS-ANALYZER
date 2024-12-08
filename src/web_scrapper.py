from playwright.sync_api import sync_playwright

import pandas as pd

import logging

logging.basicConfig(
   
   filename='job_scrapper.log',
   level=logging.INFO,
   format='%(asctime)s - %(levelname)s - %(message)s'  
)

def scrape_job_listing(url):
    job_data=[]
    success_count=0
    error_count=0
    
    with sync_playwright() as p:
        
        browser=p.chromium.launch(headless=True)     
        
        page=browser.new_page()
        
        page.goto(url,timeout=60000,wait_until='domcontentloaded')
        
        page.wait_for_load_state('networkidle')
        # soup= BeautifulSoup(html_content,'html.parser')  
        # job_listings=soup.find_all(class_='job_listings')  
        print("Clicking the load more buttons to load all jobs")
        while True:
            try:
                load_more_listing = page.locator('.load_more_jobs')
                if load_more_listing.is_visible():
                    load_more_listing.click()
                    page.wait_for_timeout(2000)
                else:
                    print('now all jobs are updated')
                    break 
            except Exception as e:
                logging.error(f'error clicking load more button {e}')
                break
        job_elements = page.locator('li.job_listing')
        # Adjust this selector if necessary
        for i in range(job_elements.count()):
            try:
                job_title = job_elements.nth(i).locator('h3.job_listing-title').inner_text(timeout=2000)
                job_company = job_elements.nth(i).locator('div.job_listing-company strong').inner_text(timeout=2000)
                job_location = job_elements.nth(i).locator('div.job_listing-location').inner_text(timeout=2000)
                job_application_link = job_elements.nth(i).locator('a.job_listing-clickbox').get_attribute('href')
                job_post_date = job_elements.nth(i).locator('.job_listing-date').inner_text(timeout=5000)
                               
                
                job_data.append({
                    
                    'Job Title': job_title,
                    'Company': job_company,
                    'Location': job_location,
                    'Application Link':job_application_link,
                    'Date':job_post_date
                
                })
                logging.info(f"successfully scraped job {job_title} at {job_company}")
                success_count+=1
                
                
            except Exception as e:
                error_count+=1
                print(f"Error extracting job {i}: {e}")   
        browser.close()
        logging.info(f"scrapping completed successfully scrapped {success_count} jobs , failed to scrape {error_count} jobs")
        
        return pd.DataFrame(job_data)


