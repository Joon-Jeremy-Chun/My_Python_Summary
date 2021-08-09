# 사칙연산(Arithmetic operation)
+ `+,-,*,/` 가 존재한다.
```python
print (1+1)
print (1-2)
print (2*-2)
print (10/5)
```

+ 몫 과 나머지

```python
print (10 // 3)
print (10 % 3)
```
out1 : 3\
out2 : 1
+ 제곱
```
print (2**10)
print (2**(1/2))
```
out1 : 1024\
out2 : 1.4142135623730951
+ 변수를 지정하여 사칙연산이 가능하다.
```python
a = 2
b = 3
c = 1
x = (-b+(b**2-4*a*c)**(1/2))/(2*a),(-b-(b**2-4*a*c)**(1/2))/(2*a)
print(x)
```
out : (-0.5, -1.0)