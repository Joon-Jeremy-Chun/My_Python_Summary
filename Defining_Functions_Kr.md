# 함수 (Function)
수학의 함수와 같은 구조가 있다. `input value` 없이 쓸수 있고 `output value`존재 하지 않을 수 도있다. _수학의 함수와 다른 점은 `input value`없이 `output value`를 가지고 올 수있다._
+ 프로그램에서는 `input value`를 `parameter`라고 한다.
+ 함수의 정의 부분과 함수의 호출 부분의 구조를 같는다.
```python
def 함수명([인자1,...]) # input
    <code block>
    [return <반환 값>] # output
```
# 인자(paramter)와 반환(return value)
## 1. 인자, 반환 `return`값 없는 함수의
예)
```python
def my_func() :
    print ("example of function")
    print ("without parameter")

my_fun() # 인자없이 함수를 사용한다.
         # 결과 값 없이 print만 된다.
```
## 2. 인자 값은 있으나 반환 `return` 값이 없는 함수
예)
```python
def my_friend(friendName) :
    print (friendName, "나의 친구 입니다.")

my_friend("Joon Jeremy Chun") 
```
 ex 1) 학교 정보표 함수 만들기.
```python
def students_info(name,phoneNum,ID) :
    print ("-------------------------")
    print ("학생 이름: %s" %name) #여러 방식
    print ("전화 번호: {0}".format(phoneNum))
    print ("학생 ID: ", ID)
    print ("-------------------------")

students_info("천준", "010-0000-0000","2021") #정보표에 정보가 기록되어 출력된다.
```
ex 2) 리스트를 인자로 갖은 함수. (학교 정보표 함수)
```python
def students_info_list(students_info) :
    print ("-------------------------")
    print ("학생 이름: ", students_info [0]) 
    print ("전화 번호: ", students_info [1])
    print ("학생 ID: ", students_info [2])
    print ("-------------------------")

students_info = ["천준","010-0000-0000","2021"] #데이터를 리스트 형식으로 지정한다.
students_info_list (students_info) # 함수에 인자를 삽입한다. 그리고 함수를 호출한다.
```
## 3. 인자 값도 있고 반환 값도`return` 있는 함수

예) 3개의 숫자의 합.
```python
def add_3num(x,y,z) :
    a = x+y+z
    return a

n=add_3num(100,10,1) # 3개의 숫자의 합 결과를 가져온다.
type(n) # int 즉, 반환값이 있는 함수

def add_3num(x,y,z) :
    a = x+y+z
    print (a)

n=add_3num(100,10,1) 
type(n) # None type 즉, 반환값이 단순 프린트한 결과이다.

```
# 변수의 유효 범위
+ 전역 영역`(global scope)`, 지역 영역`(local scope)`, 내장영역`(built-in scope)`이 존재한다.
+ `스코핑 룰(Scoping rule)` 혹은 `LGB 룰(Local/global/Built-in rule)`에따라 함수 호출할 때 변수를 검색한다.
+ 동일한 변수명을 사용할때는 `LGB룰`에따라 변수가 선택된다.

예) 원리를 파악한다.
```python
a = 10 #전역변수
def func1() :
    a = 1
    print ("[func1]지역변수 a = ",a)
    
def func2() :
    a = 2
    print ("[func2]지역변수 a = ",a)

def func3() :
    print ("[func3]전역변수 a = ",a)

def func4() :
    global a #함수내로 전역변수를 변경하기 위해 선언
    a = a - 1 #전역변수에서 1 작은수로 변경
    print("[func4]전역변수 a = ", a) 

# 그뒤 다음 값을 출력해본다.

func1()
func2()
print("현재 전역변수 a =",a)
#
func4()
print("현재 전역변수 a =",a)
#
func3()
#
func4()
func3()
```

# 람다(lambda) 함수
한줄표현하는 `lambda`함수

예) 제곱함수를 만들고 9의 제곱을 구하라
```python
def my_sq(x) :
    a = x**2
    return a

my_sq(9)
```
예) 위의 예제에 람다함수로 표현
```python
(lambda x : x**2)(9)
```
```python
my_sq = lambda x : x**2
my_sq(9)
```

# 유용한 내장 함수
내장함수를 사용하면 code block도 짧아지고 속도도 빨라진다.
## 1. 형 변환

+ 정수형 변환 `int()`
+ 실수형 변환 `float()`
+ 문자형 변환 `str()`

