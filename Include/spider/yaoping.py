from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from xml import etree
import time

driver_path="chromedriver.exe"
driver=webdriver.Chrome(executable_path=driver_path)
driver.get("https://dian.ysbang.cn/login.html")
userAccount=driver.find_element_by_id("userAccount")
password=driver.find_element_by_id("password")
userAccount.send_keys("13164660890")
password.send_keys("12ab3456")
WebDriverWait(driver,1000).until(
    EC.presence_of_element_located((By.ID, "searchKey"))
)
name=input("请输入药名：")
search = name
searchKey=driver.find_element_by_id("searchKey")
searchKey.send_keys(search)

WebDriverWait(driver,1000).until(
    EC.presence_of_element_located((By.ID,"searchKey"))
)
goSearch = driver.find_element_by_id("goSearch")
goSearch.click()

time.sleep(5)
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "drugInfoList")))
finally:
    print(driver.page_source)
    driver.close()
