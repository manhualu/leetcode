[Move Zeroes](https://leetcode.com/problems/move-zeroes/)

## EASY (Sun 8 Jan 2023)

==GAVE UP==

# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

My first thoughts were inefficient. It would loop through the array and when it hits a 0, it will swap that 0 with all the numbers on its right so it ends up at the end of the array. This would at most take O(n^2) element. However, would use no memory.
My second thoughts was better than the O(n^2) time complexity.

# Approach

<!-- Describe your approach to solving the problem. -->

By getting all the non zero numbers into an array and then looping through the og nums to replace the first positions with the non zero numbers from the first array.
Although this came at a tradeoff/cost of the space complexity as we have a non zero numbers array.

# Complexity

- Time complexity:
  <!-- Add your time complexity here, e.g. $$O(n)$$ -->

  $$O(n) + O(n) = O(n)$$

- Space complexity:
  <!-- Add your space complexity here, e.g. $$O(n)$$ -->
  $$O(n)$$

# Code

```py
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZeroNums = []

        for num in nums:
            if num != 0:
                nonZeroNums.append(num)

        i = 0
        numOfNonZeroNums = len(nonZeroNums)

        while (i < len(nums)):

            if i < numOfNonZeroNums:
                nums[i] = nonZeroNums[i]
            else:
                nums[i] = 0

            i += 1


        return nums
```
