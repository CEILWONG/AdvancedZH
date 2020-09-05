# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        out=[]

        if root==None:
            return []

        out.extend(self.inorderTraversal(root.left))
        out.append(root.val)
        out.extend(self.inorderTraversal(root.right))

        return out

