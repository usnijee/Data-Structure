'''
deque(double-ended queue) : queue의 앞,뒤에서 삽입 삭제가 가능한 큐
''' 

from collections import deque

d = deque()

## append(x): 큐의 뒤로 삽입
d.append(1)
d.append(2)

## appendleft(x): 큐의 앞으로 삽입
d.appendleft(4)
d.appendleft(5)

#print(d) # deque([5,4,2,1])

## clear: 큐의 모든 요소를 삭제함.
d.clear()
#print(d)  # deque([])

## copy: 얕은 복사
d.append(12)
copied_d = d.copy()
#print(copied_d) # deque([12])

## count(x): 큐에서 x와 같은 값의 개수
d.append(1)
d.append(2)
d.append(3)
d.append(1)
#print(d.count(1)) #2

## extend(iterable): iterable한 값을 파라미터로 넣으면 해당 값들이 하나씩 큐의 오른쪽에 붙음
d.clear()
d.append('lft')  # deque([lft])
d.extend('lft')  # deque([l,f,t])
#print(d) # deque([lft,l,f,t])

## extendleft(iterable): iterable한 값을 파라미터로 넣으면 해당 값들이 하나씩 큐의 왼쪽에 붙음
d.extendleft('abc') 
#print(d) # deque(['c', 'b', 'a', 'lft', 'l', 'f', 't'])

## index(x[, start[, stop]]): 큐(인덱스 시작 후 및 인덱스 중지 전)에서 x의 위치를 반환. 첫 번째 일치를 반환하거나 찾을 수 없는 경우 ValueError 발생.
d.clear()
d.extend('abcxyzabcxyzabc')
#print(d.index('x',1,6)) # deque에서 인덱스 1~6사이의 최초'x'의 인덱스 값

## insert(i, x): i 위치에 x를 삽입
d.clear()
d.extendleft('usnijee')
d.insert(0,'e') 
# print(d) # deque(['e', 'e', 'e', 'j', 'i', 'n', 's', 'u'])

## pop(): 큐의 맨 오른쪽의 element를 삭제하고 반환. element가 없으면, IndexError가 발생.
d.pop()
# print(d) # deque(['e', 'e', 'e', 'j', 'i', 'n', 's'])

## popleft(): 큐의 맨 왼쪽의 element를 삭제하고 반환. element가 없으면, IndexError가 발생.
d.popleft()
# print(d) # deque(['e', 'e', 'j', 'i', 'n', 's'])

## remove(value): 큐에 있는 value 값 중 처음으로 등장한 value를 삭제. 못 찾으면, ValueError가 발생
d.remove('j')
# print(d) #deque(['e', 'e', 'i', 'n', 's'])

## reverse(): 큐를 제자리에서 반대로 뒤집는다. 반환값은 없음
d.reverse()
# print(d) #deque(['s', 'n', 'i', 'e', 'e']) 

## maxlen: 큐 생성 시, 정했던 큐의 최대 크기, 정하지 않았으면 None 반환
k = deque(maxlen=5)
# print(k.maxlen) #5