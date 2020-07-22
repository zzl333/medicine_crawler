from selenium import webdriver
import json
import time
import requests
import pandas as pd

def loginSys(loginName, password):

    driver_path = "chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get('https://dian.ysbang.cn/login.html')
    driver.implicitly_wait(0.2)
    LoginTitle = driver.title

    result = driver.title
    if LoginTitle == result:
        vcode = input("vcode:")

        driver.find_element_by_id('userAccount').send_keys(loginName)
        time.sleep(0.2)
        driver.find_element_by_id('password').send_keys(password)
        time.sleep(0.2)
        driver.find_element_by_id('captcha').send_keys(vcode)
        driver.implicitly_wait(0.2)
        driver.find_element_by_id("loginBtn").click()
        get_Data(driver)

def get_Data(driver):
    c = driver.get_cookies()
    cookie = [item["name"] + "=" + item["value"] for item in c]
    cookiestr = '; '.join(item for item in cookie)
    url = "https://dian.ysbang.cn/wholesale-drug/sales/getWholesaleList/v4110"
    driver.quit()
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": cookiestr,
        "Sec-Fetch-Mode": "cors",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://dian.ysbang.cn/drugListByKey.html?"
                   "v=4.25.0&searchKey=a&providerId=&providerIdList=&"
                   "providerName=&firstClassId=&secondClassId=&"
                   "thirdClassId=&firstClassName=&secondClassName=&"
                   "thirdClassName=&drugId="
    }
    data = {
        "classify_id": "",
        "drugId": -1,
        "ex": "201909051538",
        "factoryNames": "",
        "mustStockAvailable": 0,
        "onSale": 0,
        "operationtype": 1,
        "page": 1,
        "pageNo": 1,
        "pagesize": "60",
        "platform": "pc",
        "providerName": "",
        "provider_filter": "",
        "provider_id": "",
        "sort": "",
        "specs": "[]",
        "tagId": "",
        "ua": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 Chrome 76",
        "version": "pc4.15.0"
    }
    while True:
        name = input("请输入药名：")
        data["searchkey"]=name
        response = requests.post(url=url, headers=headers, data=json.dumps(data))
        js=json.loads(response.text)
        wholesales = js["data"]["wholesales"]
        exall = pd.DataFrame(wholesales)
        nendData = exall[["chainPrice", "promotionalPrice", "provider_name"]]
        nendData.to_csv("data.csv", encoding="utf-8")
        print("最高价格：")
        print(max(list(map(lambda x: float(x), nendData["chainPrice"]))))
        print("最高折后价：")
        print(max(list(map(lambda x: float(x), nendData["promotionalPrice"]))))

if __name__ == "__main__":
    username = "13164660890"
    password = "12ab3456"
    loginSys(username, password)

