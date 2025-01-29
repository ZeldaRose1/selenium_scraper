#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 08:57:52 2025

@author: zelda
"""

import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Initialize service object with Firefox driver
service = Service(
    executable_path=r"/data/Books/projects/web_scraping/password_test/geckodriver"
)
# Initialize Firefox instance with service
driver = webdriver.Firefox(service=service)

# Pull Reddit page
driver.get("https://ohid.ohio.gov/wps/portal/gov/ohid/login")

# Wait to ensure the necessary elements have loaded before continuing.
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.TAG_NAME, "input"))
)

# Find username and password fields
uname = driver.find_element(By.ID, "loginUserID")
uname.clear()
uname.send_keys("Lalexander10")

# Find password field
passwd = driver.find_element(By.ID, "loginPassword")
passwd.clear()
passwd.send_keys("P@55word2024" + Keys.ENTER)


# Wait for 10 seconds and close browser
time.sleep(10)
# driver.close()



# # Load website
# driver.get("https://orteil.dashnet.org/cookieclicker/")

# # Save id to search for
# cookie_id = "bigCookie"

# # Move cursor to big cookie and click it.
# cookie = driver.find_element(By.ID, cookie_id)
# cookie.click()
