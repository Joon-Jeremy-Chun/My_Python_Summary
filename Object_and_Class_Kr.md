# 객체(Object)와 클래스(Class)
+ 클래스는 반복되 형태의 변수와 함수가 있을때 사용한다.
+ 클래스는 붕어빵 `틀`이다.
+ 클래스에 의해 만들어진 각각의 `결과`는 객체다.
+ 객체는 클래스에서 생성하므로 객체를 클래스의 `인스턴스,사례(Instance)`라고 한다.

클래스 선언 기본 구조
```python
class 클래스명 () : 
    변수1 #클래스변수
    변수2
    def 함수1(self[인자1,인자2,...]): #클래스 함수
        (code block)
    def 함수2(self[인자1,인자2,...]):
        (code block)
```
+ 클래스명은 알파벳 대문자로 시작한다. _함수와 대조적으로_
+ `self`는 객체 생성 후에 자신을 참조하는데 이용한다.
+ 인자는 필요한 만큼 사용하며, 필요 없을시 생략할 수 있다.
#
## 1. 객체 생성 및 활용
예) 사람 클래스
+ 사람이 갖는 속성과 동작을 정의
+ 사람의 속성(변수부): 나이, 성별, 키
+ 사람의 동작(함수부): 이동, 정지

```python
class Human: #클래스 선언
    pass
```
위 정의한 `Human` 클래스의 객체 생성할 수 있다.
jj_chun은 Human 클래스의 객체다.
```python
jj_chun = Human()
```
그리고 아래를 실행하면 클래스와 생성할 때 할당받은 메모리의 주소값을 출력한다. 
```python
jj_chun
```

위에 정의한 객체(object)에 속성값을 설정할 수 있다. 그리고 그 값을 불러올 수 있다.
```python
jj_chun.ages = 34
jj_chun.gender = "m"
jj_chun.height = 177

jj_chun.ages 
jj_chun.gender
jj_chun.height
```
out1 : 34\
out2 : 'm'\
out3 : 177
#
## 2. 클래스 선언
#
## 3. 클래스 상속
새로운 클래스를 선언할때 이미 존재하는 클래스와 유사점이 있다면, 클래스 상속을 통해 변수와 함수를 가져온다.
+ 부모 클래스 혹은 슈퍼 클래스라고 한다.
+ 자식 클래스 혹은 서브 클래스라고 한다.

클래스 상속의 예\
먼저 부모 클래스를 선언 (혹은 이미 존재하는)
```python
class Bicycle():
 
    def __init__(self, wheel_size, color)
        self.wheel_size
        self.color =color

    def move(self, speed) :
        print ("자전거: 시속 {0}킬로미터로 전진".format(speed))

    def turn(self, direction) :
        print ("자전거 : {0}회전".format(direction))

    def stop(self) :
        print ("자전거({0} & {1}): 정지 ".format(self.wheel_size,self.color))

```
위 부모 클래스를 바탕으로 자식 클래스를 생성 밎 상속.
```python
class FoldingBicycle(Bicycle) :
    def __init__(self, wheel_size, color, state):
        Bicycle.__init__(self. wheel_size, color)
       #super().__init__(wheel_size, color) #부모 클래스 명대신 사용가능 (self)생략
       self.state = state

    def fold(self) :
        self.state = 'folding'
        print ("자전거: 접기, state = {0}".format(self.state))

    def unfold(self) :
        self.state = 'unfolding'
        print ("자전거: 펴기, state ={0}".format(self.state))
```
새로운 클래스 변수 `state`추가 되었다.\
새로운 클래스 메서드 `fold,unfold`가 추가 되었다.

