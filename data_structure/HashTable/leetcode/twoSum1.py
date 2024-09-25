'''
다음과 같은 정수 배열 nums와 정수 target이 주어졌을 때, 두 수를 더해서 target이 되는 두 숫자의 인덱스를 반환하세요.
각 입력에 정확히 하나의 해답이 있다고 가정할 수 있으며, 동일한 요소를 두 번 사용할 수 없습니다.
답은 아무 순서로나 반환할 수 있습니다.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        table = {value:idx for idx, value in enumerate(nums)} 

        for i, num in enumerate(nums):
            if ((target-num) in table) and (i != table[(target-num)]):
                return [i, table[(target-num)]]


'''
접근 방법에 대해 생각해볼것

1. 해쉬테이블을 떠올릴수 있는 조건 

    1-1. 아무 순서로 반환 가능 (순서를 고려하지 않아도 됨)
    1-2. 해시 테이블은 접근/삽입/삭제에 대해 O(1)임을 항상 인지할 것  --> 즉, 순서만 자유롭다면 대상에 접근해서 삽입하거나 삭제하는 기능이 매우 빠름
    1-3. in연산자를 통해 1-2를 빠르게 구현 가능 


    즉, 순서를 고려하지 않아도 된다면 해시테이블을 떠올릴것
    또한 리스트가 필요하다면 리스트 컴프리헨션은 반드시 떠올릴것
'''
        
