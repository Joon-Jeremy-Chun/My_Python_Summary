## 이진 탐색 트리의 일반 구현
## 함수
class TreeNode() : # 트리노드의 틀 (붕어빵 기계)
    def __init__(self) :
        self.left = None
        self.data = None
        self.right = None
## 전역
memory = []
root = None
## 실제 데이터
nameAry = ['블랙핑크','레트벨벳','마마무','에어핑크,','트와이스','걸스데이']

## 메인
# 첫 노드 생성(약간 다름)
node = TreeNode()
node.data = nameAry[0]
root = node # 핵심
memory.append(root)

for name in nameAry[1:] :
    node =TreeNode()
    node.data = name
    
    current = root
    while True : # 몇번 비교해야 할지 모름.
        if name < current.data :
            if current.left == None :
                current.left = node
                break
            else :
                current = current.left
        else :
            if current.right == None :
                current.right = node
                break
            else :
                current = current.right
    memory.append(node)

## 테이터를 검색(=탐색)할때 완전 효율적
findName = '마마무'

current = root
while True :
    if current.data == findName :
        print(findName, '있음')
        break
    elif findName < current.data :
        if current.left == None :
            print('없음')
            break
        else :
            current = current.left
    else :
        if current.right == None :
            print('없음')
            break
        else :
            current = current.right

    