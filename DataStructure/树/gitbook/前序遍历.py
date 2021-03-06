# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        out=[]
        if root==None:
            return []

        out.append(root.val)
        out.extend(self.preorderTraversal(root.left))
        out.extend(self.preorderTraversal(root.right))

        return out

