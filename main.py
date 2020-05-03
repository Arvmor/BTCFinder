#requirments
# pip install selenium
# apt-get update
# apt install chromium-chromedriver
# cp /usr/lib/chromium-browser/chromedriver /usr/bin

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import string
import os
import sys

# driver settings
sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', options=chrome_options)

#downloads a .txt file which contains fresh random hashes 
url = "https://onlinehashtools.com/generate-random-sha256-hash?&count=200&format=%2A&hex-base=true&randomcase=true"
driver.get(url)
time.sleep(1)
driver.find_element(
    By.XPATH, '/html/body/div/div[1]/div[2]/div[3]/div/div[3]/div[1]/div/div/div[2]/div[1]/div[3]').click()
time.sleep(1)
driver.find_element(
    By.XPATH, '/html/body/div/div[1]/div[2]/div[3]/div/div[3]/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]').click()
# main code
time.sleep(3)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
file = open("/content/output-onlinehashtools.txt", "r")  # replace your download directory path   <==============
# checking address
url = "https://www.bitaddress.org/"
driver.get(url)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="detailwallet"]').click()
for line in file:
    hstring = str(line)
    driver.find_element(By.XPATH, '//*[@id="detailprivkey"]').click()
    # pyautogui.hotkey('ctrl', 'a')
    driver.find_element(By.XPATH, '//*[@id="detailprivkey"]').clear()
    driver.find_element(By.XPATH, '//*[@id="detailprivkey"]').send_keys(hstring)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="detailview"]').click()
    public = driver.find_element(By.XPATH, '//*[@id="detailaddress"]').text
    print("public: "+str(public))
    print("priv8 : "+driver.find_element(By.XPATH,
                                         '//*[@id="detailprivwif"]').text)
    # checking the Wallet balance
    url = "https://www.blockchain.com/btc/address/"+str(public)
    driver.execute_script("window.open('');")
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[2])
    driver.get(url)
    balance = driver.find_element(
        By.XPATH, '//*[@id="__next"]/div[3]/div/div[3]/div[1]/div[1]/div[2]/div/div[6]/div[2]/span').text
    time.sleep(2)
    if str(balance) != "0.00000000 BTC":
        print("balance : "+str(balance))
    else:
        print("*****Empty Balance******")
    driver.close()
    driver.switch_to.window(driver.window_handles[1])
os.remove("/content/output-onlinehashtools.txt") # replace your download directory path   <==============
driver.close()
