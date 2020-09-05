
'''

假设1000个数，100个大小的哈希表
'''

class Node:
    def __init__(self,item):
        self.key=item
        self.next=None

class myhashset:
    def __init__(self,size):
        self.size=size
        self.alist=[None]*self.size


    def hashfunc(self,key):
        return key%self.size

    def add(self,key):
        if self.contains(key):
            return NULL
        toAddNode=Node(key)
        slot=self.hashfunc(key)

        if self.alist[slot]==None:
            self.alist[slot]=toAddNode
        else:
            toAddNode.next=self.alist[slot].next
            self.alist[slot].next=toAddNode

    def remove(self,key):

        slot=self.hashfunc(key)
        if self.alist[slot]==None:
            return  False
        elif self.alist[slot].key==key:
            tmp=self.alist[slot]
            self.alist[slot]=tmp.next
        else:
            head=Node(None)
            head.next=self.alist[slot]
            while head.next.key!=key and head.next.next!=None:
                head=head.next

            if head.next.key==key:
                head.next=head.next.next
            else:
                return False

    def contains(self,key):
        slot=self.hashfunc(key)
        if self.alist[slot]==None:
            return  False
        else:
            head=Node(None)
            head.next=self.alist[slot]
            while head.next.key!=key and head.next.next!=None:
                head=head.next

            if head.next.key==key:
                return True
            else:
                return False



wzh=myhashset(10)
wzh.add(3)
wzh.add(2)
wzh.add(12)


print(wzh.alist[2].key)
print(wzh.alist[2].next.key)
wzh.remove(2)

print(wzh.contains(2))