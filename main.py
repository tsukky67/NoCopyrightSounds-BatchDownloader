import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
from selenium.webdriver.chrome.options import Options

musicdir = os.getcwd() + "\musics"

options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=options)
params = {'behavior': 'allow', 'downloadPath': musicdir}
driver.execute_cdp_cmd('Page.setDownloadBehavior', params)

pagenum = 1
while True:
    driver.get('https://ncs.io/music-search?page='+str(pagenum))
    pagenum += 1

    elements = driver.find_elements(By.XPATH, '/html/body/main/article[3]/div/table/tbody/tr[*]/td[8]/a')

    if elements == []: #This indicates that we are past the last page.
        driver.quit()
        break

    for element in elements:
        element.click()
        time.sleep(2)
        dls = driver.find_elements(By.XPATH,'//*[@id="download"]/div[2]/div[1]/a[1]')
        dls[0].click()
        time.sleep(5)
        close = driver.find_elements(By.XPATH,'//*[@id="download"]/div[1]/a/i')
        try:
            close = driver.find_elements(By.XPATH,'//*[@id="download"]/div[1]/a/i')
            close[0].click()
        except IndexError:
            driver.back()
            close = driver.find_elements(By.XPATH,'//*[@id="download"]/div[1]/a/i')
            close[0].click()
print("Done")
