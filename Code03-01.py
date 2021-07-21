

## 함수
def add_data(friend) : # 함수 = Function = 기능
    
    katok.append(None)
    klen = len(katok)
    katok[klen-1] = friend

## 전역변수
katok = [ ] #빈 배렬

## 메인코드
add_data('다현')
add_data('정형')
add_data('쯔위')
add_data('사나')
add_data('지효')


print(katok)