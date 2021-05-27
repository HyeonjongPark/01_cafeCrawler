

from selenium import webdriver
import pandas as pd
import time
import urllib
import re
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
# driver.find_element_by_name('id').send_keys('')
# driver.find_element_by_name('pw').send_keys('')

# # 로그인 버튼 클릭
# driver.find_element_by_css_selector('#frmNIDLogin > fieldset > input').click()


제목 = []
텍스트 = []
작성자 = []
작성일 = []
조회수 = []


writer = ["꼴라리", "낭고", "달빛서가", "몽글몽글", "드림아제", "록원", "마녀체력", "멋진인생사랑후", "메신저클레어", "미라클타임", "바다소리", "박하사탕", "비야애미", "빅보스 BigBoss", "빛이 나는 나", "소희", "쉬 라", "스타이글스", "신애인화", "쓰앵k", "아보카도", "안다미로1", "열정정민", "올리브유", "워러보이", "임가지", "제니캬라멜", "지우샤니맘", "쪼브", "초록파프리카", "카쥬", "캐트캐트", "튜닙", "풍경", "헤세르솔트", "Evito", "Lion", "ramee", "인포덱", "블루스카이님", "고캔두", "공부합시다7", "글쓰는리치몬", "김그린21", "꿈 날다", "날", "럭키세븐2030100", "레이첼 초이", "로카텔리", "돈별사", "멋지니", "무사시", "범이성이", "부자여왕님", "빛길", "사랑7", "새벽편지", "알비레오", "여우곰탱이", "열정가득79", "오연아", "온유하다", "워너비가이", "유노혬", "일초남", "정쎄오", "짱이누나", "초록은하수", "페이튼채", "프리라이프 째니", "해피노마드", "현정", "호애애애", "Paiza", "꼬꼬워니", "열빼", "블라밍",
          "열손가락", "럭키걸9", "백곰선생", "마스터Ki", "돈까스킹", "하마쪼", "시간배당", "느림", "복부인짱", "러블리수우", "장하도다", "알러부", "토디토디", "승리의여신", "행복이가득", "베러베러", "finally good", "우뇨", "젠젠", "마흔이되기전에", "비타민맘", "오로라헌터", "alsdhrdus1", "눈빛슈리", "뜨거운안녕", "월1억달성", "홍차의꿈", "봄희야", "활기찬", "속삭이는비", "건물주송연수", "쏭지니", "러너하이", "패이버릿", "뜸북", "여름날", "으쌰비앤비", "코람데오", "르네", "JJ", "55드리", "Begin again", "꿈꾸는최토끼", "지금부터", "ckctg119", "핑크쭈", "로시", "하니비", "작무", "정성을다하기", "하늬바람", "앵이", "행복월천사맘", "슬기로운자유인", "마음은이미부자", "봄날의오후", "새롬", "오곰", "스마트한우", "성현사랑", "6개월프로젝트", "둥그라미", "히말라야", "스몰액션", "패밀리파파", "보물지도님", "비전보드", "박성호", "담담은담담", "SarAH", "guring1015", "젬마", "파사현정", "커터", "cje213"]
#writer = ["시니차니피디" ,"유봉댁" ,"끈기있는 노리더", "양송이스프","해햄햇","다로롱", "청울림"]

urls = []


