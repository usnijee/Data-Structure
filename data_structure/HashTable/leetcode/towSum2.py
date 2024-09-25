'''
    2번째 해시테이블 풀이 
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for idx, value in enumerate(nums):
            if (target-value) in table: # O(1)
                return [idx, table[(target-value)]]
            else:
                table[value] = idx
 