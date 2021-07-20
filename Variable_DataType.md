# 변수 (Variable)
반복되는 자료형이나 데이터를 변수로 지정하여 효율적으로 사용할 수 있다. _변수는 메모리(memory)에 저장됨으로 영구저장이 아니다._

## 1. 변수 선언과 대입
1. 변수 선언을 가장 먼저 해야한다.

예) a변수는 정수형이다: `int a`

2. 그뒤 변수에 데이터를 대입(저장)해야한다

예) 변수a에 10을 대입(저장)한다. `a=10` 

_C 나 JAVA는 변수 선언을 반드시 해야하는데 python이나 R은 자동으로 인지한다._

## 2. 기억해야할 변수 이름의 규칙들
 + 변수명은 `문자`, `숫자`, 그리고 `밑줄기호`(_)를 이용한다.
 + 숫자로 시작하는 변수를 만들수 없다.
 + 대소문자를 구분한다.
 + 공백을 포함할 수 없다. _왜냐하면 다음항이 명령어 일경우와 논리 충돌_
 + 밑줄 `_` 이외의 기호는 변수로 사용할 수 없다. _명령어중 논리 충돌_
 + 예약어(Reserved word)는 변수명으로 이용할 수 없다. _저장된 의미와 논리 충돌_

# 문자열(string) `str`
+ 문자열을 표시하기 위해서는 `큰따옴표(")`나 `작은따옴표(')`를 문자열 앞뒤에 쓴다.

```python
string1 = "Seeing is believing"
string2 = 'We can see when we believe'
print (string1)
print (string2)
```
+ 따옴표를 같이 집어 넣을려면 
```python
string3 = ""Seeing is believing""
string4 = "'We can see when we believe'"
print (string3)
print (string4)
```
+ 두개 이상의 따옴표를 넣으려면 앞뒤로 3겹의 따옴표들 `"",''`을 넣는다.
```python
string5 = """"Seeing is believing" but I think 'We can see when we believe'"""
print (string5)
```

문자열 끼리면 더하기`(연결)` 곱하기`(반복)`도 가능.
```python
a = 'I '
b = 'l'
c = 'o'
d = 'v'
e = 'e '
f = 'you.'
print (a+b+c+d+e+f)
print (a+b+c*10+d+e+f)
```
# 리스트(list)

 몃가지 데이터 처리 종류들이 존재한다.
 1. 리스트 `[]`
 2. 튜플   `()`
 3. 딕션너리 `{key1:value,key2:valu}`
 4. 세트 `(set)`

## 리스트 만들기
+ 대괄호`[]`를 이용하여 만든다.
+ 각 항목의 데이터 타입은 같이 않아도 됨.
```python
ex1 = [1, 'I', Ture, [1,2,3]]
```
+ 인텍스(index) 형태로 데이터가 저장된다.
+ 데이터는 입력한 _순서_ 대로 지정된다. 항목은 콤마`(,)`로 구분된다.

_순서 기준은 0,1,2,... 0부터 시작한다._

_또한 가장 마지막은 -1로 시작하여 거꾸로 인텍스가 가능하다._
+ 대괄호 않에 아무것도 쓰지 않으면 빈 리스트가 만들어진다. 그리고 형태는 리스트이다.

### 1. 리스트 활용의 예
```python
love_principles = ['patient', 'kind', 'unselfish']
love_principles[0]
love_principles[1]
love_principles[2]
love_principles[-3]
love_principles[-2]
love_principles[-1]
```
_각각 부여된 순서 숫자를 index라 한다._

### 2. 리스트 데이터 변경 예
다음과 같은 형태로 데이터를 변경 가능하다.
```python
love_principles[2] = 'not conceided'
```
## 리스트 다루기
### 1. 문자열`(string)`과 마찬가지로 `연결(+)`과 `반복(*n)` 이 가능하다.
```python
list1 = [1,2,3,4]
list2 = ['a','b','c','d']
print (list1+list2)
print (list1*2+list2)
```
### 2. 리스트중 일부 데이터 가져오기
+ `list[i]`는 `i`의 항목을 불러옴. _*0부터 인텍스 시작_
+ `list[i_start : i_end ]`
+ `list[i_start : i_end : i_step]` _*step 증가 단계_

``` python
love_principles = ['patient', 'kind', 'unselfish', 'forgive']
love_principles[0:3]
love_principles[:3]
love_principles[0:4]
love_principles[:]
love_principles[0:4:1]
love_principles[0:4:3]
```
### 3. 리스트 항목 삭제
`del list[i]`를 이용한다.
```python
love_principles = ['patient', 'kind', 'unselfish', 'forgive']
del love_principles[0]
print (love_principles)
```
_*`del`하게되면 `index의 order`가 빈공간을 마추어 다시짜여진다._
### 4. 리스트에서 특정 데이터 존재여부 확인
`data in list`를 이용한다.
```python
love_principles = ['patient', 'kind', 'unselfish', 'forgive']
print (1 in love_principles)
print ('kind' in love_principles)
```
### 5. 기타 메서드`(method)`
여러종류의 메스드가 존재한다.

# 튜플(Tuple)
+ 리스트와 유사하게 데이터를 하나로 묶는데 소괄호`()` 이용. (괄호 없이도 입력)
+ ___리스트와 매우 큰 차이점은 변경이 불가능하다.___
+ 그래서 특정 메스드는 불가능하다.
+ 장점은 테이터가 변한지 않으니 용량가변성이 없어 메모리나 용량을 최소화할 수 있다. 즉 회전속도에 매우 유리하다.