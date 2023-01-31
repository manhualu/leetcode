# [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

## EASY (Tue 31 Jan 2023)

==GAVE UP==

# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

A height-balanced binary tree is a binary tree in which the height of the two subtrees of every node never differs by more than one.

# Approach

<!-- Describe your approach to solving the problem. -->

I looked online for the best algorithm to build a height-balanced tree. I learnt how to make a TreeNode lol.

# Complexity

- Time complexity:
  <!-- Add your time complexity here, e.g. $$O(n)$$ -->

  $$O(n)$$
  for number of nodes being created

- Space complexity:
  <!-- Add your space complexity here, e.g. $$O(n)$$ -->
  $$O(logn)$$
  for recursive stack space where logn is height of the tree

# Code

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

def buildBST(nums: List[int], lo: int, hi: int) -> Optional[TreeNode]:
    if lo > hi:
        return None

    mid = math.floor( (lo + hi)/2 )
    root = TreeNode(nums[mid])

    root.left = buildBST(nums, lo, mid-1)
    root.right = buildBST(nums, mid+1, hi)

    return root


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return buildBST(nums, 0, len(nums) - 1)
```
