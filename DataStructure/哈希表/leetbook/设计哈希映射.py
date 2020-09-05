class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size=10000
        self.alist=[None]*self.size

    def hashfunc(self,key):
        return key%self.size


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        aNode=Node(key,value)
        slot=self.hashfunc(key)
        if self.alist[slot]==None:
            self.alist[slot]=aNode
        else:
            now=self.alist[slot]
            while now.next!=None and now.key!=key:
                now=now.next

            if now.key==key:
                now.value=value
            else:
                aNode.next=now.next
                now.next=aNode

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        slot=self.hashfunc(key)
        if self.alist[slot]==None:
            return -1
        else:
            now=self.alist[slot]
            while now.next!=None and now.key!=key:
                now=now.next

            if now.key==key:
                return now.value
            else:
                return -1



    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        slot=self.hashfunc(key)
        if self.alist[slot]==None:
            return -1
        elif self.alist[slot].key==key:
            self.alist[slot]=self.alist[slot].next
        else:
            head=Node(key,None)
            head.next=self.alist[slot]
            while head.next.next!=None and head.next.key!=key:
                head=head.next

            if head.next.key==key:
                head.next=head.next.next
            else:
                return -1


wzh=MyHashMap()
#wzh.put(2,2)
wzh.put(2,1)
print(wzh.get(2))
wzh.remove(2)
print(wzh.get(2))
