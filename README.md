# 01_cafeCrawler

1. slack - token 발급 => slack_token.txt에 private 하게 저장

2. naver_id와 naver_pw 각각을 private하게 txt에 저장

3. page_range = 11 지정 => 원하는 페이지의 article 넘버 스크래핑 후, 원하는 url 과 paste

4. (11-1) * 50 개의 article 만큼 각 article에 방문해서, 댓글 단 유저의 닉네임들을 파싱

5. 각 article에 특정 user의 닉네임이 존재하지 않는 경우, 그 url을 return해주는 조건문 생성

6. 로컬에 파일 저장 

7. 원하는 workspace의 slack channel에 로컬에 저장한 파일을 읽어 봇이 메시지를 던질 수 있도록 post_message 함수 생성 
