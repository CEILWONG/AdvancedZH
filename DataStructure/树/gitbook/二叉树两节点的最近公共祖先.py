# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Queue:
    def __init__(self):
        self.alist=[]

    def putin(self,val):
        self.alist.insert(0,val)

    def pushout(self):
        return self.alist.pop()

class Solution:
    def fatherDict(self,root):
        adict={}
        q=Queue()
        adict[root]=None
        q.putin(root)
        while q.alist:
            outNode=q.pushout()
            if outNode.left!=None:
                adict[outNode.left]=outNode
                q.putin(outNode.left)
            if outNode.right!=None:
                adict[outNode.right]=outNode
                q.putin(outNode.right)
        return adict

    def lowestCommonAncestor(self, root,p,q) -> 'TreeNode':
        adict=self.fatherDict(root)
        alist=[root]
        nowNode=p
        while adict[nowNode]!=None:
            alist.append(nowNode)
            nowNode=adict[nowNode]

        qnowNode=q
        while qnowNode not in alist:
            qnowNode=adict[qnowNode]

        return qnowNode


