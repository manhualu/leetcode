"""
    Maximum Depth of Binary Tree
        EASY (Sat 24 Dec 2022)
    https://leetcode.com/problems/maximum-depth-of-binary-tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None: 
            return 0

        # Get the maxDepth of the right tree
        rightDepth = self.maxDepth(root.right)

        # Get the maxDepth of the left tree
        leftDepth = self.maxDepth(root.left)

        # Choose the tree that is deeper and add 1 to account for root node
        if rightDepth > leftDepth:
            return rightDepth + 1
        else:
            return leftDepth + 1
