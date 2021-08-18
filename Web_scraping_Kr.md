# Web scraping 
_Jupyternotebook base_
#
## 검색
 `webbrowser` library 사용하여
특정 검색어 특정 사이트 검색밎 열기
- 특정 `web` 열기
```python
import webbrowser
url = 'www.naver.com'
webbrowser.open(url)
```
out : True\
*url(Uniform Resource Location)
<br><br>
+ 특정`web`에서 특정 `검색어`
```py
naver_search_url = "https://search.naver.com/search.naver?query="
search_word = '증권'
url = naver_search_url + search_word

webbrowser.open(url)
```
out : True
<br><br>
+ `for`문 이용 여러 단어 리스트 검색 
```py
naver_search_url = "https://search.naver.com/search.naver?query="
word_list = ['증권','금융']

for i in word_list :
    url = naver_search_url + i
    webbrowser.open(url)
```
out : True\
#리스트 단어가 검색된다.
#
## 데이터 다운
 `urllib` library 사용하여 데이터 다운 해보기
- 라이브러리 지정
- img,html위치 지정
- 저장명과 위치 지정\
_C:\\Myexam 폴더에_
```py
import urllib.request as req

img_url = "http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg"
html_url =  "http://google.com"

save_path1 = "C:\\Myexam\\test1.jpg"
save_path2 = "C:\\Myexam\\index.html"
```
<br><br>
+ 예외 처리 `try`를 사용하여 처리가 안될때 대비

- `.urlretrieve( #url, #경로와 이름)` 사용해 다운 한다.

```py
try:
 file1, header1 = req.urlretrieve(img_url, save_path1)
 file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
 print("Download failed.")
 print(e)
else:
 # Header 정보 출력
 print(header1)
 print(header2)

```
#
## 웹 페이지의 html 소스 가지고 오기

```py
import requests

r = requests.get("https://www.google.co.kr")
r
```
out : <Response [200]> _잘 됬으면 나오는 output_

- 일부분만 출력하기
- 두가지 방법
```py
r.text[0:100]
```
```py
import requests
html = requests.get("https://www.google.co.kr").text
html[0:100]
```
#
## 데이터 찾고 추출하기 ex1
`Beautiful Soup` library 사용하여 파싱하고 태그나 속성을 통해 원하는 데이터 추출하기

- 테스트용 html
- `BeautifulSoup` 사용하기
```py
from bs4 import BeautifulSoup

#test code
html = """<html><body><div><span>\
<a href=http://www.naver.com>naver</a>\
<a href=http://www.google.com>google</a>\
<a href=http://www.daum.net>daum</a>\
</span></div></body></html>"""

#BeautifulSoup에 html소스 파싱
soup = BeautifulSoup(html, 'lxml')
soup
```

+ `.prettify()` 함수를 사용해서프린트해본다.
```py
print(soup.prettify())
```
out : #정리되서 나옴
<br><br>
- 해당 `'태그'`가 있는 _첫번째_ 요소를 찾는다.
```py
soup.find('a')
```
out : `<a href="http://www.naver.com">naver</a>`

<br>

+ `get_text()`를 사용하여 안에 있는 텍스트만 불러오기
```py
soup.find('a').get_text()
```
out : 'naver'
<br><br>
- `find_all()`을 사용하여 모든 요소를 반환 하기
- 리스트 형식으로 반환 된다.
```
soup.find_all('a')
```
out : [`<a href="http://www.naver.com">naver</a>,
 <a href="http://www.google.com">google</a>,
 <a href="http://www.daum.net">daum</a>`]
 <br><br>
 - `for`문을 이용하여 텍스트만 반환한다.
 - `get_text()`는 리스트에 적용할 수 없음으로
 ```py
site_names = soup.find_all('a')
for site_name in site_names :
  print(site_name.get_text())
```
out : \
naver\
google\
daum
#
## ## 데이터 찾고 추출하기 ex2
```py
from bs4 import BeautifulSoup

#테스트용 html code

html2 = """
<html>
 <head>
  <title>작품과 작가 모음</title>
 </head>
 <body>
  <h1>책 정보</h1>
  <p id="book_title">토지</p>
  <p id="author">박경리</p>
  
  <p id="book_title">태백산맥</p>
  <p id="author">조정래</p>

  <p id="book_title">감옥으로부터의 사색</p>
  <p id="author">신영복</p>
 </body>
</html>
"""

soup2 = BeautifulSoup(html2, 'lxml')
```

- `title 태그` 요소 찾아오기
```py
soup2.title
```
out : `<title>작품과 작가 모음</title>`
<br><br>
- `body` 전체 혹은 body 안의 `특정 요소`를 가져올 수 있다.
```py
soup2.body
```
out : # body 전체
```py
soup2.body.h1
```
out : `<h1>책 정보</h1>`