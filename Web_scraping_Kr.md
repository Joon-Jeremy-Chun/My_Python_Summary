# Web scraping 
_Jupyternotebook base_

### 주의 사항
1. 웹페이지의 소스코드에서 데이터를 얻기 위한 `규칙` 확인
2. 웹 사이트에 너무 빈번하게 접근 금지
3. 언제든지 예고 없이 `변경`될 수 있다.
4. 인터넷 상에 곤개된 테이터라고 하더라고 `저자권(copyright)`이 있는 경우가 있다.

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
`BeautifulSoup` library 사용하여 파싱하고 태그나 속성을 통해 원하는 데이터 추출하기

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
<br><br>

- 코드의 `p태그` 요소 중 `id`가 `book_title`인 속성을 갖는 _첫 번째_ 요소만 반환
- `find_all()`로 역시 모든 값을 리스트에 저장 찾을 수 있다.
```py
soup2.find('p',{"id":"book_title"})
# p태그의 id key의 book_title이라는 벨류
```
out : `<p id="book_title">토지</p>`
<br><br>
practic) 책이름 / 저자 형식으로 나타내기
```py
book_titles = soup2.find_all('p',{'id':'book_title'})
book_authors = soup2.find_all('p',{'id':'author'})

for book_title, book_author in zip(book_titles, book_authors):
    print(book_title.get_text() + ' / ' + book_author.get_text())
```
out :\
토지 / 박경리\
태백산맥 / 조정래\
감옥으로부터의 사색 / 신영복
# 
## `CSS` 선택자`(selector)`를 이용
#
## 줄바꿈으로 가독성 높이기
#
## 실제 크롤링 예제 - ranking list 가져오기
_Aug/19/2021_
- alexa.com에서 한국 사이트 순위 가져오기
1. 사이트를 열어 분석한다.
2. 원하는 데이터 위치 확인

```py
import requests
from bs4 import BeautifulSoup

#사이트
url = "https://www.alexa.com.topsites/countries/KR"

#데이터를 text형태로 가져와 lxml 정리처리
html_website_ranking = requests.get(url).text
soup_website_ranking = BeautifulSoup(html_website_ranking, 'lxml')


#일단 분석해서 내가 원하는 위치가 어디인지 확인 한다.
# p태그의 요소 안에 a 테그의 요소만 저장

website_ranking = soup_website_ranking.select('p a')
#a 는 하이퍼 링크를 걸어주는 테그

# 텍스트만 저장
website_ranking_address = [website_ranking_element.get_text() for website_ranking_element in website_ranking[1:]]
```
+ 불러오기 10항
```py
print("[Top Sites in South Korea]")
for k in range(10) :
    print ('{0} - {1}'.format(k+1, website_ranking_addres[k]) )

```
out : #10 웹 순위 (Aug/19/2021기준)
#
## 실제 크롤링 예제 - 이미지 저장