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

for c in range(len(A)) : #len(A)대신 len(B)도 가능
    print (A[c],B[c])

```

__참고__ `zip` 함수 : 위와같이 리스트의 변수를 매치시킨다.
```python
A = ['a1','a2']
B = ['b1','b2']
for A, B in zip(A,B) :
    print (A,B)
```
`zip`함수의 좋은점은 len(A)과 len(B) 작은것을 기준으로 매치되고 나머지는 자동으로 프린트되지 않는다.

## 3. `while` 문
+ `while`문은 `if`와 `for`의 조합이다.
+ `True`가 나오면 코드로 진행하고 그 답으로 ___다시___ 조건문으로 돌아와 질이 한다.
+ `Fales` 가 나오면 조건문에서 나온다.

## 4. `while` 문의 구조
다음과 같은 구조로 만든다.
```python
while <조건문> :
    <code block>
```

## 5. `break` and `continue`
어떤 특정 조건을 만족하는 경우 멈추고 `<code block>` 에서 나와야 하는 경우 `break`를 사용한다. 혹은 다음 반복문을 시행해야할 경우 `continue`를 사용한다.

예) 0보다크고 2보다 작은 수를 프린트하라.
```python
k = 0 # 초기화
while True :
    k = k + 1 # 새로운 k는 1씩 증가한다 
    if (k > 2) : # k가 2보다 크면 
        break # 멈춰라
    else : # (if 가)그렇지 않을 경우 
        print (k) # k의 값을 출력해라
```
예) 2를 제외하고 0부터 4까지 프린트하라. `for`를 사용해서.
```python
for k in range(0,5,1) :
    if (k == 2) :
        continue
    else:
        print (k)
```

예) 2를 제외하고 0부터 4까지 프린트하라. `while`,`continue`,그리고 `brack`를 사용해서.
```python
k = -1 # k = k+1을 사용해서 시작을 -1로 설정
while True :
    k = k +1
    if (k == 2) :
        continue
    elif (k < 5) :
        print (k)
    else :
        break
```
## 6. 리스트 컴프리헨션 `(List) Comprehension`
리스트, 세트, 딕셔너리 안에서 실행할 수 있는 한줄 `for`문.\
기본구조는 다음과 같다.
```python
[<반복 실행문> for <반복 변수> in <반복 범위>]
```

예 6.1.1) 리스트의 항목의 수를 각각 루트를 씌워라.

```python
numbers = [1,2,3,4,5]
root = []
for i in numbers :
    root.append(i**(1/2))
print (root)
```
예 6.1.2) 위의 문제에 `comprehension`을 사용하라.

```python
numbers = [1,2,3,4,5]
root = [i**(1/2) for i in numbers]
print (root)
```

`if`문과 함께 사용 가능하다.

예) 위의 문제에서 `comprehension`과 `if`를 사용하라.
```python
N = range(-100,100,1)
root = [i**(1/2) for i in N if 0 < i < 6]
print(root)
```