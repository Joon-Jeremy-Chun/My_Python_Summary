# 데이터 분석을 위한 패키지(packages)
외부 패키지는 인스톨 해서 사용한다.
`pip install numpy`


# 1. NumPy package
+ 과학 연산할때 유용한 패키지다. _데이터 연산이 빠르다._
+ 데이터를 `arrary`(배열) 형태  로 처리한다.
#

## 1. 배열 생성하기
```python
import numpy as np
```
별명으로 numpy -> np 로 지정
<br><br>
+ `리스트(list)`로 부터 1차원 배열 생성
```python
data1 = [0,1,2,3,4,5]
a1 = np.array(data1)
a1
```
out : array([0, 1, 2, 3, 4, 5])
<br><br>
+ 정수와 실수가 혼합되어 있을때
```python
data2 = [0,1,2,3,4,5.5]
a2 = np.array(data2)
```
데이터 타입이 실수형으로 나오는 걸 알 수 있다. _숫자는 비트를 뜻함_
```python
a1.dtype
a2.dtype
```
out1 : dtype('int64')\
out2 : dtype('float64')
<br><br>
+ 1차원 뿐만 아니라 2차원(행렬)형식도 가능(혹 그 이상)
```python
np.array([[0,1,2],[3,4,5],[6,7,8]]) #[]를 잊지말고 추가
```
#
## 2. 범위 지정 배열 생성
+ `.arange()`를 이용한다.

```python
np.arange(start,stop,step)
np.arange(start,stop)
np.arange(stop)
```
형식이다.
<br><br>
+ `.linspace(start,stop,num)`를 이용하여 시작과 끝의 수 사이를 숫자`num`에 맞게 균등하게 나눈다.
+`num`이 지정되지 않으면 50으로 간주한다.
```python
np.linspace(0,1,5) # 5개의 항을 만든다.
```
out : array([0.  , 0.25, 0.5 , 0.75, 1.  ])

#
## 3. 행렬 생성
+ `.reshape(m,n)`을 사용한다.
예) 0부터 11까지 4by3행렬을 만들어라
```python
np.arange(12).reshape(4,3)
```
out : #행렬\
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 9, 10, 11]])
<br><br>
+  `.shape`을 수행하여 행렬 크기를 구할 수 있다.
```python
b1 = np.arange(25).reshape(5,5)
b1.shape
```
out : (5, 5)
<br><br>
+ 1차원 함수는 `(n,)`로 표시된다.
```python
b1 = np.arange(25)
b1.shape
```
out : (25,)
<br><br>
+ 원소가 `0` 혹은 `1`인 1차원 2차원 행렬만들기
+ `zeros()`와 `ones()`를 이용
예)
```python
np.zeros((3,4))
np.ones((3,4))
```
out :  각각
<br><br>
+ `단위행렬 (Identity matrix)` 생성
+ `.eye(n)`을 사용
```python
np.eye(3)
```
out : 
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
#
## 4. 데이터 타입 변환
#
## 5. 임의의(random) 수 생성
#
## 6. 배열의 연산
#

#
# 2. pandas package
+ `series`(수열) 형태과 `dataframe` (데이터 테이블) 형태로 데이터를 연산 한다. 