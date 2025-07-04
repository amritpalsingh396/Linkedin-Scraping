import time
import csv
import re

import pandas as pd
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import json
from datetime import datetime

chromedriver_autoinstaller.install()
# chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument("--headless=new")
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("force-device-scale-factor=0.25")
# chrome_options.add_argument("high-dpi-support=1.0")
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()

df = pd.read_csv('all_links_A.csv')

url = "https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true"

driver.get(url)

time.sleep(120)


with open(f"all_links_company.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Link"])  # Header row
    time.sleep(5)  # Allow page to load
    for i in df:
        driver.get(i)
        time.sleep(5)