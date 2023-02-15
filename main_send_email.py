import os
import requests
from datetime import datetime
from screenshot import take_screen_shot,login_glassdor,quit_driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
driver.set_window_size(1920, 1080)

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")




# Check Non-member Home
link_to_check = 'https://www.glassdoor.com/index.htm'
response = requests.get(link_to_check)
status_code = response.status_code
# Take Screen Shot --------------->
filename = "non_member_home"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()

# login to google chrome driver
login_glassdor(driver)

# Check EI Reviews
link_to_check = 'https://www.glassdoor.com/Reviews/Amazon-Reviews-E6036.htm'
response = requests.get(link_to_check)
status_code = response.status_code
# Take Screen Shot ------------->
filename = "ei_reviews"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()


# Check EI Salaries
link_to_check = 'https://www.glassdoor.com/Salary/IBM-Salaries-E354.htm'
response = requests.get(link_to_check)
status_code = response.status_code
# Take Screen Shot --------------->
filename = "ei_salaries"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()

# Check Job Search
link_to_check = 'https://www.glassdoor.com/Job/software-engineer-jobs-SRCH_KO0,17.htm?context=Jobs&clickSource=searchBox'
response = requests.get(link_to_check)
status_code = response.status_code
# Take Screen Shot -------->
filename = "job_search"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()

# Check Job Search in SF
link_to_check = 'https://www.glassdoor.com/Job/software-eng-in-sf-jobs-SRCH_KO0,18.htm?clickSource=searchBox'
response = requests.get(link_to_check)
status_code = response.status_code
# Take Screen Shot --------------->
filename = "job_search_sf"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()


# Check Job Search in London
link_to_check = 'https://www.glassdoor.com/Job/london-doctor-jobs-SRCH_IL.0,6_IC2671300_KO7,13.htm?clickSource=searchBox'
response = requests.get(link_to_check)
status_code = response.status_code
# Take Screen Shot --------------->
filename = "job_search_london"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()

# Check Job View
link_to_check = 'https://www.glassdoor.com/Job/Home/recentActivity.htm'
response = requests.get(link_to_check)
status_code = response.status_code
# Take Screen Shot --------------->
filename = "job_view"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()

# Check Job View Search SRE
link_to_check = 'https://www.glassdoor.com/Job/jobs.htm?context=Jobs&clickSource=searchBox&locId=1147401&locT=C&sc.keyword=Site%20Reliability%20Engineer'
response = requests.get(link_to_check)
status_code = response.status_code
# Take Screen Shot --------------->
filename = "job_search_sre"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()

# Check Member Home
link_to_check = 'https://www.glassdoor.com/member/home/index.htm'
response = requests.get(link_to_check)
status_code = response.status_code
# Take Screen Shot --------------->
filename = "member_home"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()



# Check Localized Pages for non-English Domains 
link_to_check = 'https://www.glassdoor.es/index.htm'
response = requests.get(link_to_check)
status_code = response.status_code

# Take Screen Shot --------------->
filename = "non_english_home"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()


# Check Localized Pages German EI Overview
link_to_check = 'https://www.glassdoor.de/%C3%9Cberblick/Arbeit-bei-Walmart-EI_IE715.11,18.htm'
response = requests.get(link_to_check)
status_code = response.status_code

# Take Screen Shot --------------->
filename = "german_ei_overview"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()


# Check Localized Pages German Job Search Engineer
link_to_check = 'https://www.glassdoor.de/Job/berlin-ingenieur-jobs-SRCH_IL.0,6_IC2622109_KO7,16.htm'
response = requests.get(link_to_check)
status_code = response.status_code
# Take Screen Shot --------------->
filename = "german_gob_search"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()


# Tier 2 and Check EI Jobs Ford
link_to_check = 'https://www.glassdoor.com/Jobs/Ford-Motor-Company-Jobs-E263.htm?filter.countryId=1'
response = requests.get(link_to_check)
status_code = response.status_code
# Take Screen Shot --------------->
filename = "ei_jobs_ford"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()

# Check EI Overview Microsoft
link_to_check = 'https://www.glassdoor.com/Overview/Working-at-Microsoft-EI_IE1651.11,20.htm'
response = requests.get(link_to_check)
status_code = response.status_code

# Take Screen Shot --------------->
filename = "ei_overview_microsoft"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()

# Check EI interviews Apple
link_to_check = 'https://www.glassdoor.com/Interview/Apple-Interview-Questions-E1138.htm'
response = requests.get(link_to_check)
status_code = response.status_code
# Take Screen Shot --------------->
filename = "ei_interview_apple"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()


# Check Salary Search
link_to_check = 'https://www.glassdoor.com/Salaries/amman-software-engineer-salary-SRCH_IL.0,5_IM1502_KO6,23.htm?clickSource=searchBtn'
response = requests.get(link_to_check)
status_code = response.status_code
# Take Screen Shot --------------->
filename = "salary_search"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()


# Tier 3 and Check EI Benefits Adobe
link_to_check = 'https://www.glassdoor.com/Benefits/Adobe-US-Benefits-EI_IE1090.0,5_IL.6,8_IN1.htm'
response = requests.get(link_to_check)
status_code = response.status_code
# Take Screen Shot --------------->
filename = "ei_benefits"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()

# Check EI Photos Disney 
link_to_check = 'https://www.glassdoor.com/Photos/Walt-Disney-Company-Office-Photos-E717.htm'
response = requests.get(link_to_check)
status_code = response.status_code
# Take Screen Shot --------------->
filename = "ei_photos"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()



# Check Salaries by Employer, Occupation, Metro
link_to_check = 'https://www.glassdoor.com/Salary/Meta-Software-Engineer-San-Francisco-Salaries-EJI_IE40772.0,4_KO5,22_IL.23,36_IM759.htm'
response = requests.get(link_to_check)
status_code = response.status_code
# Take Screen Shot --------------->
filename = "ei_salaries_by_employer_metro"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()

# Check Salaries by Employer, Occupation, City
link_to_check = 'https://www.glassdoor.com/Salary/Meta-Software-Engineer-San-Francisco-Salaries-EJI_IE40772.0,4_KO5,22_IL.23,36_IC1147401.htm'
response = requests.get(link_to_check)
status_code = response.status_code
# Take Screen Shot --------------->
filename = "ei_salaries_by_employer_city"
take_screen_shot(link_to_check,filename,status_code,driver)
img = open(f"gd_screenshots/{filename}.png", 'rb').read()


quit_driver(driver)

print("Sending The Email ...")
os.system("python send_email.py")