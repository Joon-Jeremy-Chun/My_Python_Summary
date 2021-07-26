# 변수 (Variable)
반복되는 자료형이나 데이터를 변수로 지정하여 효율적으로 사용할 수 있다. \
_변수는 메모리(memory)에 저장됨으로 영구저장이 아니다._

## 1. 변수 선언과 대입
1. 변수 선언을 가장 먼저 해야한다.

예) a변수는 정수형이다.
```python
 int a
```

2. 그뒤 변수에 데이터를 대입(저장)해야한다.

예) 변수a에 10을 대입(저장)한다. 
```python
a = 10
```

_C 나 JAVA는 변수 선언을 반드시 해야하는데 python이나 R은 자동으로 인지한다._

## 2. 기억해야할 변수 이름의 규칙들
 + 변수명은 `문자`, `숫자`, 그리고 `밑줄기호`(_)를 이용한다.
 + 숫자로 시작하는 변수를 만들수 없다.
 + 대소문자를 구분한다.
 + 공백을 포함할 수 없다. _왜냐하면 다음항이 명령어 일경우와 논리 충돌_
 + `밑줄` `_` 이외의 기호는 변수로 사용할 수 없다. _명령어중 논리 충돌_
 + `예약어(Reserved word)`는 변수명으로 이용할 수 없다. _저장된 의미와 논리 충돌_

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
+ ___리스트와 매우 큰 차이점은 튜플은 변경이 불가능하다.___
+ 그래서 특정 메스드는 불가능하다.
+ 장점은 테이터가 변한지 않으니 용량가변성이 없어 메모리나 용량을 최소화할 수 있다. 즉, 회전속도에 매우 유리하다.
+ 특정 함수를 사용하여 List <-> Tuple 가능하다.

# 딕셔너리(Dictionary)
+ 기존`(List,Tuple)`과는 다른새로운 타입의 테이터 모음이다.
+ 사전과 유사한 구성; 키`(key)`와 값`(value)`이 한 쌍으로 구성된다.
+ 인텍스`(index)`대신 키`(key)` 를 이용하여 데이터`(value)`를 다룬다.
+ 그러므로 `print` 했을때 `order` 순서가 없다.
+ `{}`를 이용한다. 예) `dict_name = {key1:value, key2:value}`
+ 테이터가 순서보다는 두 정보의 매치가 중요할때 사용한다.

___*만약 `key`가 중복된다면, 자동으로 마지막 데이터를 가져온다.___ 혹은 ___마지막에 타입된 값___

## 1. 딕셔너리 만들기
키`(key)`는 숫자와 문자열만 될수 있고 그 값`(value)`는 어떤 데이터 형태도 가능하다.
```python
dict_data1 = {1:10, 2:20, 3:30, 4: 40}
dict_data2 = {"list_data1":['a','b','c'], "list_data2":[3,2,1]}
print (dict_data2)
print (dict_data2["list_data2"])
```

## 2. 딕셔너리 다루기
+ 데이터 삭제하려면 `del ...[key]`을 사용한다.
```python
dict_data1 = {1:10, 2:20, 3:30, 4: 40}
del dict_data1 [1]
print (dict_data1)
```
+ 테이터를 추가하거나 `value` 값을 변경하려면 dict_data[ `key` ] = `value`를 사용하다.
```python
dict_data2 = {1:1.0, 2:20, 3:30, 4: 40}
dict_data2[5]=50
dict_data2[1]=10
print (dict_data1)
```
## 3. 딕셔너리 메서드`(method)` 활용하기
다음과 같은 딕셔너리 메서드가 존재한다.

# 세트(Sets)

+ 세트를 만들때는 중괄호`{}`를 사용한다.
+ 중복은 한번만 출력된다.
```python
set1 = {1,2,3}
set1a = {1,2,3,3,}
print(set1)
print(set1a)
```

## 1. 세트의 구현
+ 교집합 `(intersection)`
+ 합집합 `(union)`
+ 차집합 `(difference)`

## 2. 세트 메서드`(method)`, `연산자` 활용하기
| 메서드  | 설명     | method   | 연산자 |
|-------  | ------  | -------  | ----- |
| 교집합  | A  and  B|     A.Intersection(B)| A & B|
| 합집합  | A  or  B|    A.union(B)| A \\| B |
| 차집합  | A not  B|    A.difference(B)| A - B  |

```python
setA = {1,2,3,4,5}
setB = {4,5,6,7,8}
print (setA&setB)
print (setA.intersection(setB))
```
# 데이터 타입 변형
데이터 타입을 변형할 수 있다.
+ `list()`
+ `tuple()`
+ `set()`

```python
A = [1,2,3,4,5]
B = tuple (A)
print (B)
C = set (B)
print (C)
D = list (A)
print (D)
```

