# 제어문 (Control Statement)

파이썬에서 많이쓰는 제어문

+ 조건문 `(if else)`
+ 반복문 `(for in)`
+ 조건+반복 `(while)`

# 조건문 `(if)`
조건에 따라 코드를 다르게 실행할때 사용한다.\
흐름도를 구성하고 하는 것이 쉽다.
+ `if` 조건에 따라 분기 _(예/아니오)_ 에 따라 명령을 수행.

## 1. 단일 조건에 따른 분기 `(if else)`
가장 기본적인 `if` 문의 구조
+ `:` 을 반드시 사용
+ 들여쓰기 `(Tab)` 반드시 사용.
```python
If (조건문) :
    (코드 블록)
```
예)
```python
x = 90
if (x >= 90) :
  print("축하합니다.")
  print("당신은 합격입니다.")
else :
    print("실격")
```
## 2. 다중 조건에 따른 분기 `(if elif else)`
2개 이상의 분기를 사용하고 싶을때.
+ `(elif)`는 앞 조건의 __아니오__ 일때 시행된는 분기문이다. _위치를 `if`와 동등하게 해야한다.


예)
```python
y = 85
if (y >= 90) :
    print("Exellent")
elif (80 <= y < 90) :
    print("Good")
else :
    print("need improvement")
```
+ 만약 __예__ 다음에 분기를 만들고 싶으면 `if`문을 그 안에 들여쓰기`(Tab)` 해서 사용해야한다.

예)
```python
z = 85
if (y >= 80) :
    if (y >= 90) :
        print ("Exellent")
    else:
        print ("Good")
else :
    print("need improvement")
```
_같은 결과값 기대_

## 3. 조건문 동작 안하기 `(pass)`
아무 (혹은 임시로) 작동을 하고 싶지 않을때, 만약 코드 블럭을 비우면 에러가 된다. 그럴때 `pass`를 적용한다. 

```python
A = 95
if (y >= 90) :
    # empty code block
elif (80 <= y < 90) :
    print("Good")
else :
    print("need improvement")
```
will produce error message
```
File "<ipython-input-14-6dd606f113c4>", line 4
    elif (80 <= A < 90) :
       ^
IndentationError: expected an indented block
```
`pass`를 적용한다.
```python
A = 95
if (y >= 90) :
    pass
elif (80 <= y < 90) :
    print("Good")
else :
    print("need improvement")
```

# 반복문
python에서는 `for` 와 `while` 을 이용하여 반복문을 시행한다.
## 1. `for`문의 구조
`for` `in` 그리고 `code block`을 이용하여 구성한다.
```python
 for <반복 변수> in <반복범위> : 
     <code block>
```
예) 1부터 10 ___전___ 까지 각 숫자에 20을 더하라.
```python
 for a in range(1,10,1) :
     b = a + 20
     print(b)
```
__참고__ `range`함수 : `range(start,stop,step)` from the `start` to (before) the `stop` by the given `steps`.

예) 1부터 10까지 숫자중 5보다 큰수을 프린트하라.
```python
N = range(1,11,1)
for n in N :
    if (n > 5) :
        print(n)
    else:
        pass
```

## 2. 중첩 `for`문
`for` 문도 중복 가능.
```python
for <반복 변수1> in <반복 범위1> :
    for <반복 변수2> in <반복 범위2> :
        <code block>
```
예) 2 by 2 모든 조합의 캐이스를 프린트한다.
```python
A = ['a1','a2']
B = ['b1','b2']

for a in A :
    for b in B :
        print(a,b)
```
예) 두개의 리스트의 변수를 매치시킨다.
```python
A = ['a1','a2']
B = ['b1','b2']

for c in range(len(A)) :
    print (A[c],B[c])

```

__참고__ `zip` 함수 : 
```python

```

## 3. `while` 문
+ `while`문은 `if`와 `for`의 조합이다.
+ `True`가 나오면 코드로 진행하고 그 답으로 ___다시___ 조건문으로 돌아와 질이 한다.
+ `Fales` 가 나오면 조건물에서 나온다.
