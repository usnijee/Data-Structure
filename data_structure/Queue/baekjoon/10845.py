'''
10845. 큐 구현하기

접근 > 입력과 출력을 살펴보면 일반적인 큐와달리 왼쪽에서 입력해서 오른쪽에서 출력되는 뒤집혀져있는 구조임
'''
import sys 

class Queue(object):
    def __init__(self):
        self.queue = []
    
    def push(self, x):
        self.queue.append(x)
    
    def pop(self):
        if len(self.queue) >= 1:
            print(self.queue.pop(0))
        else:
            print(-1)
    
    def size(self):
        print(len(self.queue))
    
    def empty(self):
        if len(self.queue) == 0:
            print(1)
        else:
            print(0)
    
    def front(self):
        if len(self.queue) >= 1:
            print(self.queue[0])
        else:
            print("-1")
    
    def back(self):
        if len(self.queue) >= 1:
            print(self.queue[-1])
        else:
            print("-1")

num = int(sys.stdin.readline())
q = Queue()
for _ in range(num):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        q.push(s[-1])
    elif s[0] == 'pop':
        q.pop()
    elif s[0] == 'size':
        q.size()
    elif s[0] == 'empty':
        q.empty()
    elif s[0] == 'front':
        q.front()
    elif s[0] == 'back':
        q.back()

# from collections import deque
# import sys

# input = sys.stdin.readline
# n = int(input())
# dq = deque()

# for _ in range(n):
#     command = list(input().split())
#     if command[0] == 'push':
#         dq.append(command[1])
#         print(command[1])
#     elif command[0] == 'pop':
#         if len(dq) > 0 :
#             tmp = dq.popleft()
#             print(tmp)
#         else : print(-1)
#     elif command[0] == 'size':
#         print(len(dq))
#     elif command [0] == 'empty':
#         if len(dq) > 0: print(0)
#         else : print(1)
#     elif command[0] == 'front':
#         if len(dq) > 0: print(dq[0])
#         else : print(-1)
#     elif command [0] == 'back':
#         if len(dq) > 0: print(dq[-1])
#         else: print(-1)