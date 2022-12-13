"""
Diameter of Binary Tree
    EASY (Wed 14 Dec 2022)
    
    https://leetcode.com/problems/diameter-of-binary-tree/ 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiameter = self.diameterOfBinaryTree(root.right)

        return max(leftHeight + rightHeight, max(leftDiameter, rightDiameter))


    def getHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        return max(leftHeight, rightHeight) + 1