for geul in writer:
    urls.append("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=29171253&search.media=0&search.searchdate=all&search.exact=&search.include=%3E&userDisplay=50&search.exclude=&search.option=0&search.sortBy=date&search.searchBy=5&search.includeAll=&search.query=" +
                urllib.parse.quote(geul, encoding="cp949") + "&search.viewtype=title&search.page=1")
    try:
        urls.append("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=29171253&search.media=0&search.searchdate=all&search.exact=&search.include=%3E&userDisplay=50&search.exclude=&search.option=0&search.sortBy=date&search.searchBy=5&search.includeAll=&search.query=" +
                    urllib.parse.quote(geul, encoding="cp949") + "&search.viewtype=title&search.page=2")
        urls.append("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=29171253&search.media=0&search.searchdate=all&search.exact=&search.include=%3E&userDisplay=50&search.exclude=&search.option=0&search.sortBy=date&search.searchBy=5&search.includeAll=&search.query=" +
                    urllib.parse.quote(geul, encoding="cp949") + "&search.viewtype=title&search.page=3")
        #urls.append("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=29171253&search.media=0&search.searchdate=all&search.exact=&search.include=%3E&userDisplay=50&search.exclude=&search.option=0&search.sortBy=date&search.searchBy=5&search.includeAll=&search.query=" + urllib.parse.quote(geul, encoding ="cp949") + "&search.viewtype=title&search.page=4")
        #urls.append("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=29171253&search.media=0&search.searchdate=all&search.exact=&search.include=%3E&userDisplay=50&search.exclude=&search.option=0&search.sortBy=date&search.searchBy=5&search.includeAll=&search.query=" + urllib.parse.quote(geul, encoding ="cp949") + "&search.viewtype=title&search.page=5")
        #urls.append("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=29171253&search.media=0&search.searchdate=all&search.exact=&search.include=%3E&userDisplay=50&search.exclude=&search.option=0&search.sortBy=date&search.searchBy=5&search.includeAll=&search.query=" + urllib.parse.quote(geul, encoding ="cp949") + "&search.viewtype=title&search.page=6")
        #urls.append("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=29171253&search.media=0&search.searchdate=all&search.exact=&search.include=%3E&userDisplay=50&search.exclude=&search.option=0&search.sortBy=date&search.searchBy=5&search.includeAll=&search.query=" + urllib.parse.quote(geul, encoding ="cp949") + "&search.viewtype=title&search.page=7")
        #urls.append("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=29171253&search.media=0&search.searchdate=all&search.exact=&search.include=%3E&userDisplay=50&search.exclude=&search.option=0&search.sortBy=date&search.searchBy=5&search.includeAll=&search.query=" + urllib.parse.quote(geul, encoding ="cp949") + "&search.viewtype=title&search.page=8")
        #urls.append("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=29171253&search.media=0&search.searchdate=all&search.exact=&search.include=%3E&userDisplay=50&search.exclude=&search.option=0&search.sortBy=date&search.searchBy=5&search.includeAll=&search.query=" + urllib.parse.quote(geul, encoding ="cp949") + "&search.viewtype=title&search.page=9")
        #urls.append("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=29171253&search.media=0&search.searchdate=all&search.exact=&search.include=%3E&userDisplay=50&search.exclude=&search.option=0&search.sortBy=date&search.searchBy=5&search.includeAll=&search.query=" + urllib.parse.quote(geul, encoding ="cp949") + "&search.viewtype=title&search.page=10")
        #urls.append("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=29171253&search.media=0&search.searchdate=all&search.exact=&search.include=%3E&userDisplay=50&search.exclude=&search.option=0&search.sortBy=date&search.searchBy=5&search.includeAll=&search.query=" + urllib.parse.quote(geul, encoding ="cp949") + "&search.viewtype=title&search.page=11")
        #urls.append("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=29171253&search.media=0&search.searchdate=all&search.exact=&search.include=%3E&userDisplay=50&search.exclude=&search.option=0&search.sortBy=date&search.searchBy=5&search.includeAll=&search.query=" + urllib.parse.quote(geul, encoding ="cp949") + "&search.viewtype=title&search.page=12")
        #urls.append("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=29171253&search.media=0&search.searchdate=all&search.exact=&search.include=%3E&userDisplay=50&search.exclude=&search.option=0&search.sortBy=date&search.searchBy=5&search.includeAll=&search.query=" + urllib.parse.quote(geul, encoding ="cp949") + "&search.viewtype=title&search.page=13")
        #urls.append("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=29171253&search.media=0&search.searchdate=all&search.exact=&search.include=%3E&userDisplay=50&search.exclude=&search.option=0&search.sortBy=date&search.searchBy=5&search.includeAll=&search.query=" + urllib.parse.quote(geul, encoding ="cp949") + "&search.viewtype=title&search.page=14")
        #urls.append("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=29171253&search.media=0&search.searchdate=all&search.exact=&search.include=%3E&userDisplay=50&search.exclude=&search.option=0&search.sortBy=date&search.searchBy=5&search.includeAll=&search.query=" + urllib.parse.quote(geul, encoding ="cp949") + "&search.viewtype=title&search.page=15")
    except:
        print("first page.")

for url in urls:
    driver.get(url)

    parsed = urlparse.urlparse(url)
    real_writer = parse_qs(parsed.query, encoding='cp949')['search.query']

    driver.switch_to_frame("cafe_main")

    for i in range(0, 50):
        try:

            # 제목.append(driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/table/tbody/tr["+str(i+1)+"]/td[1]/div[2]/div/a[1]/span").text)
            텍스트.append(driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[5]/table/tbody/tr["+str(i+1)+"]/td[1]/div[2]/div/a[1]").text)
            작성자.append(real_writer)
            작성일.append(driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[5]/table/tbody/tr["+str(i+1)+"]/td[3]").text)
            조회수.append(driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[5]/table/tbody/tr["+str(i+1)+"]/td[4]").text)
        except:
            print("under 50 posting")
            break


# driver 종료
driver.quit()

df = pd.DataFrame({"title": 텍스트, "writer": 작성자, "date": 작성일, "viewCount": 조회수})
#df.to_excel("naverCafeReply_A_"+datetime.today().strftime("%m%d")+".xlsx", index = False)
df.to_excel("D:/workspace/010_crawler_naverCafe2/data/users/naverCafeReply_A_" +
            datetime.today().strftime("%m%d")+".xlsx", index=False)
df.to_excel(
    "D:/workspace/010_crawler_naverCafe2/data/naverCafeReply_A.xlsx", index=False)
