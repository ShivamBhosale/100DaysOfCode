from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs= soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    jobpostdate = job.find('span',class_='sim-posted').span.text
    if 'few' in jobpostdate:
        company_name = job.find('h3',class_="joblist-comp-name").text.replace(' ','')
        skills= job.find('span',class_="srp-skills").text.replace(' ','')
    
        print(f'''
        Company Name:{company_name}
        Required Skills:{skills}
        Date Posted:{jobpostdate}
        ''')