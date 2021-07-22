## 함수
def isQueueFull() :
    global SIZE, queue, front, rear 
    if (rear >= SIZE-1) :
        return True
    else :
        return False
def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('Full memory')
        return
    else :
        rear += 1
        queue[rear] = data
    
def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False
    
def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('Empty')
        return None
    else :
        front +=1
        data = queue[front]
        queue[front] = None
        return data
        
def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('Empty')
        return None
    else :
        return queue[front+1]

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front, rear = -1, -1

## 메인
#연습1
enQueue('A')
enQueue('B')
enQueue('C')
enQueue('D')
enQueue('E')

print('출구 <--', queue, '<--입구')
enQueue('E')
print('출구 <--', queue, '<--입구')

#연습2
retData = peek()
print('다음 손님 대기하세요-->', retData)
