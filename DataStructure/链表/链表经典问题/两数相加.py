# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1=l1
        p2=l2
        p3=head=ListNode(0)
        addnum=0

        while p1 and p2:
            tmpNode=ListNode(0)
            p3.next=tmpNode
            p3=p3.next
            p3.val=(p1.val+p2.val+addnum)%10
            addnum=(p2.val+p2.val+addnum)//10

            p1=p1.next
            p2=p2.next

        rest=p2 if p2 else p1
        while p2 and addnum!=0
            