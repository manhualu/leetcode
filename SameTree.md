# [Same Tree](https://leetcode.com/problems/same-tree/)
##  EASY (Wed 28 Dec 2022)

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Divide and conquer obviously lol, by looking at the right tree and left tree. Then returning true if both the right tree and left tree return tree as well as if the current node of p and q is equal. 

# Approach
<!-- Describe your approach to solving the problem. -->
Recursion

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(|V|)$$ where V is the number of nodes

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(|D|)$$ where D is the maximal depth of the tree. In the case of a balanced tree, the space complexity will be O(log(|V|)) and unbalanced tree is O(|V|).

# Code
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: 
            print("going into here")
            return True
        elif p is None and q is not None:
            return False
        elif p is not None and q is None: 
            return False

        rightTree = self.isSameTree(p.right, q.right)
        leftTree = self.isSameTree(p.left, q.left)

        return (p.val == q.val) and (rightTree and leftTree)

```