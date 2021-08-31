# MySQL DB 파이썬 연동
_jupyternotebook base_\
데이터 다루기 기본 개요

1. 라이브러리 가져오기(pymysql)
2. 접속하기
3. 커서 가져오기
4. SQL 구문 만들기(CRUD SQL 구문등)
5. SQL 구문 실행 하기
6. DB에 complete 하기 (commit)
7. DB연결 닫기

| 순서 | python 명령어|
|------|--------------|
|라이브러리 가져오기| import pymysql|
|접속하기| connect()|
|커서 가져오기| cursor()|
|SQL 구문|select,update,delete,insert|
|SQL 구문 실행|execute()|
|DB에 commit|commit()|
|DB 닫기|close()|


#

## 1. 라이브러리
```py
!pip install pymysql
```