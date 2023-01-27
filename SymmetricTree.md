# [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

## EASY (Fri 27 Jan 2023)

==GOT HINTS==

# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

My first idea was to treat each node as its own root, and compare the left and right side to see if they are symmetrical, but noticed this was not right. It was only asking for if symmetrical at the root they gave us.

# Approach

<!-- Describe your approach to solving the problem. -->

I then realised that instead I need to compare the root.left and the root.right of the nodes at each level.

# Complexity

- Time complexity:
  <!-- Add your time complexity here, e.g. $$O(n)$$ -->

  $$O(|V|)$$
  where V is the number of nodes

- Space complexity:
  <!-- Add your space complexity here, e.g. $$O(n)$$ -->
  $$O(|D|)$$
  where D is the maximal depth of the tree. In the case of a balanced tree, the space complexity will be O(log(|V|)) as this the maximal depth of a balanced tree and unbalanced tree is O(|V|) as this is the worst case.

# Code

## Attempt 1 (fail)

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root.left is None and root.right is None:
            print("going into 0")
            return True
        elif root.left is None and root.right is not None:
            print("going into 1")
            return False
        elif root.left is not None and root.right is None:
            print("going into 2")
            return False

        leftTree = self.isSymmetric(root.left)
        rightTree = self.isSymmetric(root.right)
        print("rightTree is ", rightTree, "when root is ", root.val)
        print("leftTree is ", leftTree, "when root is ", root.val)
        print("root.left.val == root.right.val", root.left.val == root.right.val)
        print("=============")

        return root.left.val == root.right.val and leftTree and rightTree

```

## Attempt 2

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def compare(leftTree: Optional[TreeNode], rightTree: Optional[TreeNode]) -> bool:
    if leftTree is None and rightTree is None:
        return True
    elif leftTree is None and rightTree is not None:
        return False
    elif leftTree is not None and rightTree is None:
        return False

    return leftTree.val == rightTree.val and compare(leftTree.left, rightTree.right) and compare(leftTree.right, rightTree.left)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return compare(root.left, root.right)
```
