from collections import deque

d = deque()

d.append(1)
d.append(2)
d.popleft()

print(d)

p = deque([2,3])
print(p)