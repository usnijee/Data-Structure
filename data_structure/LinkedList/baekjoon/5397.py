'''
백준 5397번. 키로커

< : 화살표 왼쪽 키
> : 화살표 오른쪽 키
- : Backspace
'''
class Node(object):
    def __init__(self,value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class Kiroker(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.cursor = self.tail

    def insert_bk(self, cursor, value):
        new_node = Node(value)
        cur_prev = cursor.prev
        cur_prev.next = new_node
        cursor.prev = new_node
    
    def remove(self):
        cur_prev = self.cursor.prev
        self.cursor.prev = cur_prev.prev
        cur_prev.prev.next = self.cursor
    
    def printResults(self):
        p = self.head.next
        while p != self.tail:
            if p.next != self.tail:
                print(p.value,end="")
            else:
                print(p.value)
            p = p.next


kiro = Kiroker()    
n = int(input())
for _ in range(n):
    k = list(input())
    for i in k:
        if i == '<': 
            if kiro.cursor.prev is not None:
                kiro.cursor = kiro.cursor.prev
            else:
                pass
        elif i == '>':
            if kiro.cursor.next is not None:
                kiro.cursor = kiro.cursor.next
            else:
                pass
        elif i == '-':
            kiro.remove()
        else:
            kiro.insert_bk(kiro.cursor,i)

kiro.printResults()
            

        
