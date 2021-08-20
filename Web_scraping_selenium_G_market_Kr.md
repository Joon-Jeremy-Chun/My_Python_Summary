# Web scraping practice
G market 에서 소비자 가격과 판매가격을 가져온다. 그리고 각 아이템의 할인율을 만들어본다.

_Jupyternotebook base_\
_chromedriver base_\
_파일 경로:C://Myexam//chromedriver//_ 

## 패키지
```py
import requests
from selenium import webdriver
import time
```
#
## 1. Scraping
1. G market 배스트셀러 패이지 크롤링
2. 데이터 전처리( None 을 원가로 측정)
3. 할일율 계산 컬럼 추가
4. 할인율 50%이상인 상품만 필터링
<br><br>
- web연결밎 확인
```py
driver = webdriver.Chrome("C://Myexam//chromedriver//chromedriver.exe")
url = "http://corners.gmarket.co.kr/Bestsellers"
```
- elements select\
_web 개발자도구를 사용해서 원하는 위치 확인_
```py

