# 데이터 분석을 위한 패키지(packages)
외부 패키지는 인스톨 해서 사용한다.
`pip install numpy`


#  NumPy package
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
+ `Numpy` 배열은 문자열도 원소로 가질수 있다.
```python
ex1 = np.array(['1.5','0.6','3'])
ex1.dtype
```
out : dtype('<U3') \
\# 데이터 형식이 유니코드(U)이며 문자의 수는 최대(<>)세(3)개
<br><br>
+ `.astype()`을 통하여 `int` `float` `str` 형태로 변환할 수 있다.
```python
ex1 = np.array(['1.5','0.6','3'])
ex2 = ex1.astype(float)
ex2
ex2.dtpye
```
out1 : array([1.5, 0.6, 3. ])\
out2 : dtype('float64')
+ 실수에서 정수로 바뀔때는 소수점은 버린다.
#
## 5. 임의의(random) 수 생성
+ `random` module을 통하여 난수를 생성할 수 있다.
+ `NumPy`의 `rand()`과 `randint()`함수를 이용 할 수 있다.

+ 임의 하나의 숫자를 불러올때
```python
np.random.rand()
```
out : #범위 지정없이[0,1)에서 임의의 실수.
<br><br>
+ 임의의 원소를 갖는 행렬 (m*n) 
```python
np.random.rand(3,4) #행렬을 뜻한다.
```
out : #임의의 값 [0,1)을 원소로 같은 3*4행렬\
array([[0.40804391, 0.40445968, 0.42831879, 0.54258503],\
       [0.78607999, 0.77882787, 0.65623124, 0.83637594],\
       [0.68608357, 0.09765773, 0.95964838, 0.33702147]])
<br><br>
+ k개의 임의의 원소를 갖는 행렬 (m*n)
```python
np.random.rand(2,3,3)
```
out : #array 안에 2개의 3*3행렬
<br><br>
+ 지정 범위에 해당하는 `정수`로 난수,난수행렬 생성
```python
np.random.randint(10, size = (4,3))
np.random.randint(1,30)
```
out1 : #  임의의 원소 9를 최대로하는 4*3행렬\
out2 : # [1,30)범위의 임의의 수


#
## 6. 배열의 연산
배열의 연산을 위해선 형태`(shape)`이 같아야 한다.

#
## 7. 통계를 위한 연산
#
## 8. 행렬 연산

#
