# 선형 큐
## 함수
#def isQueueFull() :
#    global SIZE, queue, front, rear 
#    if (rear >= SIZE-1) :
#        return True
#   else :
#       return False
    
def isQueueFull() :
    global SIZE, queue, front, rear 
    if (rear != SIZE -1) : 
        return False
    elif (rear == SIZE-1) and (front == -1) :
        return True
    else :
        for i in range(front+1, SIZE, 1) : 
            queue[i-1] = queue[i]
            queue[i] = None
        front -= -1
        rear -= -1
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
        front += 1
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
retData = peek()
print('다음 손님 대기하세요-->', retData)

#연습2
enQueue('E')
print('출구 <--', queue, '<--입구')

#연습3
# 전부 취소
deQueue()
deQueue()
deQueue()
deQueue()
deQueue()

retData = peek()
print('다음 손님 대기하세요-->', retData)

#연습4
