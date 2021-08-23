# Single web site analysis
1. youtube-rangking 사이트에서 카테고리별 구독자수, 체널수, 비디오수를 수집해온다.
2. 데이터 처리
3. 저장: 엑셀파일로 저장
4. 시각화
#
## 대상 site 분석
1. 데이터 위치 파악(경로)
#
## 유트브 랭킹 데이터 (youtube-rank.com)
```py
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
```
+ 웹 열기
```py
browser = webdriver.Chrome("C://Myexam//chromedriver//chromedriver.exe")
url = "https://youtube-rank.com/board/bbs/board.php?bo_table=youtube"
browser.get(url)
```
+ 데이터 가져오기 & 정리
```py
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
```
+ 원하는 데이터의 테그 추출하기
+ `tr`
```py
channel_list = soup.select('tr')

# 몃개인지 확인
# 첫번째 데이터 확인
print(len(channel_list), '\n')
print(channel_list[0])
```
out : 102\
out : #첫번째 데이터
+ tr 태크 확인 
+ 처음 2행 제외하기
+ `form` `table` `tbady` `tr`
```py
channel_list = soup.select('form  table  tbody  tr')
#확인
print(len(channel_list))
```
out : 100
+ 데이터 구조 확인하기
```py
channel_check = channel_list[0]
print (channel_check)
```
#
## 데이터 분류
+ 카테고리, 채널명, 구독자 수, view 수, 동영상 수 추출

1. `p` 테그 안에 `class = category` 정보 추출
```py
category = channel_check.select('p.category')[0].text.strip() 
#.strip()을 하는 이유는 문자열 앞뒤의 공간과 개행문자을 삭제하려고
print (category[0:5])
```