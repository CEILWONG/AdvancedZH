# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if root==None:
            return 0

        leftmax=self.maxDepth(root.left)
        rightmax = self.maxDepth(root.right)

        maxdepth=(leftmax if leftmax>rightmax else rightmax)+1
        return maxdepth

