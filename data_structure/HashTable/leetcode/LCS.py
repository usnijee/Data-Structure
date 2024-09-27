'''
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        num_set = set(nums) # 중복값 제거 
        max_length = 0 # 최대 길이 저장 변수 

        for num in nums:
            if num -1 not in num_set:
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)
        return max_length

# Test the function with the provided examples
k = Solution()
print(k.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
print(k.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # Output: 9

