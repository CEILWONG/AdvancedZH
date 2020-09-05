"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Queue:
    def __init__(self):
        self.alist=[]

    def putin(self,val):
        self.alist.insert(0,val)

    def pushout(self):
        return self.alist.pop()

class Solution:
    def connect(self, root) -> 'Node':
        if root==None:
            return None

        q1=Queue()
        q2=Queue()
        q1.putin(root)
        while q1.alist or q2.alist:
            act_q=q1 if q1.alist else q2
            sty_q=q2 if act_q==q1 else q1
            nowNode=act_q.pushout()
            if nowNode.left!=None:
                sty_q.putin(nowNode.left)
            if nowNode.right!=None:
                sty_q.putin(nowNode.right)

            while act_q.alist:
                nextNode=act_q.pushout()
                nowNode.next=nextNode
                nowNode=nextNode
                if nowNode.left != None:
                    sty_q.putin(nowNode.left)
                if nowNode.right != None:
                    sty_q.putin(nowNode.right)
            nowNode.next=None
        return root