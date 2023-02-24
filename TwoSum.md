# [Two Sum](https://leetcode.com/problems/two-sum/)

## EASY (Monday 5 Sept 2022)

# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

### Brute-force Approach

# Approach

<!-- Describe your approach to solving the problem. -->

### Bruteforce approach - O(n^2)

Generate all possible pairs and see if they get the target sum.

## Hash Map Solution - O(n)

Create a hash map that allows quick access to the index of a number by looking through the whole array

# Complexity

- Time complexity:
    <!-- Add your time complexity here, e.g. $$O(n)$$ -->

  Bruteforce approach - O(n^2)

  Hash Map Solution - O(n)

- Space complexity:
  <!-- Add your space complexity here, e.g. $$O(n)$$ -->

  Bruteforce approach - O(1)

  Hash Map Solution - O(n)

# Code

## Brute-force Approach - O(n^2)

```py
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

```

## Hash Map Approach - O(n)

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map solution

        # Create a hash map that allows quick access to the index of a number
        # by looking through the whole array
        numbersAndItsIndex = {}

        for i in range(len(nums)):
            numbersAndItsIndex[nums[i]] = i

        for i in range(len(nums)):
            # The second clause of the and statement ensures that a number is not looked at more than once
            if target - nums[i] in numbersAndItsIndex and i != numbersAndItsIndex[target-nums[i]]:
                return [i, numbersAndItsIndex[target-nums[i]]]

        return []

```
