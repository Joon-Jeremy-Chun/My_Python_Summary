# 변수 (Variable)
반복되는 자료형이나 데이터를 변수로 지정하여 효율적으로 사용할 수 있다. _변수는 메모리(memory)에 저장됨으로 영구저장이 아니다._

## 변수 선언과 대입
1. 변수 선언을 가장 먼저 해야한다.

예) a변수는 정수형이다: `int a`

2. 그뒤 변수에 데이터를 대입(저장)해야한다

예) 변수a에 10을 대입(저장)한다. `a=10` 

_C 나 JAVA는 변수 선언을 반드시 해야하는데 python이나 R은 자동으로 인지한다._

## 기억해야할 변수 이름의 규칙들
+ 변수명은 `문자`, `숫자`, 그리고 `밑줄기호`(_)를 이용한다.
+ 숫자로 시작하는 변수를 만들수 없다.
+ 대소문자를 구분한다.
+ 공백을 포함할 수 없다. _왜냐하면 다음항이 명령어 일경우와 논리 충돌_
+ 밑줄 `_` 이외의 기호는 변수로 사용할 수 없다. _명령어중 논리 충돌_
+ 예약어(Reserved word)는 변수명으로 이용할 수 없다. _저장된 의미와 논리 충돌_

## 문자열(string) `str`
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
+ 긴문장과 두개 이사의 따옴표를 넣으려면 앞뒤로 3겹의 따옴표들 `"",''`을 넣는다.
```python
string5 = """"Seeing is believing" but I think 'We can see when we believe'"""
print (string5)
```

문자열 끼리면 더하기 곱하기도 가능
```python
a = 'I '
b = 'love '
c = 'you.'
print (a+b+c)
print (a+b*7+c)
```
