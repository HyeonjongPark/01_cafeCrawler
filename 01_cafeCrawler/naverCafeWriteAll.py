from selenium import webdriver
import pandas as pd
import time
import urllib
import re
import requests
import certifi
import openpyxl

from urllib import parse
import urllib.parse as urlparse
from urllib.parse import parse_qs
from datetime import datetime
import pyperclip
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(3)

# 로그인 전용 화면
driver.get('https://nid.naver.com/nidlogin.login')


time.sleep(3)


# id, pw 입력할 곳을 찾습니다.
tag_id = driver.find_element_by_name('id')
tag_pw = driver.find_element_by_name('pw')
tag_id.clear()
time.sleep(1)

# id 입력
naver_id = open(
    "D:/workspace/python_workspace/01_cafeCrawler/naver_id.txt", "r").readline()
tag_id.click()
pyperclip.copy(naver_id)
tag_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# pw 입력
naver_pw = open(
    "D:/workspace/python_workspace/01_cafeCrawler/naver_pw.txt", "r").readline()
tag_pw.click()
pyperclip.copy(naver_pw)
tag_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)


driver.find_element_by_css_selector('#frmNIDLogin > fieldset > input').click()


time.sleep(3)
# 아이디와 비밀번호 입력
# driver.find_element_by_name('id').send_keys('id')
# driver.find_element_by_name('pw').send_keys('pw')

# driver.find_element_by_css_selector('#frmNIDLogin > fieldset > input').click()


인덱스 = []
텍스트 = []
작성자 = []
작성일 = []
조회수 = []
좋아요 = []

urls = []
pages = range(1, 45)

# 새벽기상
for page in pages:
    urls.append("https://cafe.naver.com/ArticleList.nhn?search.clubid=29171253&search.menuid=216&userDisplay=50&search.boardtype=L&search.specialmenutype=&search.totalCount=501&search.page="+str(page))

# 독서
for page in pages:
    urls.append("https://cafe.naver.com/ArticleList.nhn?search.clubid=29171253&search.menuid=217&userDisplay=50&search.boardtype=L&search.specialmenutype=&search.totalCount=501&search.page="+str(page))

# 운동
for page in pages:
    urls.append("https://cafe.naver.com/ArticleList.nhn?search.clubid=29171253&search.menuid=218&userDisplay=50&search.boardtype=L&search.specialmenutype=&search.totalCount=501&search.page="+str(page))

# 재테크/ SNS/ ..
for page in pages:
    urls.append("https://cafe.naver.com/ArticleList.nhn?search.clubid=29171253&search.menuid=219&userDisplay=50&search.boardtype=L&search.specialmenutype=&search.totalCount=501&search.page="+str(page))


for url in urls:
    driver.get(url)

    driver.switch_to_frame("cafe_main")
    driver.implicitly_wait(1)

    for i in range(0, 50):
        try:
            인덱스.append(driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[4]/table/tbody/tr["+str(i+1)+"]/td[1]/div[1]/div").text)
            텍스트.append(driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[4]/table/tbody/tr["+str(i+1)+"]/td[1]/div[2]").text)
            작성자.append(driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[4]/table/tbody/tr["+str(i+1)+"]/td[2]/div/table/tbody/tr/td/a").text)
            작성일.append(driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[4]/table/tbody/tr["+str(i+1)+"]/td[3]").text)
            조회수.append(driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[4]/table/tbody/tr["+str(i+1)+"]/td[4]").text)
            좋아요.append(driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[4]/table/tbody/tr["+str(i+1)+"]/td[5]").text)
        except:
            print("under 50 posting")
            break


# driver 종료
driver.quit()

df = pd.DataFrame({"index": 인덱스, "title": 텍스트, "writer": 작성자,
                  "date": 작성일, "viewCount": 조회수, "like": 좋아요})
#df.to_excel("naverCafeWrite_A_"+datetime.today().strftime("%m%d")+".xlsx", index = False)
df.to_excel("D:/workspace/010_crawler_naverCafe2/data/users/naverCafeWrite_A_" +
            datetime.today().strftime("%m%d")+".xlsx", index=False)
df.to_excel(
    "D:/workspace/010_crawler_naverCafe2/data/naverCafeWrite_A.xlsx", index=False)
