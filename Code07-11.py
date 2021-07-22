# 원형 큐
## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if (rear + 1)%SIZE == front :
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else:
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅!')
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅!')
        return None
    return queue[(front+1) % SIZE]

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front, rear = 0, 0 #수정
