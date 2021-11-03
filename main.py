# -----------------------------------Tinder Automation - Automated Swipe------------------------------------------------

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

account_id = 'Your facebook account id'
password = 'your facebook password'
count = 0


def url_update(n):
    new_url = driver.window_handles[n]
    driver.switch_to.window(new_url)


chrome_driver_path = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com")

# -----------------------------------------login ti account--------------------------------------------------
time.sleep(4)
login1 = driver.find_element_by_xpath('//*[@id="q-1565082725"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login1.click()
print("clicked on login")


try:
    # -------------------------------------------------click on more----------------------------------------------------
    time.sleep(2)
    url_update(0)
    try:
        login2 = driver.find_element_by_xpath('//*[@id="q-1343742289"]/div/div/div[1]/div/div[3]/span/button')
    except NoSuchElementException:
        login2 = driver.find_element_by_xpath('//*[@id="q-1343742289"]/div/div/div[1]/div/div[3]/span/button')

    login2.click()
    print("clicked on more")
except NoSuchElementException:
    print("more option is disabled")
    pass

# -------------------------------------------------click on facebook------------------------------------------------
time.sleep(3)
url_update(0)
login3 = driver.find_element_by_xpath('//*[@id="q-1343742289"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
login3.click()
print("clicked on facebook")

# -------------------------------------------------enter id-------------------------------------------------------------
time.sleep(3)
url_update(1)
login4 = driver.find_element_by_name('email')
login4.send_keys(account_id)
print("Email passed")

# -------------------------------------------------enter password-------------------------------------------------------
login5 = driver.find_element_by_xpath('//*[@id="pass"]')
login5.send_keys(password)
print("Password passed")

# -------------------------------------------------enter----------------------------------------------------------------
login = driver.find_element_by_xpath('//*[@id="loginbutton"]')
login.send_keys(Keys.ENTER)
print("Enter Pressed")

# -------------------------------------------------Enable Notifications-------------------------------------------------
time.sleep(10)
url_update(0)
try:
    location_access = driver.find_element_by_xpath('//*[@id="c-143158991"]/div/div/div/div/div[3]/button[1]/span')
except NoSuchElementException:
    location_access = driver.find_element_by_xpath('//*[@id="q-1343742289"]/div/div/div/div/div[3]/button[1]/span')
location_access.click()
print("Location Access Enabled.....")

# -------------------------------------------------Disable Notifications------------------------------------------------
notification_access = driver.find_element_by_xpath('//*[@id="q-1343742289"]/div/div/div/div/div[3]/button[1]/span')
notification_access.click()
print("Notification Access Denied.....")

# --------------------------------------------------Accept cookies------------------------------------------------------
cookies = driver.find_element_by_xpath('//*[@id="q-1565082725"]/div/div[2]/div/div/div[1]/button')
cookies.click()
print("Cookies Accepted.....")

# --------------------------------------------------Swipe -------------------------------------------------------------

time.sleep(12)
like = driver.find_element_by_xpath('//*[@id="q-1565082725"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span/svg/path')
like.click()
print("Liked.....")

while True:
    url_update(0)
    try:
        time.sleep(1)
        like = driver.find_element_by_xpath('//*[@id="q-1565082725"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[5]/div/div[4]/button/span/span')
        like.click()
        print("Liked.....")

    except ElementClickInterceptedException:
        home = driver.find_element_by_xpath('//*[@id="c-143158991"]/div/div/div[2]/button[2]/span')
        home.click()

    except NoSuchElementException:
        time.sleep(5)
        pass
    except :
        exte = driver.find_element_by_xpath('//*[@id="c-143158991"]/div/div/div[3]/button[2]/span')
    count += 1
    print(f"profile visited :{count}")


