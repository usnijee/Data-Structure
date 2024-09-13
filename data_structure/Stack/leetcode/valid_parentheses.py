'''
20. Valid Parentheses

생각> 
1. 각각의 (, {, [는 닫힌괄호 ),},]와 대응되어야 함
2. 열린-닫힌이 하나의 대응체이기에 총 개수는 짝수이어야 함
3. 닫힌이 먼저 나올수는 없음 

접근>
->리스트를 형성 후 입력 문자열을 반복문을 통해 열린괄호는 리스트에 append하고 닫힌 괄호가 오면
리스트의 열린괄호들을 LIFO형태로 닫힌 괄호와 대응 시켜서 최종적으로 리스트의 개수가 0개가 되면 됨
'''

class Solution(object):
    def isValid(self, s):
        stack = []
        dic = {'(':')','{':'}','[':']'}
        for i in s:
            if i in dic.keys():
                stack.append(i)
            else:
                if stack and dic[stack[-1]] == i:  #딕셔너리를 이용하여 열린-닫힌의 쌍이 맞을때를 구현 
                    stack.pop()
                else:
                    return False
        if stack: # stack에 원소가 존재하는 경우 
            return False
        else:     # stack에 원속가 존재하지 않는 경우
            return True
        