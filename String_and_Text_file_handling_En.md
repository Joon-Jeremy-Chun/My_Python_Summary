# String and Text file handling
+ It needs to read data or string types from text files. 
+ Vary of `method` options will help manipulation on the string.
+ Input text file data can save data type.
+ Can control string `split`, `delete`, and `connect`.

# String handling
## 1. 문자열 분리하기
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

