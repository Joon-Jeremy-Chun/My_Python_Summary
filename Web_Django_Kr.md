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

