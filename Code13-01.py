#이진 검색
#검색 구현
## 함수
def binSearch(ary, fData) :
    pos = -1
    start = 0
    end = len(ary)-1

    while (start <= end) :
        mid = (start+end) // 2
        if fData == ary[mid] :
            return mid
        elif fData > ary[mid] :
            start = mid + 1
        else :
            end = mid -1

    return pos


## 전혁
dataAry = [11,22,33,44,55,66,77,88,99,110]
findData = 67
## 메인
print('배열-->',dataAry)
position = binSearch(dataAry, findData)
if position == -1 :
    print( '없음')
else :
    print(findData, '는', position, '위치에 있음')
        

