

class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

    def set_next(self,nextnode):
        self.next=nextnode

    def set_data(self,setdata):
        self.data=setdata


class Mylist(object):
    def __init__(self):
        self.head=None;

    def add(self,item):
        temp=Node(item)

        temp.next=self.head
        self.head=temp

    def size(self):

        current=self.head
        count=0

        while current!=None:
            count=count+1
            current=current.next
        return count

    def search(self,item):

        count=0
        current=self.head

        while current!=None:
            count=count+1
            if current.data==item:
                return count
            else:
                current=current.next

        return False

    def remove(self,item):
        current=self.head

        if current.data==item:
            self.head=current.next
        else:
            previous=current
            current=current.next

        while current!=None:
            if current.data==item:
                previous.next=current.next
                current=current.next

            else:
                current=current.next
                previous=previous.next




    def showit(self):

        current=self.head
        while not current == None:
            print(current.data)
            current=current.next
            #print(current.data)


def main():
    alist=Mylist()
    alist.add(3)
    alist.add(4)
    alist.add(8)
    alist.add(9)
    alist.add(10)
    alist.showit()
    print("size is : %d"%alist.size())

    print(alist.search(9))
    alist.remove(8)
    alist.showit()

main()