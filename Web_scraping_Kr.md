# Web scraping 
_Jupyternotebook base_
#
## `webbrowser` library 사용.
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
## `urllib` library 사용.
사용하여 데이터 다운 해보기
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
- 예외 처리 `try`를 사용하여
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