# 웹 라이브러리 Django 노트

Model, View, Controller
`(MVC)` 을 기본으로 한 프레임 워크

Model, View, Template
`(MVT)` 패턴으로 되있다.

장고에서는 View를 Template, Controller를 View라고 한다.

`Model`은 데이터베이스에 저장되는 데이터를 의미

`Template`은 사용자에게 보여지는 UI 부분 (html로 만들어 졌다)

`View` 간단히 말해 기능 : 실질적으로 프로그램 로직이 동작하여 데이터를 가져오고 적절하게 처리한 결과를 템플릿에 전달하는 브릿지
#
## 장고 설치하기
```
pip install Django
```
확인하기
```
python -m django --version
```
#
## application 개발 방식
1. 프로젝트 뼈대 만들기
2. 모델 코딩하기
3. URLconf 코딩하기
4. 템플릿 코딩하기
5. view 코딩하기

#
## 1. 프로젝트 뼈대 만들기
프로젝트 뼈대 만들기 순서 명령
1. mysite라는 프로젝트 생성:
기본셋팅을 한다.(기본 파일 밎 코드 자동 생성)
```

django-admin startproject mysite
```
<br><br>
- 위 프로젝트명 mysite -> projectsite 변경
```
move mysite projectsite #폴더 위치에서
```
<br><br>

2.  polls라는 애플리케이션 생성: 역시 기본세팅으로 기본 파일 밎 코드가 생성된다.
```
python manage.py startapp polls
```
<br><br>

3. 설정 파일을 확인 및 수정
- `settings.py`에서 보통 4가지의 셋팅을 한다.
- `ALLOWED_HOSTS`, `INSTALLED_APPS`, `databases`, `TIME_ZONE`
```
notepad settings.py
```
- 호스트에 내 아이피와 localhost '127.0.0.1' 을 추가 한다. _cmd 커맨트창에 ipconfig 내 아이피 확인_
- apps 위에서 추가한 polls를 추가한다. `'polls.apps.PollsConfig'`
- timezone 안에 Asia/Seoul로 변경
<br><br>
4. 데이터베이스에 기본 테이블을 생성
```
python manage.py migrate
```
- 위 명령어후 인증 사용자 계정 auth(author)등 권한생성 (table 생성)
- db.sqlite3 자동으로 생성된다.
- database에 무엇이 있는지 알려면 `sqlite3 db.sqlite3`
<br><br>

5. 현재까지 작업을 개발용 웹 서버로 확인
```
python manage.py runserver
```
- 서버를 실행하고 브라우저를 통해 서버 접속
- 서버용으로 새로운 cmd 실행 하는것이 편리
#
## Admin 사이트 접속
```
python manage.py createsuperuser
```
그뒤 절차에 따라 username email password를 설정

- 사이트 127.0.0.1:(설정한 번호)/ admin에가서 로그인
#
## 골격 생성
어플리케이션을 MVT 패턴 방식으로 개발할 수 있도록 골격 생성
```
tree /F projectsite
```
위 명령어를 시행하면 데이터베이스,셋팅,applications등 연결 구조를 볼 수 있다.
#
<br><br>
노트
# 장고 웹 프레임워크
설문조사 웹 만들기
## Model coding
- Questions choice 두개의 테이블이 필요

-아나콘다에서 python manage.py makemigrations : 실행후 polls에 migrations 폴더밎 파일이 생성됨

- python manage.py migrations : 데이터베이스에 테이블 생성

- 브라우져에 `http://127.0.0.1:8000/admin/` admin으로 들어가면 위에서 만든 아이디 정보와 현재 만든 questions 와 choice 부분이 만들어져있다.
<br><br>
## View 및 Template



#

___노트 mini porject 1___
# 장고 mini project ToDolist 만들기
1. ToDoList 미니프로젝트 분석
    1. 현황 분석
    2. 테이터 분석(식별, 흐름)

2. ToDoList 미니프로젝트 설계
    1. Model
    2. URLconf
    3. Template
    4. View
#
## 구상하기
- ### Model(models.py): 테이블 구성
1. 메모내용; (반드시 아래옵션은 아니여도된다.)\
 varchar 타입으로 (가변적으로 사용)\
 길이 : 255
2. 메모 완료여부\
boolean 타입(True,False)
<br><br>
- ### URLconf
1. URLconf (urls.py)\
 path('',view.index,name=index)\
