# Selenium 이용해서 데이터 가져오기
_Jupyternotebook base_
+ chromedriver download (https://sites.google.com/a/chromium.org/chromedriver/downloads)
+ 원래는 프라우져 자동화 목적 툴로 테스팅을 목적으로 만들어졌다.
```py
!pip install selenium
from selenium import webdriver
driver = webdriver.Chrome("C:\\Myexam\\chromedriver\\chromedriver.exe")
```
#
## 기본 컨트롤
+ url 시작하기: 반드시 http를 포함해야한다.
```py
driver.get("https://www.naver.com/")
```
+ 원도우 사이즈 조절
```py
driver.set_window_size(1024,768)
```
+ 스크롤 위치 이동
```py
driver.execute_script("window.scrollTo(300,400);")
```
#
## Alert 다루기
+ alert 체크 코드
```py
try:
    alert = driver.switch_to.alert
    print(alert.text)
except:
    print('alert 없음')
```
+ alert 만들고 후에 위 코드 실행해보기
```
driver.execute_script("alert('test');")
```
#
## 버튼 클릭하기
_`never.com` 메인의 버튼의 class는 `.btn_submit`이다._
```py
driver.find_element_by_css_selector(".btn_submit").click()
```
#
## 