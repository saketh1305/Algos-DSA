from typing import List
class Solution:
    def max_sum(nums : List):
        max_sum = float('-inf')
        curr_sum = 0
        n = len(nums)
        
        for i in range(n):
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        
        
        return max_sum