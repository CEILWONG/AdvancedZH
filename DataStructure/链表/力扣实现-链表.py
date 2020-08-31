class Node:
    def __init__(self,data):
        self.key=data
        self.next=None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        times=0
        current=self.head
        while index>0 and times!=index:
            if current==None:
                return -1
            else:
                current=current.next
                times+=1

        if current==None or index<0:
            return -1
        else:
            return current.key

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        tmp=Node(val)
        tmp.next=self.head
        self.head=tmp

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        tmp=Node(val)
        current=self.head

        while current.next!=None:
            current=current.next

        tmp.next=current.next
        current.next=tmp

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        pass


wzh=MyLinkedList()
wzh.addAtHead(1)
wzh.addAtHead(2)
wzh.addAtHead(3)
output=wzh.get(3)
print(output)