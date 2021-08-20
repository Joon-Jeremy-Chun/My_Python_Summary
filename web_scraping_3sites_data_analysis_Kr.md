# multi web sites data analysis
1. 멜론 벅스 지니 의 사이트의 서비스, 순위, 타이틀, 가수 정보 수집
2. 데이터 처리 `pandas`library 사용
3. 엑셀파일로 저장 각각저장
4. 각 파일데이터를 하나로 저장
#
## 대상 site 분석
1. 데이터 위치 파악(경로)
#
## MelOn site crawling
```py
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("C://Myexam//chromedriver//chromedriver.exe")
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

