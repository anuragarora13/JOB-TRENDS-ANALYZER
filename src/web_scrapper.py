# Build a project that scrapes websites for data and analyzes it. 
# For example, scrape job listings to study trends.
# import requests

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    
    browser=p.chromium.launch(headless=True)
    
    page=browser.new_page()
    
    page.goto('https://jobspresso.co/remote-ai-data-jobs/')
    
    page.wait_for_load_state('networkidle')
    html_content = page.content()
    
    # soup= BeautifulSoup(html_content,'html.parser')  
    # job_listings=soup.find_all(class_='job_listings')
    job_elements = page.locator('li.job_listing')  # Adjust this selector if necessary
    for i in range(job_elements.count()):
        job_title = job_elements.nth(i).locator('h3.job_listing-title').inner_text()
        job_company = job_elements.nth(i).locator('div.job_listing-company').inner_text()
        job_location = job_elements.nth(i).locator('div.job_listing-location').inner_text()
        
        print(f"Job Title: {job_title}")
        print(f"Company: {job_company}")
        print(f"Location: {job_location}")
        print("------")
