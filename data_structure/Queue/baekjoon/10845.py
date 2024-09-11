'''
10845. 큐 구현하기
'''
class Queue(object):
    def __init__(self):
        self.queue = []
    
    def push(self, x):
        self.queue.append(x)
    
    def pop(self):
        if len(self.queue) >= 1:
            print(self.queue.pop(0))
        else:
            print("-1")
    
    def size(self):
        print(len(self.queue))
    
    def empty(self):
        if len(self.queue) == 0:
            print("1")
        else:
            print("0")
    
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

num = int(input())
for _ in range(num):
    