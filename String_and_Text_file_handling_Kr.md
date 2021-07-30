# 문자열과 텍스트 파일 데이터 다루기
+ 데이터가 포함된 텍스트 파일에서 문자 열을 읽어올 수 있어야 한다.
+ 다양한 문자열 `메서드(method)`가 제공됨으로 문자열을 처리하기 쉽다.
+ 읽어온 텍스트 파일을 다른 형태의 데이터로 변환해서 이용.
+ 문자열 분리, 제거, 연결 등을 할 수 있다.

# 문자열 다루기
## 1. 문자열 분리하기 `.split()`
+ `split()` 메서드를 이용한다.
+ 리스트로 반환한다.
```python
str.split([sep]) #sep를 기준으로 문자열을 분리한다.
```
+ 만약 `sep` 입력하지 않고 `str.split()`을 수행하면 문자열 사이의 모든 `공백`과 `개행문자(\n)`를 없애고 분리된 문자열을 항목으로 담은 리스트를 반환한다.

예)
```python
my_str = "I love you vary much"
my_str.split()
```
out : ['I', 'love', 'you', 'vary', 'much']
+ `콤마(,)`를 기준으로 문자열을 분리 하고 싶을때 `()`안에 `,`를 집어넣는다.

예)
```python
my_str = "I, love, you, vary, much"
my_str.split(',')
```
out : ['I', 'love', 'you', 'vary', 'much']
+ parameter `maxsplit`를 추가하면 앞에서부터 원하는 횟수 만큼만 문자열을 분리 할 수 있다.

예)
```python
my_str = "I love you vary much"
my_str.split( maxsplit = 2) #2개의 분기 점을 만들어라.
```
out : ['I', 'love', 'you vary much']

예) 국가 번호에 있는 번호에서 국내 번호로 전환
```python
phone_number = "+82-10-2345-6789"
my_num = phone_number.split("-", maxsplit = 1)

print (my_num)
print ("국내전화번호: 0{0}".format(my_num[1]))
```
out : ['+82', '10-2345-6789'] \
국내전화번호: 010-2345-6789

## 2.문자열 삭제하기 `.strip()`
+ `strip()`메서드는 문자열 ___앞과 뒤___ 에서 시작해서 지정한 문자(chars) 외의 다른 문자를 만날 때까지 지정한 문자를 모두 삭제한다.
+ 지정 문자 없이 시행한다면 앞뒤의 모든 `공간`과 `개행문자`를 삭제해서 반환 한다.

예) 빈공간을 지울때
```python
my_str = "   python\n     "
my_str.strip()
```
out : 'python'

예) 문자를 지울떄
```python
my_str = "ooopythonooooooo"
my_str.strip('o')
```
out : 'python'

예) 여러문자를 지울때
```python
my_str = "##!!aaapythonaaa!a!a#a"
my_str.strip('a#!') #순서는 상관 없다.
```
out : 'python'

+ 문자열의 `앞(왼쪽)`과 `뒤(오른쪽)` 한쪽만 할때 가각각 `.lstrip()` `.rstrip()`을 사용한다.

예) 왼쪽 오른쪽 문자만 지울때
```python
my_str = "ooopythonooooooo"
my_str.lstrip('o') # delete left-side
my_str.rstrip('o') # delete right-side
```
out : 'pythonooooooo'\
'ooopython'

+ 복합적 상황에서 사용 가능하다.

prctice1) 데이터에 문장이 각 문자 사이가 콤마(,)와 빈공간 그리고 개행문자로 되어 있다. 리스트에 문자열을 분리  저정하라.
```python
data_1 = "   I ,love , you \n , so,much \n\n"
#문자열 분리
data_list1 = data_1.split(',')

#리스트 안에 각 문자열 앞뒤 빈공간 밎 개행문자 제거
data_list_final = []
for words in data_list1 :
    x = words.strip()
    data_list_final.append(x)

print(data_list_final)
```
out : ['I', 'love', 'you', 'so', 'much']

## 3.문자열 연결하기
+ `더하기(+)`연산자도 문자를 연결 할 수 있다. 또한`.join()` 메서드를 이용 할 수 있다.

