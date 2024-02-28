import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd


driver = webdriver.Firefox()


jobs={"roles":[],
     "companies":[],
     "locations":[],
     "experience":[],
     "skills":[]}

for i in range(50):
    # just change the url or number of pages
    driver.get("https://www.naukri.com/data-scientist-jobs-{}".format(i))
    time.sleep(3)
    lst=driver.find_elements(By.CSS_SELECTOR, ".sjw__tuple")
    
    for job in lst:
        driver.implicitly_wait(10)
        
        try:
            role=job.find_element(By.CSS_SELECTOR, ".sjw__tuple .title").text
        except NoSuchElementException:
            skills = "Not specified"
            
        try:
            company=job.find_element(By.CSS_SELECTOR, ".sjw__tuple .comp-name").text
        except NoSuchElementException:
            skills = "Not specified"
            
        try:
            location=job.find_element(By.CSS_SELECTOR, ".locWdth").text
        except NoSuchElementException:
            skills = "Not specified"
            
        try:
            exp=job.find_element(By.CSS_SELECTOR, ".exp span").text
        except NoSuchElementException:
            skills = "Not specified"
            
        try:
            skills_elements = job.find_elements(By.CSS_SELECTOR, ".tag-li")
            skills = ', '.join([skill.text for skill in skills_elements])
        except NoSuchElementException:
            skills = "Not specified"
            
        jobs["roles"].append(role)
        jobs["companies"].append(company)
        jobs["locations"].append(location)
        jobs["experience"].append(exp)
        jobs["skills"].append(skills)
        
df = pd.DataFrame(jobs)
df.to_csv("DSJobsNaukri.csv", index=False)
