# 모듈(Modules)
3가지 종류가 있다.
1. 내장 모듈
2. 외장 모듈
3. 사용자 개인 모듈

특징은 다음과 같다.
+ 상수, 변수, 함수, 클래스 코드가 포함되는 파일이다.
+ 모듈은 다른 모듈를 불러와 사용 가능하다.
+ 모듈로 나누면 코드 작성과 관리가 매우 쉬워진다.
+ 공동작업이 편리해 진다.
+ 이미 작성된 코드를 재사용할 수 있다.
## 모듈 생성 밎 호출
내장 `마술 명령어(magic command) %`를 사용
1. 만들기 `(%%writefile 파일명.py)`
2. 불러오기 `(%load 파일명.py)`
3. 파이썬 코드 파일 실행하기 `(%run 파일명.py)`
#
## 1. 모듈 불러오는 기본 형식 `(import)`
#
## 2. 모듈 불러오는 다른 형식
+ `모듈명.` 이 앞부분을 안쓰고 바로 변수, 함수, 그리고 클래스를 직접사용한다.

```python
from 모듈명 import 변수(혹은 함수, 클래스)
```
의 형태로 사용한다.
#
## 3. 모듈명을 별명으로 선언
+ 모튤명이 길거나 여러 모튤을 임포트 할때 별명으로 선언함으로 해결한다.
```python
import module_name as module_nikeName
from moudle_name import function_name as nike_name
```
#
## 4. 모듈을 직접 실행하는 경우와 import한 후 사용 하는 경우
모듈 테스트 할때 직접 모듈을 실행한다.

___직접 수행할때만 실행되는 코드___
```python
if __name__ == "__main__" :
```

#
## 5. 내장 모듈
이미 내장 되있는 모듈\
자세한 내용 : 
https://docs.python.org/3.9/library/
#
## 6. 난수(random) 발생 모듈
+ 모듈명 : random
+ 함수명 : random

0~1 사이의 실수중 임의의 숫자를 생성
```python
import random
random.random()
```
out : #random real number

### functions in `random` module
|함수|설명|사용 예|
|-----|-----|------|
|random()|임이의 `실수` x: 0.0<=x<=1.0|random()|
|randint(a,b)|임의의 `정수` x: a<=x<=b|randint(1,6)|
|randrange(a,b,c)|c만큼 스텝을 띄운,임이의 `정수` x: a<=x<=b|randrang(1,100,2)
|choice(seq)|공백이 아닌 (seq)에서 임의의 항목을 반환|random.choice([1,2,3])
|sample(population,k)|sequence로 된 모집단에서 _중복되지 않는_ k개의 인자 반환|random.sample([a,b,c,d],2)|

예) 두 주사위를 던저 임의의 두 숫자를 반환하라.
```python
import random

a = random.randint(1,6)
b = random.randint(1,6)
print ("주사위 값: {0},{1}".format(a,b))
```
out : 주사위 값: 1,3#임의의 숫자
<br><br>
예)0부터 100까지 임의의 5의 배수를 반환하라.
```python
import random

print (random.randrange(0,101,5))
```
out : 45#임의의 5의 배수
<br><br>
예) 다음 보기에서 임의의 과일을 반환하라.
```python
import random

fruits = ['사과', '배', '망고', '수박']
print (random.choice(fruits))
```
out : 수박#임의의 과일
<br><br>
예) 다음 보기에서 2개의 임의의 인자를 _중복 없이_ 반환하라.
```python
import random

fruits = ['사과', '배', '망고', '수박']
print (random.sample(fruits,2))
```
out : ['배', '수박']#임의의 쌤플
#
## 7. 날짜 및 시간 관련 처리 모듈
실무에서 공통적으로 다루기 힘든 2가지; 날짜와 시간 형식, 한글형식이다.

`datetime` 모듈에는 날짜를 표현하는 `date` 클래스와 시간을 표현하는 `time` 클래스가 있다.

+ 클래서에서 객체를 생성하기
```python
import datetime
date_obj = datetime.date(year, month, day)
time_obj = datetime.time(hour, minute, second)
datetime_obj = datetime.datetime(year, month, day, hour, minute, second) #모듈.클래스명
```
+ 클래스 매서드를 이용하기
```python
import datetime

date_var = datetime.date.date_classemthod() # 모튤.클래스.클래스 메스드
time_var = datetime.time.time_classmethod()
datetime_var = datetime.datetime.datetime_classmethod()
```
+ 오늘 날짜를 표현하라.
```python
import datetime

set_day = datetime.date(2021, 8, 4)
print (set_day)
```
out : 2021-08-04
<br><br>
+ 빼기연산도 가능하다.

예) 충무공 일생의 날을 구하시오. _1545년 4월28일 부터 1598년 12월 16일까지_ 
```python
import datetime

date_brith = datetime.date(1545, 4, 28)
date_death = datetime.date(1598, 12, 16)
diff_days = date_death-date_brith

print (diff_days)
```
out : 19590 days, 0:00:00
<br><br>
데이터 타입 확인하기
```python
type(date_brith)
type(diff_days)
```
out1 : datetime.date
out2 : datetime.timedelta