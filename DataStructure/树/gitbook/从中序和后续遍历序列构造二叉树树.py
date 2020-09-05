# Definition for a binary tree node.
#基本思路：后序遍历序列中，根节点在最后一个；中序遍历序列中，根节点划分了左右子树
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:

        if len(inorder)==0:
            return None

        rootval=postorder[-1]
        node=TreeNode(rootval)

        root_inorder_index=inorder.index(rootval)

        left_inorder_list=inorder[0:root_inorder_index]
        left_postorder_list=postorder[0:len(left_inorder_list)]

        right_inorder_list=inorder[root_inorder_index+1::]
        right_postorder_list=postorder[len(left_inorder_list):-1]

        node.left=self.buildTree(left_inorder_list,left_postorder_list)
        node.right=self.buildTree(right_inorder_list,right_postorder_list)

        return node

# s=Solution()
# node=s.buildTree([9,3,15,20,7],[9,15,7,20,3])
#
# print(node.right.right.val)