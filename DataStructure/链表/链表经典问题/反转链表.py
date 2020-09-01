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

    def showall(self):

        tmp=self.head
        while tmp!=None and tmp.next!=None:
            print(tmp.key)
            tmp=tmp.next
        if tmp!=None:
            print(tmp.key)

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

        while current!=None and current.next!=None:
            current=current.next

        if current==None:
            tmp.next=None
            self.head=tmp
        else:
            tmp.next=current.next
            current.next=tmp

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        times=0
        current=self.head
        previous=None
        while index>0 and times!=index:
            if current==None:
                return False
            else:
                times+=1
                previous=current
                current=current.next

        tmp=Node(val)
        if previous==None:
            #tmp=Node(val)
            tmp.next=current
            self.head=tmp
        else:
            tmp.next=previous.next
            previous.next=tmp


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index<0:
            return False

        times=0
        current=self.head
        previous=None
        while current!=None and times!=index:
            previous=current
            current=current.next
            times+=1

        if times!=index or current==None:
            return False
        elif previous==None:
            self.head=current.next
        else:
            previous.next=current.next


def getalink():
    la=MyLinkedList()
    la.addAtTail(0)
    la.addAtTail(1)
    la.addAtTail(2)
    la.addAtTail(3)
    la.addAtTail(4)
    la.addAtTail(5)
    return la

la=getalink()