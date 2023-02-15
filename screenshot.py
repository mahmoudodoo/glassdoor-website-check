import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def login_glassdor(driver):
    driver.get("https://www.glassdoor.com/profile/login_input.htm")
    sleep(2)
    username = "glassdoornoc@gmail.com"
    password = "^%HyhqVFqHy9H(hX"
    driver.find_element(By.NAME,'username').send_keys(username)
    driver.find_element(By.NAME,'submit').click()
    sleep(2)
    driver.find_element(By.XPATH,"""//*[@id="inlineUserPassword"]""").send_keys(password)
    driver.find_element(By.NAME,'submit').click()
    print("Login to Glassdor Website ...")

def take_screen_shot(link,filename,status_code,driver):
    driver.get(f"{link}")
    print("please wait be patient ...")
    if filename =="job_view":
        sleep(1.5)
    sleep(.5)
    driver.save_screenshot(f'gd_screenshots/{filename}.png')
    print(f"The screenshot for the {filename} has been saved!")
    
def quit_driver(driver):
    driver.quit()

