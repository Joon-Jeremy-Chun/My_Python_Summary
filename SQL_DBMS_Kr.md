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
## 데이터 베이스의 특징
- 데이터의 무결성(Integrity)
    1. 데이터 베이스 안에는 오류가 없어야 한다.
    2. 제약 조건(Constrain)이라는 특성을 가짐

- 데이터의 독립성
    1. 데이터베이스 크기 변경하거나 테이터 파일 저장소 변경 시 기존에 작성된 응용프로그램은 전혀 영향을 받지 않아야 한다.
- 보안
    1. 허가된 사람들만 접근할 수 있어야함
    2. 접근할 때도 사용자의 계정에 짜라서 다른 권한을 가짐
- 데이터 중복의 최소화
- 응용프로그램 제작 및 수정이 쉬워짐
- 데이터의 안전성 향상
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
- 각 데이터베이스DB는 고유한 이름을 가지고 있다.
- 저장할 정보는 Table이라는 형식에 맞춰 저장
- 행 : low, record
- 열 : column, field
- 열이름은 테이블 내에서 고유해야 한다.
- 기본 키 : Primary Key (PK), null값이 안되며 고유해야한다. 예)순번 
- 외래 키: foreign key 예) 고객이 주문 할 때 주문 테이블.
- 외래 키 필드 : 두 테이블의 관계를 맺어주는 키
#
## 데이터 활용
1. 주로 select문 사용해 데이터 활용
    - 사용할 데이터 베이스 선택
    - select 열이름 from 테이블 이름 [where 조건]
    -  새로운 테이블 생성
    - 테이블 삭제 : drop table 이름
2. View : 가상 테이블 
    - 실제 행 테이터를 가지고 있지 않음
    -  보안면에서 안정되다.
    -  데이터를 읽을때 효율적이다.
3. 스포어드 프로시저(Stored Procdure) : SQL문을 하나로 묶어서 편리하게 사용하는 기능
4.  트리거(Trigger) : 테이블에 부착되어 테이블에 insert나 update 또는 delete 작업이 발생되면 실행되는 코드
    - 예) 테이블에 변화가 있을때 메세지를 보낸다.
5. 백업과 복원
    - 백업 현재의 데이터 베이스를 다른 매체에 보관하는 작업
    - 백업과 복원은 DBA(DataBase Administrator)가 해야 할 가장 중요한 일

#
## SQL 기본
### 1. select 문
```sql
select select_expr
    from table_references
    where where_condition
    group by {col_name : expr : position}
    having where_condition
    order by {col_name : expr : position}
```
```sql
select 열 이름
from 테이블이름
where 조건
```
### 2. use 문
- 사용할 데이터베이스 지정
```SQL
use 테이터베이스이름;
```
### 3. select와 from
- select * from 테이블; - 모두불러온다.
- select (원하는 열) from 테이블; 원하는 열만 불러온다.
### 4. 주석(Remark)
- 한 줄 주석: `--`한 줄 주석
- 여러 줄 주석 `/*` 내용 `*/`
### 5. show 명령어
```sql
show databases;
show tables;
show table status;
```
### 6. describe 명령어
-field와 타입을 알려준다.
```
describe 데이터베이스;
```
### 7. where 조건
예)
```sql
select * from employees;
select * from employees where last_name = 'Peha';
select * from employees where last_name = 'Peha' and first_name = 'Aamer' ;
```
