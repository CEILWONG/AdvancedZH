# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1=l1
        p2=l2
        head=now=ListNode(0,None)
        while p1 and p2:
            if p1.val>p2.val:
                now.next=p2
                p2=p2.next
                now=now.next
            else:
                now.next=p1
                p1=p1.next
                now=now.next

        now.next=p2 if p2 else p1

        return head.next