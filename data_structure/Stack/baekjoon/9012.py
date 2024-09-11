'''
5397.괄호

1. 기본 VPS -> ()
2. 추가 VPS -> 기본VPS + 기본VPS (접합)
3. 추가 VPS -> (vps) 즉, 기본vps 사이에 다른 vps도 추가가능
    ex. (()), ((()))
EX. (())(()), (())
즉, vps(vps) or vps단독 or vps+vps 가능하다는 의미 

접근법 
-> 스택을 활용하여 문자열을 활용해서 '('는 스택에 push하고 ')'는 스택에 저장되어 있는 (를 pop하여 하나의 ()를 
이루도록 구성 
-> 이때, ) 후 스택에서 꺼내올 (가 없다면 이는 vps가 아님을 나타냄
'''

class stack(object):
    def __init__(self):
        self.s = []
    
    def insert(self, v):
        self.s.append(v)
    
    def remove(self):
        self.s.pop()

num = int(input())
for _ in range(num):
    stackk = stack()
    s = input()
    for idx, i in enumerate(s):
        if i == '(':
            stackk.insert(i)
            if idx == len(s)-1:
                print("NO") 
        elif i == ')':
            if len(stackk.s) >= 1 :
                stackk.remove()
                if (len(stackk.s) == 0) and (idx == len(s)-1):
                    print("YES") 
                elif (len(stackk.s) != 0) and (idx == len(s)-1):
                    print("NO")  
            else:
                print("NO")
                break




