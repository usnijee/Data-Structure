## 에디터 

'''

L : 커서를 왼쪽으로 한 칸 옮김
D : 커서를 오른쪽으로 한 칸 옮김
B : 커서 왼쪽에 있는 문자 삭제 (커서가 맨 앞에 위치시 무시)
P $ : $라는 문자를 커서 왼쪽에 추가

'''
'''
접근>
1. 초기에 head와 tail이 가리키는 value가없는 노드가 생성되어 있고 cursor는 tail이 가리키는 노드를 같이 가리킴
2. 
'''

import sys
input = sys.stdin.readline
class Node(object):
    def __init__(self,value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class Editor(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.cursor = self.tail
    
    def insert_cursor_fr(self,cursor,value):
        pre_cur = cursor.prev 
        new_node = Node(value,cursor,pre_cur)
        pre_cur.next = new_node
        cursor.prev = new_node
    
    def remove(self):
        pre_cur = self.cursor.prev
        pre_cur.prev = self.cursor.prev
        pre_cur.prev.next = self.cursor

    def print_list(self):
        p = self.head.next
        while p != self.tail:
            if p.next != self.tail:
                print(p.value, end="")
            else:
                print(p.value)
            p = p.next
        
    
editor = Editor()               
n = list(input()) 
for i in range(len(n)):
    editor.insert_cursor_fr(editor.tail,n[i])

num = int(input())
for _ in range(num):
    order = list(input())
    if order[0] == 'L':
        if editor.cursor.prev.prev is not None:
            editor.cursor = editor.cursor.prev
    elif order[0] == 'D':
        if editor.cursor.next is not None:
            editor.cursor = editor.cursor.next
    elif order[0] == 'B':
        editor.remove()
    else:
        editor.insert_cursor_fr(editor.cursor,order[2])

editor.print_list()

