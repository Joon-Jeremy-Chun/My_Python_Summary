## 함수
def isStackFull() : # 스택 꽉 확인
    global SIZE, stack, top
    if (top == SIZE-1) :
        return True
    else :
        return False

def push(data) : # 푸쉬
    global SIZE, stack, top
    if (isStackFull() == True) :
        print('스택 꽉!')
        return
    top += 1
    stack[top] = data

def isStackEmpty() :
    global SIZE, stack, top
    if (top == -1) :
        print('empty')
        return True
    else:
        print('not empty')
        return False

def pop() :
    global SIZE, stack, top
    if(isStackEmpty()) :
        print('Staks already empty')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek() :
    global SIZE, stack, top
    if(isStackEmpty()) :
        print('empty')
    else :
        return stack[top]


## 전역
SIZE = 5
stack = [ None for _ in range(SIZE)]
top = -1

## 메인
push('커피1');push('커피2')
retData = peek()
print('다음에 나올것 -->', retData)
