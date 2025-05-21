from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
#from selenium_stealth import stealth
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import pandas as pd
import csv
import numpy as np

opts = Options()
#opts.add_argument("--headless")
opts.add_argument("--window-size=1920,1080")
opts.add_argument("--disable-gpu")
opts.add_argument("--allow-insecure-localhost")
opts.add_argument("--disable-blink-features=AutomationControlled")
opts.add_argument('--no-sandbox')
opts.add_argument('--enable-unsafe-swiftshader')
opts.add_argument('--disable-dev-shm-usage')
opts.add_argument('--log-level=1')
opts.add_argument("--disable-extensions")
opts.add_argument("--disable-component-extensions-with-background-pages")
#assert opts.headless  # Operating in headless mode
DRIVER_PATH = 'chromedriver.exe'



#proxy
p = '<51.159.24.172, 3163>'
pxy = Proxy()

#set proxy type
pxy.p_type = ProxyType.MANUAL

#http proxy
pxy.http_pxy = p

#ssl proxy
pxy.ssl_pxy = p

#object of DesiredCapabilities
c = webdriver.DesiredCapabilities.CHROME

#browser.close
#search_form = browser.find_element_by_id('navnesognamefornavn')



#search names


resultsToSave = np.array([])
i = 0
i2 = 0

    
#open browser
#browser = Chrome(options=opts,desired_capabilities = c,executable_path=DRIVER_PATH) #with proxy


browser = Chrome(options=opts) #without proxy
#stealth(browser)
browser.get('https://www.ft.dk/samling/20231/afstemning/268.htm')
print("sleeping")
#time.sleep(5000)
print("woke up...")
#accept cookies


time.sleep(1)
#results = browser.find_elements(By.CSS_SELECTOR, '.text-right')
#results = browser.find_element_by_class_name("table")
#results = browser.find_element("name","table")
print("sleeping")
#time.sleep(100)
print("woke up...")
wait = WebDriverWait(browser, 10)
folk = []
saveindex = 0
index=243
while index>0:
    browser.get("https://www.ft.dk/samling/20231/afstemning/"+str(index)+".htm")
    time.sleep(1)
    print("searching...")
    #/html/body/form/div[4]/div/div/div[2]/div[3]/div[3]/div[2]/div[1]/div/h2
    #afstemning = browser.find_element(By.XPATH, "//html/body/form/div[4]/div/div/div[2]/div[3]/div[3]/div[2]/div[1]/div/h2").get_attribute("innerHTML").strip()
    afstemning = index
    #afstemning_elem = wait.until(EC.presence_of_element_located((By.XPATH, "//html/body/form/div[4]/div/div/div[2]/div[3]/div[3]/div[2]/div[1]/div/h2")))
    print(afstemning)
    folk.append([afstemning])
    for x in list(range(179)):
        #/html/body/form/div[4]/div/div/div[2]/div[3]/div[3]/div[2]/div[10]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[1]
        #/html/body/form/div[4]/div/div/div[2]/div[3]/div[3]/div[2]/div[10]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]
        #/html/body/form/div[4]/div/div/div[2]/div[3]/div[3]/div[2]/div[10]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[1]
        #/html/body/form/div[4]/div/div/div[2]/div[3]/div[3]/div[2]/div[10]/div[3]/div[2]/div/div[1]/table/tbody/tr[178]/td[3]
        #/html/body/form/div[4]/div/div/div[2]/div[3]/div[3]/div[2]/div[10]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[1]
        navn = browser.find_element(By.XPATH, "//html/body/form/div[4]/div/div/div[2]/div[3]/div[3]/div[2]/div[10]/div[3]/div[2]/div/div[1]/table/tbody/tr["+str(x+1)+"]/td[1]").get_attribute("innerHTML").strip()
        parti = browser.find_element(By.XPATH, "//html/body/form/div[4]/div/div/div[2]/div[3]/div[3]/div[2]/div[10]/div[3]/div[2]/div/div[1]/table/tbody/tr["+str(x+1)+"]/td[2]").get_attribute("innerHTML").strip()
        stemme = browser.find_element(By.XPATH, "//html/body/form/div[4]/div/div/div[2]/div[3]/div[3]/div[2]/div[10]/div[3]/div[2]/div/div[1]/table/tbody/tr["+str(x+1)+"]/td[3]").get_attribute("innerHTML").strip()
        folk.append([navn,parti,stemme])
    index = index-1
    saveindex = saveindex+1
    print(index/132*100)
    if(1==1):
        df = pd.DataFrame(folk)
        df.to_csv('afstemninger20231_ theMISSING_prt2.csv', index=False)
        saveindex=0
        print("reached 235")

print(folk)


browser.close()

#Write csv
df = pd.DataFrame(folk)
df.to_csv('afstemninger20231 theMISSING_prt2.csv', index=False)

quit()
