# 입력과 출력 `Input&Output`
`input()`과 `print()`함수를 사용한다.

## 1. `print()`함수
출력 형식을 지정하지 않는 기본 출력 방법과 다양한 형식으로 출력할 수 있는 형식들이 존재한다.

### 기본 출력
+ `문자열`과 `숫자`를 출력한다.
+ `콤마(,)`로 구분하고 연속해서 입력한다. _공백이 생긴다._
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
_이유: `print()`함수 안에 라인 끝에 자동으로 `\n`이 들어가는데 `end = ` 인자는 끝에 보이지 않는 `\n`을 대처하고 그안의 연산이 `""`빈상태가 되어 다음 열 값이 붙어서 프린트 된다._

## 2. `print()`함수 지정 출력
나머지 연산자`(%)`를 이용하여 형식 밎 위치를 지정할 수 있다.
```python
print("%tpye" % data)
```
+ `따옴표("")`와 `%data` 사이에 `콤마(,)`가 없고 `공백`이 있다.
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

say = "I want to say: {0} {1} {2}" #변수로 지정 가능
print (say.format(letter_0,letter_1,letter_2))

```
+ `{}`로 `.format(data)`의 순서를 지정한다. 
+ 비여있다면 순서대로 출력한다.

### 출력 형식 `{ n : 형식 }`
예) 소수점 2자리 10자리까지만 나타내어라.
```python
A = 2**(1/2)

print ("소숫점 2자리까지: {0 : 2d} n\ 소숫점 10자리까지: {1 :10d}".format(A,A))
```

### 숫자의 출력 형식 지정
다음과 같은 출력 방식이 존재한다.

## 3. 키보드 입력
키보드로 데이터를 입력할 때는 `input()` 함수를 사용한다.\
예) 간단한 입력 출력
```python
yourName = input("what your name?")
print ("Hi %s good to know you." %yourName)
```
예) 직사각형 넓이 계산기
```python
length = input ("length of square?")
area = float (length)**2
print ("The area of square: %f" %area)
```
## 4. 파일 읽고 쓰기
데이터는 하드에 저장 되있고 작업을 할때는 메모리위로 올려 작업하고 다시 하드로 저장 해야한다. 그래서 파일을 읽고 쓸때는 
1. opne 
2. read
3. write
4. close

의 순서를 가진다.
### 파일 열기
+ 파일에 `변수`를 지정해주고 `open` 함수로 파일명과 모드를 입력한다.
```python
f = open('file_name','mode')
f.read()
f.close()
```
### 모드의 종류
|mode|의미|
|----|----|
|r|일기 모드로 파일 열기. 모드를 지정하지 않으면 기본적으로 읽기모드로 지정된다.|
|w|쓰기 모드로 파일 열기. 같은 이름의 파일이 있으면 기존내용 모두 삭제된|
|x|쓰기 모드로 파일 열기. 같은 이름의 파일이 있을 경우 오류가 발생함.|
|a|추가 모드로 파일 열기.|
|b|바이너리 파일 모드로 파일 열기. 실제 컴퓨터용어인 바이너리로(숫자) 파일을 연다.|
|t|텍스트 파일 모드로 파일 열기. 지정하지 않으면 기본적으로 텍스트 모드로 지정됨.|

`mode`는 혼합해서 사용가능. 예) `'wb'`혹은`'bw'`

### 파일 쓰기
+ 파일 쓰기를 위한 코드 구조
```python
f = opne('file_name', 'w')
f.write(str)
f.close()
```

