# 통계 대표값
평균, 중앙값, 최빈값이 집단의 대표 값이 될 수 있다.
1. mean
2. median
3. mode
+ 가장먼저 데이터을 열어본다. 그 뒤
```python
import numpy as np
import pandas as pd

pd.set_option('precision',3) #출력을 소숫점 3자리 이하.

```
주어진 파일 scores_em.csv
+ 데이터의 구성을 python에서 열어보기
```python
df = pd.read_csv('scores_em.csv', index_col = 'student number') # index for studen number 

df.head() # read first 5 rows
```
#
## 1. 평균 (mean)
일반적으로 평균이 대표 값이 된다. 
+ 처음 10개의 영어의 값을 대표값으로 가정하고 불러오기
```python
scores10 = np.array(df['english'])[0:10]
print (scores10)
```
out : [42 69 56 41 57 48 65 49 65 58]
<br><br>
+ 알파벳 순으로 인덱스를 부여하기
```python
scores10_df = pd.DataFrame({'socre':scores10}, index = pd.Index(['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J'], name = 'student'))

scores10_df
```
out : # (10,2)의 데이터 프레임
<br><br>
+ 평균값 구하기
```python
sum(scores10) / len(scores10)
```
```python
np.mean(scores10)
```
out : 55
```python
scores10_df.mean()
```
out : socre    55.0\
dtype: float64


#
## 2. 중앙값 (median)
일반적으로 평균이 대표 값이 되나, `예외값`이(outlire)이 평균에 지대한 영향을 미칠 경우가 있다. 이때 중앙값을 이용한다.
+ 데이터를 정렬한다.
+ 홀수일때 (n+1)/2 번째 데이터 값을 가져온다.
+ 짝수일때 두 중앙 값의 평균을 가져온다.
<br>

```python
#정렬
sorted_scores10 = np.sort(scores10)
print(sorted_scores10)

#공식 적용
n = len(sorted_scores10)
if n % 2 == 0 :
    m0 = sorted_scores10[n//2 -1] #[]안에는 정수형만 들어간다 그래서 정수를 구하기 위해//사용 
    m1 = sorted_scores10[n//2]
    median = (m0+m1) / 2
else :
    median = sorted_scores10[n // 2 -1]
print (median)
```
out : [41 42 48 49 56 57 58 65 65 69]\
56.5
<br>
+ `.median()` 메서드 사용하기
```python
np.median(scores10)
#혹은
scores10.median()
```
out :\
socre    56.5\
dtype: float64
#
## 3. 최빈값 (mode)

#
## 4. 절사평균
+ outlire 때문에 평균에 영향을 미치는걸 보안 하기위해서 사용한다.

+ 10% 절사평균은 자료 양쪽의 10% 씩을 버리고 나머지 데이터 80%만 가지고 평균을 낸다.
