# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Queue:
    def __init__(self):
        self.list=[]

    def putin(self,Node):
        self.list.insert(0,Node)

    def pushout(self):
        return self.list.pop()


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        out=[]
        q1=Queue()
        q2=Queue()
        if root==None:
            return out

        q1.putin(root)
        while q1.list!=[] or q2.list!=[]:
            active=q1 if q1.list else q2
            standby=q2 if active==q1 else q1
            thisfloor=[]
            while active.list!=[]:
                tmpNode=active.pushout()
                thisfloor.append(tmpNode.val)
                if tmpNode.left!=None:
                    standby.putin(tmpNode.left)
                if tmpNode.right!=None:
                    standby.putin(tmpNode.right)
            out.append(thisfloor)

        return out