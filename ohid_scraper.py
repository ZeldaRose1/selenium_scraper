#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 08:57:52 2025

@author: zelda
"""

import time
import os

import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Read in username and password from auth.txt file
if os.path.isfile("auth.txt"):
    try:
        f = open("auth.txt", 'r')

        for lin in f:
            if lin.split(":")[0] == 'username':
                un = lin.split(":")[1].split("\n")[0]
            if lin.split(":")[0] == 'password':
                pw = lin.split(":")[1].split("\n")[0]

    except Exception as e:
        # If there is no username and password in the text file
        # request data form user
        print(e)
        un = input("Please input username:\t\t")
        pw = input("Please input password:\t\t")
    finally:
        # Close file to free memory
        f.close()


# Initialize service object with Firefox driver
service = Service(
    executable_path=r"./geckodriver"
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
uname.send_keys(un)

# Find password field
passwd = driver.find_element(By.ID, "loginPassword")
passwd.clear()
passwd.send_keys(pw + Keys.ENTER)

# Clean memory
del un, pw

# Save variable for xpath
oepa_x = "//div[@data-app-id='4ec93658-bb94-43f3-b02b-aeab5f025743']"
oepa_x += "//div[contains(a, 'Open App')]/a"

# Wait until website loads
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, oepa_x))
)

# Load next web page
page2 = driver.find_element(By.XPATH, oepa_x)
page2.click()
