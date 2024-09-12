'''
10845. 큐 구현하기
'''
import sys

class Queue(object):
    def __init__(self):
        self.queue = []
    
    def push(self, x):
        self.queue.insert(0, x)
        print(x)
    
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
            print(self.queue[len(self.queue)-1])
        else:
            print("-1")
    
    def back(self):
        if len(self.queue) >= 1:
            print(self.queue[0])
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
