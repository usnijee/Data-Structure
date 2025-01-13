'''
백준 2164번. 카드2

접근1. 단순히 pop과 append로 리스트의 요소를 빼고 추가하는 방식-> 시간복잡도가 Q(n)
접근2. deque()를 이용한 방식 -> popleft는 Q(n)

'''
from collections import deque

class Queue(object):
    def __init__(self, n):
        self.cage = deque([i for i in range(1, n+1)])

    def removeandinsert(self):
        while len(self.cage)>1:
            self.cage.popleft()  # O(1) 시간 복잡도
            self.cage.append(self.cage.popleft())  # O(1) 시간 복잡도
        return self.cage[0]

n = int(input())
q = Queue(n)
print(q.removeandinsert())
        
