"""
Two Sum
    EASY (Mon 5 Sept 2022)
    https://leetcode.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsLength = len(nums)
        i = 0
        
        while i < numsLength:
            # Skips iterating through numbers already looked at
            j = i + 1
            while j < numsLength:
                if nums[i] + nums[j] == target: 
                    return [i, j]
                j += 1

            i += 1
            
        return []
