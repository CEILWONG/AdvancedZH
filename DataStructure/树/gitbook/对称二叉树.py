# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def isSym(self,left,right):
        if left or right:
            if left==None or right==None:
                return False
            elif left.val==right.val:
                flag1=self.isSym(left.left,right.right)
                flag2=self.isSym(left.right,right.left)
                if flag1 and flag2:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return True

    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None:
            return True
        else:
            return self.isSym(root.left,root.right)