path('creatTodo/',views) 메모하기\
path('doneTodo/',views) 완료하기
2. view (views.py) 와 html)\
 `index()`함수와 `creatTodo()`, `doneTodo()`
3. template(template/app/*.\
 `index.html` 필요\
 DB에 Data 메모넣기
 
#
##  MVT 코딩 순서대로 실행
1. 프로젝트 뼈대
2. 모델 코딩 (models.py, admin.py)
3. URLconf (url.py)
4. 템플릿 (templates/ 하위 *.html)
5. View (views.py)
#
## 1. 프로젝트 뼈대 만들기
1. 폴더에 ToDoList 라는 프로젝트 생성 : `django-admin startproject ToDoList`
2. my_to_do_app 이라는 애플리케이션 _프로젝트안에 생성_ : `python manage.py startapp my_to_do_app`
3. 설정 파일을 확인 및 수정 : `notepad setting.py`
- 수정할 내용은 `ALLOWED_HOSTS`, `INSTALLED_APPS`, `databases`, `TIME_ZONE` 4개
- `INSTALLED_APPS`에 내가 추가한 `'my_to_do_app',`을 추가하며 콤마를 잊지말자.
4. 데이터베이스에 기본 테이블 생성 : `python manage.py migrate` 실행하면 `db.sqlite3`가 생성된다.
- `migrate`는 데이터베이스에 변경사항이 있을 때 반영해주는 명령. 커맨트창에 _Applying ~~~ ... ok 가 뜬다._
5. 현재까지 작업을 _개발용 웹_ 서버로 확인 : `python manage.py runserver`로 서버를 실행하고 프라우져로 접속하여 로켓로고 확인하면 ok

## 1.2 admin 등록하기 접속하기
1. manage.py 가 있는 폴더위치에서 다음을 실행 : `python manage.py createsuperuser`
2.순서에따라 작성후 /admin에 접속해본다.

## 1.3 애플리케이션을 MVT 패턴 방식으로 개발할 수 있도록 골격 생성
1. `C:\\MyTest>tree /F ToDoList` 

## 2.  model 코딩
모델 작업은 테이터베이스에 테이블을 생성하는 작업.\
my_to_do_app에서 model 코딩 클레스 생성 :문자길이 버튼 등등

1. 테이블을 정의 한다. : `notepad models.py`
- (장고뼈대 만들때 이미 존재) 
- 아래 내용을 코딩
    1. class `Todo()` 생성 
    2. content 는 255으로 설정 isDone 은 Boolean으로 완료 버튼사용
2. admin에 등록
- 위에 정의한 models.py 가 admin에 보이도록  admin.py에 등록
```py
from my_to_do_app.models import Todo
```
3. 데이터베이스에 변경이 필요한 사항을 추출함 : `python manage.py makemigrations`
- ToDoList 폴더로 올라간후 실행(데이터 베이스 위치)
- 위 명령에 의해 my_to_do_app/migrations 폴더와 하이 마이크레이션 파일들이 생김
4. 데이터베이스에 변경사항을 반영함 : `python manage.py migrate`
- 데이터 베이스에 테이블 생성
- 데이터 베이스에가서 테이블 목록을 확인하면 `my_to_do_app_todo` 가 생김
5. 현재까지 사항을 재발용 웹 서버로 실행 : `python manage.py runserver`
- Todos 목록이 서버에 생김
## 3. URLconf 코딩

#
#
___노트 mini porject 2___
# 장고 mini project RestaurantShare 만들기
### MVT 코딩 순서
1. 프로젝트 뼈대 만들기
2. 모델 코딩하기
3. URLconf 코딩하기
4. 템플릿 코딩하기
5. View 코딩하기
#

### 데이터 식별
- 카테고리식으로 이름 .. (한식, 중식, ...)
- 맛집이름 `Restrurant_name`
- 링크 `Restrurant_link`
- 상세설명 `Restrurant_content`
- 장소키워드 `Restrurant_keyword`
#

### 프로젝트 뼈대 만들기
- RestaurantShare 프로젝트 만들기
- shareRes 와 senㄸemail 두개의 앱만들기
- 설정확인
- 데이터 기본테이블 생성
- 현재까지 작업 개발용 웹 서버로 확인
#

### admin 계정 생성
#
### 뼈대 확인
`tree /F ResturantShare`
#
### model 코딩
