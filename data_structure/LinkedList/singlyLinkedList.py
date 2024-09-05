# Node 클래스 생성
# value : node에 저장 된 값 
# next : next node의 주소값 

class Node(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next 

class singlyLinkedList(object):
    def __init__(self):
        self.head = None
    
    def insert_bk(self, value):
        new_node = Node(value)
        # head가 가리키는 것의 존재 유무로 1차 분기(head가 노드를 가리키는지 = 생성된 Node가 첫번째 노드인지)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, idx):
        if self.head is None:
            print("There aren't enough nodes")
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value  
    
    def insert(self, idx, value):
        new_node = Node(value)
        # insert를 첫번째 노드에 할 경우 
        if idx == 0:
            new_node.next = self.head # 새로운 node의 next가 현재 head가 가리키는 노드가 되도록
            self.head = new_node # head는 이제 새로운 node를 가리키도록 설정 
        else:
            current = self.head
            for _ in range(idx-1):
                current = current.next
            new_node.next = current.next # current 다음에 위치한 node가 new_node의 다음에 위치하도록 설정 
            current.next = new_node # current의 다음에 위치한 node가 new_node가 되도록 설정 
    
    def remove(self, idx):
        current = self.head
        if idx == 0:
            self.head = current.next
        else:
            for _ in range(idx-1):
                current = current.next
            current.next = current.next.next  # 이게 최선인가...

        


            

            
                


            
            
                
            



        

            




