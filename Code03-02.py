## 리스트 삽입과 삭제
## 함수
def add_data(friend) : # 함수 = Function = 기능
    katok.append(None)
    klen = len(katok)
    katok[klen-1] = friend
    
def insert_data(position, friend) :
    katok.append(None)
    klen = len(katok)
    for i in range(klen-1, position, -1) :
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend
    
def delete_data(position) :
    klen = len(katok)
    katok[position] = None
    for i in range(position+1, klen, 1) :
        katok[i-1] = katok [i]
        katok[i] = None
    del(katok[klen-1])
    

## 전역변수
katok = [ ] #빈 배렬

## 메인코드
add_data('다현')
add_data('정형')
add_data('쯔위')
add_data('사나')
add_data('지효')


print(katok)

## 데이터 삽입
insert_data(3, '천준')
print(katok)
insert_data(1, '순순')
print(katok)

## 데이터 삭제
delete_data(2)
print(katok)