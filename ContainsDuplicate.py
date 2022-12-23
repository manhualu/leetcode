"""
    Contains Duplicate
        EASY (Sat 24 Dec 2022)
    https://leetcode.com/problems/contains-duplicate/
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        # prev is float because array can only be integers, so not possible to fail on first element
        prev = 0.5
        
        for num in nums:
            if prev == num: 
                return True
            else:
                prev = num


        return False