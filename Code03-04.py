## 함수
def add_data(friend) :  # 함수 = Function = 기능
    katok.append(None)
    kLen = len(katok)
    katok[kLen - 1] = friend

def insert_data(position, friend) :
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1 ) :
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

def delete_data(position) :
    kLen = len(katok)
    katok[position] = None
    for i in range(position+1, kLen, 1) :
        katok[i-1] = katok[i]
        katok[i]=None
    del(katok[kLen-1])
## 전역
katok = []
select = -1 # 1추가, 2삽입, 3삭제, 4종료

## 기존대이터 연습
add_data('다현')
add_data('정형')
add_data('쯔위')
add_data('사나')
add_data('지효')


## 메인
while (select != 4) :
    select = int(input('선택(1추가, 2삽입, 3삭제, 4종료)-->'))

    if (select == 1) :
        data = input('추가할 친구-->') # 추가작동
        add_data(data)
        print(katok)
    elif(select == 2) :
        data1 = int(input('추가할 위치 -->')) # 추가작동
        data2 = input('추가할 친구 -->') # 추가작동
        insert_data(data1-1, data2)
        print(katok)
        pass # 삽입작동
    elif(select == 3) :
        data = int(input('삭제할 친구(번호)-->')) #추가작동
        delete_data(data-1)
        print(katok)
        
    elif(select == 4) :
        pass # 종료
    else:
        print('잘못 입력!')