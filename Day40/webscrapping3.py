from bs4 import BeautifulSoup
import requests
import time

print("Enter the skills you are not familiar with\n ")
unfamiliar_skill = input('> ')
print(f'Filtering out {unfamiliar_skill}') 

def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs= soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        jobpostdate = job.find('span',class_='sim-posted').span.text
        if 'few' in jobpostdate:
            company_name = job.find('h3',class_="joblist-comp-name").text.replace(' ','')
            skills = job.find('span',class_="srp-skills").text.replace(' ','')
            moreinfo =job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'Jobs/{index}.txt','w') as f:
                    f.write(f'Company Name: {company_name.strip()}\n')
                    f.write(f'Required Skills: {skills.strip()}\n')
                    f.write(f'Date Posted: {jobpostdate.strip()}')
                    f.write(f"More info: {moreinfo}")
                print(f"File Saved: {index}")


                print(" ")

if __name__ == '__main__':
    while True:
        find_jobs()
        print("Waiting for 30 Seconds")
        time.sleep(30)