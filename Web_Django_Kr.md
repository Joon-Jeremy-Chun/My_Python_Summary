# 웹 라이브러리 Django

Model, View, Controller
(MVC) 을 기본으로 한 프레임 워크

Model, View, Template
(MVT) 패턴으로 되있다.

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
## 프로젝트 뼈대 만들기
프로젝트 뼈대 만들기 순서 명령
1. mysite라는 프로젝트 생성:
기본셋팅을 한다.(기본 파일 밎 코드 자동 생성)
```

django-admin startproject mysite
```
- 위 프로젝트명 mysite -> projectsite 변경
```
move mysite projectsite #폴더 위치에서
```
2. polls라는 애플리케이션 생성: 역시 기본세팅으로 기본 파일 밎 코드가 생성된다.
```
python manage.py startapp polls
```
3. 설정 파일을 확인 및 수정
```
notepad settings.py
```
4. 데이터베이스에 기본 테이블을 생성
```
python manage.py migrate
```
5. 현재까지 작업을 개발용 웹 서버로 확인
```
python manage.py runserver
```
#
##