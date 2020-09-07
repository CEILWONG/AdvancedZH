# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        Node=ListNode(None)

        Node.next=head

        now=Node

        while now.next!=None:
            if now.next.val==val:
                now.next=now.next.next
            else:
                now=now.next

        return Node.next