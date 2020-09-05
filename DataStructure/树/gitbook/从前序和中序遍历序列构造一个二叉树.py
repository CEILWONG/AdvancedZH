# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if len(inorder)==0:
            return None

        rootval=preorder[0]
        node=TreeNode(rootval)

        root_inorder_index=inorder.index(rootval)

        left_inorder_list=inorder[0:root_inorder_index]
        left_preorder_list=preorder[1:len(left_inorder_list)+1]

        right_inorder_list=inorder[root_inorder_index+1::]
        right_preorder_list=preorder[len(left_inorder_list)+1::]

        node.left=self.buildTree(left_preorder_list,left_inorder_list)
        node.right=self.buildTree(right_preorder_list,right_inorder_list)

        return node