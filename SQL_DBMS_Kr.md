# DBMS와 SQL
## DBMS
Data Base Management System (DBMS)
목적 
- Data 저장
- Data 검색
- 여서사람 혹은 프로그램이 동시간 데이터 공유
## 데이터 배이스 형식
1. 파일 system 
- txt, excel
- 중복 데이터 (저장공간 낭비 - 예를 들어 같은 고객정보,같은 날짜, 다른 주문정보들)

2. DBMS
    1. RDBMS - _`Table 형식이다.`_ 중복 데이터 낭비를 막기위해서

    2. NoSQL
-RDBMS 연동 사용, __빅테이터__

## RDBMS 종류와 특징
- `oracle` - 오라클 사에서 만든, 현재 우리나라에 많이 사용되고 있다. 
- `MSSQL` - 마소에서 만든 window base
- `MySQL` - open source, 다양한 프로그램 언어 
- `SYBASE` - 클라이언트 서버용 분산처리에 좋음
- `DB2` - 금융쪽에서 사용한는
- `마리아DB` - open source
- `SQLite` - 간단하다.

## DB 모델링 과정
1. DB 생성
2. Table 생성
3. Tables 관계 설정

## DB 레이아웃만든다.
1. 필드명(이름) 필드타입 필드길이
2. 제약조건
#
## SQL(Structured Query Language )
여러 데이터 베이스들의 ~sql 표준 언어(SQL)와 특징(혹은 각베이스들의 특징 언어) 언어로 구성되어있다.
1. DML (Data Manipulation Language)
- select
- update
- insert
- delete

2. DDL (Data Definition Language)
- 데이터베이스 정의 - create DataBase ...
- 데이블 정의 - create table ...
- 뷰(view): 가상 테이블 개념
- 인텍스
- 생성(create) 삭제(Drop) 변경(Alter)
3. DCL (Data Control Language)
- 사용자 권한 부여, 혹은 제한 할때.
- Grant, Revoke, Deny

#
## MySQL 노트
- cmd 창에서 
#
## 데이터베이스 모델링과 필수 용어
- 저장할 정보는 Table이라는 형식에 맞춰 저장
- 행 : low, recod
- 열 : column
- 기본 키 : Primary Key (PK), null값이 안되며 유니크해야한다. 예)순번 