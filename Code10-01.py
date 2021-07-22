## 함수
def openBox() :
    global count
    print('박스 열기')
    count -= 1
    if count == 0 :
        print("## 박스에 선물 넣기##")
        return
    openBox()
    
    print('박스 닫기!!!')
    return
## 변수
count = 10

## 메인
openBox()