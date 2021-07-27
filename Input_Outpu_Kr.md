# 입력과 출력 `Input&Output`
`input()`과 `print()`함수를 사용한다.

## 1. `print()`함수
출력 형식을 지정하지 않는 기본 출력 방법과 다양한 형식으로 출력할 수 있는 형식들이 존재한다.

### 기본 출력
+ `문자열`과 `숫자`를 출력한다.
+ `콤마(,)`로 구분하고 연속해서 입력한다.
```python
print ("I", "love", "you", 2)
```
+ `sep`을 이용하여 문자 사이에 문자열이 들어간다.
```python
print ("I", "love", "you", sep = "~~")
```
+ 빈칸 없이 문자열을 연결하려면 `(+)`
+ 문자열을 반복하려면 `(*n)`
```python
print ("I","l"+"o"+"v"+"e","you")
print ("I","l"+"o"*7+"v"+"e","you")
```
+ 문자열을 여러 줄로 출력하려면 `개행문자(\n)`을 사용한다.
+ 한칸 더 띄울려면 `\n\n`
```python
print( "I love you. \nDo you love me?")
print( "I love you. \n\nDo you love me?")
```
+ `end=` 인자를 추가하여 줄바꿈 없이 프린트 된다.
```python
print ("I love you")
print ("Do you love me?")
 ```
 
```python
print ("I love you", end = "")
print ("Do you love me?")
```
_이유: `print()`함수 안에 라인 끝에 자동으로 `\n`이 들어가는데 `end = ` 인자는 끝의 보이지 않는 `\n`을 대처하고 `""`빈상태가 되어 다음 열 값이 붙어서 프린트 된다._

## 2. `print()`함수 지정 출력
나머지 연산자`(%)`를 이용하여 형식 밎 위치를 지정할 수 있다.
```python
print("%tpye" % data)
```
+ `따옴표("")`와 `%data` 사이에 `콤마(,)`가 없고 `공백`이 있다는 점.
+ data가 문자열이라면 `%s`, 정수이면 `%d(or%i)`, 실수이면 `%f(or %F)` 로 표시한다.
+ 실수의 경우 소숫점 6자리까지 나타낸다.

프린트 함수가 두 개 이상이라면 다음과 같다.
```python
print (("%type %type" %(data1,data2))
```
예) 1개 데이터 일때
```python
name = "Joon Jeremy Chun"
print ( "%s is my name." %name)
```
예) 여러 위치 여러 데이터 일때
```python
root_2 = 2**(1/2)
print ("Inteter value of root 2: %d, Its 6 decimal value: %f" %(root_2,root_2))
```
### 출력 위치 설정
`string.format()`을 사용한다.
예)
```python
letter_0 = "I"
letter_1 = "love"
letter_2 = "you"

print ("I want to say: {0} {1} {2}".format(letter_0,letter_1,letter_2))
print ("I want to say: {2} {1} {0}".format(letter_0,letter_1,letter_2))
print ("I want to say: {} {} {}".format(letter_0,letter_1,letter_2))

say = "I want to say: {0} {1} {2}"
print (say.format(letter_0,letter_1,letter_2))

```
+ `{}`로 `.format(data)`의 순서를 지정한다. 
+ 비여있다면 순서대로 출력한다.

### 숫자의 출력 형식 지정
다음과 같은 출력 방식이 존재한다.

## 3. 키보드 입력
