'''
20. Valid Parentheses

생각> 
1. 각각의 (, {, [는 닫힌괄호 ),},]와 대응되어야 함
2. 열린-닫힌이 하나의 대응체이기에 총 개수는 짝수이어야 함
3. 닫힌이 먼저 나올수는 없음 

접근>
1. 리스트를 형성 후 입력 문자열을 반복문을 통해 열린괄호는 리스트에 append하고 닫힌 괄호가 오면
리스트의 열린괄호들을 LIFO형태로 닫힌 괄호와 대응 시켜서 최종적으로 리스트의 개수가 0개가 되면 됨
2. 문제점 -> 근데 (] , [}와 같은 형태는 호환이 안됌 
3. 
'''

class Solution(object):
    def isValid(self, s):
        k = []
        # s = s[1:-1]
        cnt = 0
        for i in s:
            if i in "({[":
                k.append(i)
            elif i in ")}]":
                if len(k) == 0:
                    cnt += 1
                else:
                    y = k.pop()
                    if (y == '(' and i != ')') or (y == '[' and i != ']') or (y == '{' and i =='}'):
                        cnt += 0
                    else:
                        


              
l = Solution()
s = input()
l.isValid(s)