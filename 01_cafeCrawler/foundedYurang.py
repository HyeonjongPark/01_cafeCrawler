from selenium import webdriver
import pandas as pd
import time
import urllib
import re
import requests
import certifi
import pyperclip

from urllib import parse
import urllib.parse as urlparse
from urllib.parse import parse_qs
from datetime import datetime, date, timedelta
from selenium.webdriver.common.keys import Keys

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = open("./slack_token.txt", "r").readline()


page_range = 11

post_message(myToken,"#unchecked", "안녕하세요 주인님. 답변되지 않은 url 찾는 일 시작합니다. 약 "+str((page_range-1)*3) +"분 정도 소요될 예정입니다.")



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
naver_id = open("./naver_id.txt", "r").readline()
tag_id.click()
pyperclip.copy(naver_id)
tag_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# pw 입력
naver_pw = open("./naver_pw.txt", "r").readline()
tag_pw.click()
pyperclip.copy(naver_pw)
tag_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)


driver.find_element_by_css_selector('#frmNIDLogin > fieldset > input').click()


time.sleep(3)


인덱스=[]
작성일=[]
urls = []



pages = range(1,page_range)

# 인덱스 별 url
for page in pages :
    urls.append("https://cafe.naver.com/ArticleList.nhn?search.clubid=29171253&search.menuid=197&userDisplay=50&search.boardtype=L&search.specialmenutype=&search.totalCount=501&search.page="+str(page))

for url in urls :    
    driver.get(url)
        
    driver.switch_to_frame("cafe_main")
    driver.implicitly_wait(1)

    for i in range(0,50):
        try :           
            인덱스.append(driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/table/tbody/tr["+str(i+1)+"]/td[1]/div[1]/div").text)
            작성일.append(driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/table/tbody/tr["+str(i+1)+"]/td[3]").text)
        except :
            print("50개 미만의 게시글입니다.")
            break

df=pd.DataFrame({"ind":인덱스, "date":작성일})

full_urls = []

# index url
for ind in 인덱스 :
    full_urls.append("https://cafe.naver.com/ArticleRead.nhn?clubid=29171253&menuid=197&boardtype=L&page=1&articleid="+str(ind))

yesterday = date.today() - timedelta(1)
yesterday_str = yesterday.strftime('%Y.%m.%d.')
# 수집된 데이터 기준으로 150개에 해당하는 미기재 url을 알고 싶을 경우,
yesterday_index = df.ind

# 오늘 기준으로 어제자 미기재 url만 알고 싶을 경우,
#yesterday_index = df[df.date == yesterday_str].ind






full_urls2 = []

# index url
for ind in yesterday_index :
    full_urls2.append("https://cafe.naver.com/ArticleRead.nhn?clubid=29171253&menuid=197&boardtype=L&page=1&articleid="+str(ind))

    
full_urls3 = []

for urls2 in full_urls2:
    driver.get(urls2)
    
    driver.implicitly_wait(1.5)
    try :
        driver.switch_to_frame("cafe_main")

        driver.implicitly_wait(1.5)
    
        nicknames = []
        
        for i in range(0,50):
            driver.implicitly_wait(1.5)
            try :           
                nicknames.append(driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div[5]/ul/li["+str(i+1)+"]/div/div/div[1]/div/a").text)
            except :
                break
                
                
        if len(nicknames) == 0:
                for i in range(0,50):
                    driver.implicitly_wait(1.5)
                    try :           
                        nicknames.append(driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div[6]/ul/li["+str(i+1)+"]/div/div/div[1]/div/a").text)
                    except :
                        break
        
        print(nicknames)
        if '인도유랑' in nicknames:
            print("exist")
        else:
            full_urls3.append(urls2)
            print("not exist")
    
    
    except : 
        print(urls2 + "there is no frame")

    


out_df=pd.DataFrame({"unchecked_url":full_urls3})

out_df.to_csv("./uncheckedUrl/"+yesterday_str+"uncheck.txt", index = False)








# slack message

# 어제자 기준
# post_message(myToken,"#unchecked","Hi, I am Dongdang Bot "+yesterday_str)

# 최근 page_range개 기준
post_message(myToken,"#unchecked","약 "+ str((page_range-1)*50) +"개의 게시물을 확인한 결과 "+date.today().strftime('%Y.%m.%d.')+"기준으로 아래의 미답변 url을 찾아냈습니다.")

file = open("./uncheckedUrl/"+yesterday_str+"uncheck.txt", "r")
strings = file.readlines()
print(strings)
file.close()


if len(strings) == 1 :
    post_message(myToken,"#unchecked","All Url is checked")
    print("All Url is checked")
else :
    for i in range(1,(len(strings))) :
        post_message(myToken,"#unchecked",strings[i])

        if i == (len(strings)-1) :
            break

