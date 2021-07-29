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
### 데이터 형태를 변환해야 하는 경우 파이썬 내장 함수를 이용한다.
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
### 리스트, 튜플, 세트형으로 변환
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
