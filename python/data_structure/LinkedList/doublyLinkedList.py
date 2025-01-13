class Node2(object):
    def __init__(self, value=0, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class doublyLinkedList(object):
    def __init__(self):
        self.head = None # head : 가장 앞쪽 node를 가리키는 포인터
        self.tail = None # tail : 가장 뒷쪽 node를 가리키는 포인터 
    
    def insert_bk(self, value):
        new_node = Node2(value)
        if self.head is None:
           self.head = new_node
           self.tail = new_node
        else:
            self.tail.next = new_node  # 현재 tail의 next를 새로 생성된 node로 설정
            self.tail = self.tail.next # tail을 new_node로 갱신하여 최종적으로 현재 마지막 노드는 new_node가 됨

    def insert_fr(self, value):
        new_node = Node2(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node
    
    def insert_at(self,idx,value):
        if idx == 0 :
            self.insert_fr(value)
        else:
            current = self.head
            for _ in range(idx-1):
                if current is None:
                    raise IndexError("Index out of bounds")
                current = current.next
            if current == self.tail:
                self.insert_bk(value)
            else:
                new_node = Node2(value)
                next_node = current.next
                current.next = new_node
                new_node.prev = current
                new_node.next = next_node
                next_node.prev = new_node

    def remove_idx(self, idx): 