```python
data_list = ['I', 'love', 'you', 'so', 'much']

a = "" #a라는 변수에 빈공간(빈문자)로 지정 하여 문자 사이를 붙인다.
a.join(data_list)
```
out : 'Iloveyousomuch'\
띄어 쓰려면 
```python
a = " " # 이렇게  정의 해야 한다.
```
+ 변수에 정의된 사잇값을 다른 문자로 대처 할 수 있다.
```python
data_list = ['I', 'love', 'you', 'so', 'much']

"~^^~".join(data_list) #변수 지정없이 바로 할 수 있다.
```
out : 'I~^^~love~^^~you~^^~so~^^~much'

## 4. 문자열 찾기
+ `.find()` 메서드를 사용하여 문자열의 위치를 찾을 수 있다. _중복일 경우 앞의 처음만 값을 반환 한다._
+ 못 찾으면 `-1`을 반환한다.
```python
str_ex = "Joon Jeremy Chun"

print ("문자열의 위치:", str_ex.find("J"))
print ("문자열의 위치:", str_ex.find("Jeremy"))
print ("문자열의 위치:", str_ex.find("joon"))
print ("문자열의 위치:", str_ex.find("Ch"))
```
out1 : 문자열의 위치: 0 #중복일경우 처음만 찾는다.\
out2 : 문자열의 위치: 5 #단어일경우 처음위치를 대표하여 출력한다.\
out3 : 문자열의 위치: -1\
out4 : 문자열의 위치: 12

+ `.find()` 메서드에 `시작`과 `끝` 위치를 지정해 그 안에서만 찾을 수 잇다.
```python
str_ex = "Joon Jeremy Chun"

print ("문자열의 위치:", str_ex.find("J",0,30))
print ("문자열의 위치:", str_ex.find("J",10,30))
```
out1 : 문자열의 위치: 0\
out2 : 문자열의 위치: -1
## 5. 문자열 개수 찾기
+ `.count()`메서드를 이용하여 데이터에 인자 문자열과 일치하는 문자열의 횟수를 가져온다.
+ 대소문자는 구분된다.
+ `.find()`메서드와 같이 검색의 `시작`과 `끝` 위치를 지정 할 수 있다.

예)
```python
str_ex = "Joon Jeremy Chun"

print ("문자열 반복 횟수:", str_ex.count("J"))
print ("문자열 반복 횟수:", str_ex.count("J",5,30))
```
out1 : 문자열 반복 횟수: 2\
out2 : 문자열 반복 횟수: 1
## 6. `.startswith()`와`.endswith()` 
+ 함수 각각 지정된 문자열이 있는지 `True`와 `False`형식으로 반환한다.
+ 범위를 지정 할 수 있다.

구조와 예
```python
str_ex = "Joon Jeremy Chun"

print (str_ex.startswith("Joon", 0, 30))
print (str_ex.startswith("Chun", 0, 30))
print (str_ex.startswith("Chun", 12, 30)) #12문자열 부터

print (str_ex.endswith("Joon", 0, 30))
print (str_ex.endswith("Chun", 0, 30))
print (str_ex.endswith("Chun", 0, 10))
```
out1 : Ture\
out2 : False\
out3 : Ture\
out4 : False\
out5 : Ture\
out6 : False
## 7. 문자열 바꾸기
+ `.replace()` 메서드를 이용한다.
+ 두번째 인수로 `숫자`를 입력하면 총 `몃회` 바꿀지 설정 할 수 있다.
+ "" 빈공간으로 지정하여 `삭제` 할 수 있다.

예)
```python
str_x = "joon jeremy chun"

print(str_x.replace("j", "J"))
print(str_x.replace("j", "J",1))
```
out1 : Joon Jeremy chun\
out2 : Joon jeremy chun
+ `replace()`메서드를 이용하여 띄여쓰기나 개행문자등 제거 할 수 있다.

## 8. 그외 중요 method

테이블

# 텍스트 파일의 데이터를 읽고 처리하기
