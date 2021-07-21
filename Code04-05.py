## 함수,클래스
class Node() : #붕어빵 기계
    def __init__(self) :
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end='  ')
    while current.link != None :
        current = current.link 
        print(current.data, end='  ')
    print()
    
def insert_node(findData, insertData):
    global memory, head, current, pre
    if (findData == head.data) :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if (current.data == findData) :
            node = Node()
            node.data =  insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return

def delete_node(delData) :
    global memory, head, current, pre
    if (head.data == delData) :
        current = head
        head = head.link
        del(current)
        return
    current = head
    while (current.link != None) :
        pre = current
        current = current.link
        if (current.data == delData) :
            pre.link = current.link
            del(current)
            return
        
def find_node(findData) :
    global memory, head, current, pre
    current = head
    if (current. data == findData) :
        return current
    while (current.link != None) :
        current = current.link()
        if (current. data == findData) :
            return current
    return Node() # 못찾는다면 빈 노드 반환
    
    

## 전역
memory = []
head, current, pre = None, None, None
# 데이터 집합(실무 DB, 웹클로링, 센서신호......)
dataArray = ['다현','정연','쯔위','사나','지효']

## 메인
# 첫 노드
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)

#그외 노드
for data in dataArray[1:] : 
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)
    
printNodes(head)

insert_node('다현', '화사')
printNodes(head)

insert_node('사나', '화사')
printNodes(head)

insert_node('천준', '문별')
printNodes(head)

delete_node('화사')
printNodes(head)

delete_node('화사')
printNodes(head)

delete_node('천준')
printNodes(head)

fNode = find_node('다현')
print(fNode.data)
Fdata = find_node('천준')
print(Fdata.data)
