import requests
from bs4 import BeautifulSoup

url='https://jobspresso.co/remote-ai-data-jobs/'
response=requests.get(url)

if response.status_code==200:
    print("Successfully Fetched The Web page")
    html_comntent=response.content
else:
    print(f"Failed to fetch the web page  {response.status_code} ")
       
soup= BeautifulSoup(response.content,'html.parser')    

job_titles=soup.find_all(class_='job_listings')

for job in job_titles:
    print(job.text)
    
    