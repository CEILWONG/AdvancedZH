# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root==None:
            return False

        if sum-root.val==0 and root.right==None and root.left==None:
            return True
        else:
            flag1=self.hasPathSum(root.left,sum-root.val)
            flag2=self.hasPathSum(root.right,sum-root.val)
            if flag1 or flag2:
                return True
            else:
                return False