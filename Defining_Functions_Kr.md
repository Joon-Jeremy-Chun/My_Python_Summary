# 함수 (Function)
수학의 함수와 같은 구조가 있다. `input value` 없이 쓸수 있고 `output value`존재 하지 않을 수 도있다. _수학의 함수와 다른 점은 `input value`없이 `output value`를 가지고 올 수있다._
+ 프로그램에서는 `input value`를 `parameter`라고 한다.
+ 함수의 정의 부분과 함수의 호출 부분의 구조를 같는다.
```python
def 함수명([인자1,...]) # input
    <code block>
    [return <반환 값>] # output
```
+ 인자, 반환값 없는 함수의 예
```python
def my_func() :
    print ("example of function")
    print ("without parameter")

my_fun() # 인자없이 함수를 사용한다.
         # 결과 값 없이 print만 된다.
```
+ 인자 값은 있으나 반환 값이 없는 함수의 예
```python
def my_friend(friendName) :
    print (friendName, "나의 친구 입니다.")

my_friend("Joon Jeremy Chun") 
```
+ 인자 값도 있고 반환 값도 있는 함수의 예
```python
def add_3num(x,y,z) :
    a = x+y+z
    return a

add_3num(100,10,1) # 3개의 숫자의 합 결과를 가져온다.
```
 ex 1) 학교 정보표 함수 만들기.
```python
def students_info(name,phoneNum) :
    print ("-------------")
    print ("학생 이름: %s" %name)
    print ("전화 번호: {0}".format(phoneNum))
    print ("-------------")

students_info("천준", "010")
```
