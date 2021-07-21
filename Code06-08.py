## 함수
def isstackFull() : # 스택 full 여부
    global SIZE, stack, top
    if (top == SIZE -1) :
        return True
    else :
        return False
    
def push(data) : # 푸쉬
    global SIZE, stack, top
    if (isstackFull() == True) :
        print('Full!')
        return
    else : 
        top += 1
        stack[top] = data
    
## 전역
SIZE = 5
stack = [ None for _ in range(SIZE)]
top = -1

## 메인

push('커피1');push('커피2');push('커피3')
push('커피4');push('커피5')
print( '바닥 |', stack)
push('녹차')
print('바닥', stack)