예) 실수형을 정수형으로
```python
[int(0.123),int(1.7),int(-5.4),int(-5.6)]
```
소수점은 버리는 방식으로 변환된다.

예) 정수형을 실수형으로
```python
[float(0),float(100),float(-100)]
```

예) 정수나 실수형을 문자형으로
```python
[str(0.0),str(0),str(-10),str(-10.0)]
```
## 2. 리스트, 튜플, 세트형으로 변환
`list()`,`tuple()`, 그리고 `set()`을 사용한다.
예) 변환 예
```python
list_data = ['abc', 1, 2, 'def']
tuple_data = ('abc', 1, 2, 'def')
set_data = {'abc', 1, 2, 'def'}

# 리스트로 전환 후 프린트
print (list(tuple_data),list(set_data))

# 튜플로 전환 후 프린트
print (tuple(list_data),tuple(set_data))

# 셋으로 전환 후 프린트
print (set(list_data),set(tuple_data))
```
## 3.`bool()` 함수의 변환 
+ `bool()`함수는 `True` 혹은 `False`로 출력하는 함수다.
+ 기본적으로 `숫자열`이면 0을 제외한 모든 숫자를 인수로 하면 `True`가 나온다.
```python
bool (0) #0은 예외로 False 가 출력된다.
bool (1)
bool (-1)
bool (1.0)
```

+ `문자열` 일때 `문자열`이나 `공백`(스페이스)는 `True`이다. 
+ 문자열 `비여있는` 경우와 `None`의 경우 `False`를 출력 한다.
```python
bool('love')
bool('  ') #공백이 '존재'한다.
bool('') #비여있다.
bool(None)
```

+ `list`, `tuple`, `sat`도 `bool()` 함수를 사용 가능하다.
+ _항목에 데이터가 있는지 없는지 검사할때 매우 유용하다._

예) 리스트에서 `bool()` 사용.

```python
my_file = []
bool(my_file) # Fales

my_file = ['I','love','you']
bool(my_file) # True
```
예) `bool()`을 사용하여 인자를 넣을 때 인자를 반환하고 비여있을 때 (0포함) '비여있습니다.'을 반환하는 함수를 만들어라. 
```python
def name_f(name) :
    if bool (name) :
        print (name)
    else :
        print ("비여 있습니다.")

name_f("천준") # 천준이 반환 된다.

name_f("") # 문자가 아닙니다. 가 반환.

```
예) 문자와 그외를 구분하는 함수
```python
def name_g(name) :
    if type(name) == str :
        print (name)
    else :
        print ("문자가 아닙니다.")

name_g("천준") # 천준이 반환 된다.

name_g("1") # 문자가 아닙니다. 가 반환.

```
## 4.최솟값과 최대값을 구하는 함수 `min()`& `max()`
+ 숫자뿐만 아니라 문자 더나아가 특수문자 까지도 순서를 정할 수있다.
+ 숫자 < 대문자 < 소문자 순서이다.
+ 첫문자가 같을경우 다음 문자를 비교한다.

## 5.절대값`abs()`과 전체 합`sum()`을 구하는 함수
```python
abs(-1)
```

```python
data_x = [-1,0,1,2,3]

sum(data_x)
```

## 6.항목의 개수를 구하는 함수 `len()`
+ 문자열일경우 문자열의 개수를 구함. _공간도 하나의 문자로 본다._

```python
len("123 456")
#의 해는 7
len("천 준")
#의 해는 3
```
+ `list`, `tuple`, `set`, 그리고 `dectionary`의 항목의 개수를 구할  수 있다.
```python
len({1:"I",2:"love",3:"you"})
```

예) `sum()`과 `len()`를 사용하지 않고 평균 구하기
```python
data_score = [73,67,89,100]

sum_scores = 0
num = 0
for single_score in data_score :
    sum_scores = sum_scores + single_score
    num = num + 1
avg = sum_scores/num
print ("총점 : {0} 평균 : {1}".format(sum_scores, avg ))

```

예) `sum()`과 `len()`를 사용하여 평균 구하기
```python
data_score = [73,67,89,100]

print ("총점 :", sum(data_score), "평균 :", sum(data_score)/len(data_score))
```
예) for fun! 만약 문자를 더한다고 한다면?
```python
data_score = ["love ","you ","so ","much"]

sum_scores = "I "
for single_score in data_score :
    sum_scores = sum_scores + single_score
    

print ("I want to say : {0}".format(sum_scores) )
```