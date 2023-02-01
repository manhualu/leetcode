# [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)

## EASY (Wed 1 Feb 2023)

==GAVE UP== was very close, but failed a few edge cases

# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

Similar to the [Same Tree](https://leetcode.com/problems/same-tree/) leetcode problem.

# Approach

<!-- Describe your approach to solving the problem. -->

I looked online for the best algorithm to build a height-balanced tree. I learnt how to make a TreeNode lol.

My problem was that I should not immediately return rightTree and leftTree if root.val == subRoot.val. This is because this assumes not repeated val appear in the tree and just moves the pointer on subRoot. Instead it only returns true if leftSubtree and rightSubtree is definitely identical too. Otherwise, it doesn't move subRoot pointer.

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

## Failed Approach

This approach assumes that a value appears at most once in the BST and cannot be repeated.

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # Move the pointer on subRoot, if root.val == subRoot.val
        if root is None and subRoot is None:
            return True
        elif root is not None and subRoot is None:
            return False
        elif root is None and subRoot is not None:
            return False

        # Haven't found similar structure, so don't move pointer on subRoot
        if root.val != subRoot.val:
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

        return self.isSubtree(root.right, subRoot.right) and self.isSubtree(root.left, subRoot.left)
```
