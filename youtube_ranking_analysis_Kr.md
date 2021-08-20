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
from bs4 imoprt BeautifulSoup
import time
import pandas as pd
```
+ 웹 열기
```py
browser = webdriver.Chrome("C://Myexam//chromedriver//chromedriver.exe")
url = "https://youtube-rank.com/board/bbs/board.php?bo_table=youtube"
browser.get(url)
```
+ 데이터 가져오기
```py
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
```
