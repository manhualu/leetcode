# [3 Sum](https://leetcode.com/problems/3sum/)

## MEDIUM (Friday 24 Feb 2023)

== FAILED ==

# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

### Brute-force Approach

# Approach

<!-- Describe your approach to solving the problem. -->

### Bruteforce approach - O(n^3)

Generate all possible triplets

## Hash Map Solution

This solution is similar to the 2Sum problem, but I was not able to fully understand and implement it : (

# Complexity

- Time complexity:
    <!-- Add your time complexity here, e.g. $$O(n)$$ -->

  Bruteforce approach - O(n^3)

- Space complexity:
  <!-- Add your space complexity here, e.g. $$O(n)$$ -->
  $$O(n)$$

# Code

## Brute-force Approach O(n^3) (FAILED, time limit exceeded)

```py
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute-force Approach, generate all possible triplets

        # Sort array
        nums.sort()

        result = []
        for i in range(len(nums)):
            # Skip over duplicates inside loop
            if (i != 0 and nums[i] == nums[i - 1]):
                 continue
            for j in range(i + 1, len(nums)):
                if (j != i + 1 and nums[j] == nums[j - 1]):
                     continue
                for k in range(j + 1, len(nums)):
                    if (k != j + 1 and nums[k] == nums[k - 1]):
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])

        return result
```
