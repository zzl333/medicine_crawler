# captchaImg
from selenium import webdriver
import time
import requests
driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://dian.ysbang.cn/login.html')
time.sleep(2)
captchaImg=driver.find_element_by_id("captchaImg")
i=0
while(i<10000):
    dir = 'images/' + str(i+1)+'.jpg'
    src=driver.find_element_by_xpath("//img[@id='captchaImg']").get_attribute("src")
    img = requests.get(src)
    if img.status_code == 200:
        fp = open(dir, 'wb')
        fp.write(img.content)
        fp.close()
        print(src + "下载完成！")
    i += 1
    captchaImg.click()
    time.sleep(0.05)