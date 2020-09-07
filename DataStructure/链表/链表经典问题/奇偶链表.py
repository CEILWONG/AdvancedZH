# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head

        now=head
        secondNode=ListNode(None)
        secondNode.next=head.next
        tmp=head.next
        while now.next!=None and tmp.next!=None:
            now.next=now.next.next
            tmp.next=tmp.next.next
            now,tmp=now.next,tmp.next
        now.next=secondNode.next

        return head
